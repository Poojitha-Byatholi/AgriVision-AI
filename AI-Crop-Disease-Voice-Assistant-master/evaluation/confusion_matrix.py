import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MODEL_PATH = os.path.join(BASE_DIR, "models", "mobilenet_crop_disease.h5")
VAL_DIR = os.path.join(BASE_DIR, "data", "raw", "val")

model = tf.keras.models.load_model(MODEL_PATH)

datagen = ImageDataGenerator(rescale=1./255)

val_generator = datagen.flow_from_directory(
    VAL_DIR,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical",
    shuffle=False
)

preds = model.predict(val_generator)
y_pred = np.argmax(preds, axis=1)
y_true = val_generator.classes

cm = confusion_matrix(y_true, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=val_generator.class_indices.keys()
)

plt.figure(figsize=(12, 12))
disp.plot(xticks_rotation=90)
plt.title("Confusion Matrix - Crop Disease Classification")
plt.savefig(os.path.join(BASE_DIR, "models", "confusion_matrix.png"))
plt.show()
