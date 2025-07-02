import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential

print("✅ TensorFlow version:", tf.__version__)
print("✅ Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))

# Data
train_dir = "dataset/train"
val_dir = "dataset/val"

train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(train_dir, target_size=(224,224), batch_size=32)
val_data = val_gen.flow_from_directory(val_dir, target_size=(224,224), batch_size=32)

# Model
base = MobileNetV2(include_top=False, weights='imagenet', input_shape=(224,224,3))
base.trainable = False

model = Sequential([
    base,
    GlobalAveragePooling2D(),
    Dense(len(train_data.class_indices), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train
model.fit(train_data, validation_data=val_data, epochs=7)

# Save
model.save("veg_disease_model.h5")
print("✅ Model saved as veg_disease_model.h5")
