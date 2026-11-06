import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CropTFIDFEngine:
    """
    TF-IDF based semantic search engine for crop-related knowledge.
    Answers ONLY when a crop is clearly mentioned.
    """

    def __init__(self, knowledge_dir="knowledge"):
        self.sentences = []
        self.crops = []

        for file_name in os.listdir(knowledge_dir):
            if file_name.endswith(".txt"):
                crop_name = file_name.replace(".txt", "").lower()
                file_path = os.path.join(knowledge_dir, file_name)

                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()
                        if line:
                            self.sentences.append(line)
                            self.crops.append(crop_name)

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.sentences)

    def get_answer(self, query):
        """
        Return the most relevant sentence ONLY if a crop is mentioned.
        Always returns (answer, score)
        """
        # ✅ FIX 1: Consistent return type
        if not self.sentences:
            return None, 0.0

        query_lower = query.lower()

        # Normalize plurals
        query_lower = (
            query_lower
            .replace("tomatoes", "tomato")
            .replace("potatoes", "potato")
            .replace("peppers", "pepper")
        )

        # Detect crop
        crop_filter = None
        for crop in set(self.crops):
            if crop in query_lower:
                crop_filter = crop
                break

        # ❌ No crop → NO answer
        # ✅ FIX 2: Consistent return type
        if crop_filter is None:
            return None, 0.0

        query_vector = self.vectorizer.transform([query_lower])
        similarity_scores = cosine_similarity(query_vector, self.vectors)[0]

        best_score = 0.0
        best_sentence = None

        for idx, score in enumerate(similarity_scores):
            if self.crops[idx] != crop_filter:
                continue
            if score > best_score:
                best_score = score
                best_sentence = self.sentences[idx]

        # Low confidence
        if best_score < 0.25:
            return None, 0.0

        return best_sentence, best_score