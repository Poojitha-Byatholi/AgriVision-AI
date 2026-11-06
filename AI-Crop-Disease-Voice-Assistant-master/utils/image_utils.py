import numpy as np
from PIL import Image
import hashlib

# --------------------------------------------------
# Image Preprocessing for CNN Model
# --------------------------------------------------

IMG_SIZE = 224  


def preprocess_image(image):
    """
    Preprocess PIL image for model prediction
    Steps:
    1. Convert to RGB
    2. Resize to model input size
    3. Normalize pixel values
    4. Expand dimensions (batch size = 1)
    """

    # Ensure image is in RGB
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Resize image
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert to numpy array
    image_array = np.array(image, dtype=np.float32)

    # Normalize (0–1)
    image_array /= 255.0

    # Add batch dimension (1, H, W, C)
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


# --------------------------------------------------
# Image Hashing (Fix Same Result Issue)
# --------------------------------------------------

def get_image_hash(image: Image.Image) -> str:
    """
    Generate a unique hash for uploaded image.
    Used to detect when a new image is uploaded.
    """
    return hashlib.md5(np.array(image)).hexdigest()


# --------------------------------------------------
# Crop Validation (Disclaimer Support)
# --------------------------------------------------

def is_valid_crop(predicted_class: str, trained_crops: list) -> bool:
    """
    Check if predicted class belongs to supported crops.
    """
    return any(crop.lower() in predicted_class.lower() for crop in trained_crops)
