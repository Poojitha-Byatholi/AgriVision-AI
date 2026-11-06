def get_remedy(remedies_data, crop, disease):
    crop = crop.lower()
    disease = disease.lower().replace(" ", "_")

    if crop not in remedies_data:
        return None, f"No data available for crop: {crop}"

    if disease not in remedies_data[crop]:
        return None, f"No data available for {disease} in {crop}"

    return remedies_data[crop][disease], None
