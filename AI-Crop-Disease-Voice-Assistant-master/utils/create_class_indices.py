import os
import json
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TRAIN_DIR = os.path.join(BASE_DIR, "data", "raw", "train")

datagen = ImageDataGenerator(rescale=1./255)

generator = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical"
)

class_indices = generator.class_indices

output_path = os.path.join(BASE_DIR, "models", "class_indices.json")

with open(output_path, "w") as f:
    json.dump(class_indices, f, indent=4)

print("class_indices.json saved to models/")
print(class_indices)
