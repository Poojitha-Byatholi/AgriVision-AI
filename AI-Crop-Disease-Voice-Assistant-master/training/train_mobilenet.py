import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -----------------------------
# Correct dataset paths
# -----------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

TRAIN_DIR = os.path.join(BASE_DIR, "data", "raw", "train")
VAL_DIR   = os.path.join(BASE_DIR, "data", "raw", "val")

# -----------------------------
# Image settings
# -----------------------------
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen   = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

val_generator = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

print("Class labels found:")
print(train_generator.class_indices)


from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

# -----------------------------
# Load MobileNetV2 base model
# -----------------------------
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False

# -----------------------------
# Add custom classification head
# -----------------------------
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.5)(x)

predictions = Dense(
    train_generator.num_classes,
    activation="softmax"
)(x)

model = Model(inputs=base_model.input, outputs=predictions)

# -----------------------------
# Print model summary
# -----------------------------
model.summary()

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# -----------------------------
# Compile model
# -----------------------------
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Callbacks
# -----------------------------
checkpoint_path = os.path.join(BASE_DIR, "models")
os.makedirs(checkpoint_path, exist_ok=True)

checkpoint = ModelCheckpoint(
    filepath=os.path.join(checkpoint_path, "mobilenet_crop_disease.h5"),
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

# -----------------------------
# Train model
# -----------------------------
EPOCHS = 10

history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS,
    callbacks=[checkpoint, early_stop]
)


import matplotlib.pyplot as plt

# Accuracy plot
plt.figure()
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")
plt.legend()
plt.savefig("models/accuracy_plot.png")
plt.show()

# Loss plot
plt.figure()
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.savefig("models/loss_plot.png")
plt.show()

import pandas as pd
import os

# -----------------------------
# Save epoch-wise training data
# -----------------------------
results_dir = os.path.join(BASE_DIR, "results")
os.makedirs(results_dir, exist_ok=True)

history_df = pd.DataFrame(history.history)

csv_file = os.path.join(results_dir, "training_history.csv")
history_df.to_csv(csv_file, index=False)

print(f"Epoch-wise training data saved to: {csv_file}")
