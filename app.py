import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json

# Load model
model = tf.keras.models.load_model('veg_disease_model.h5')

# Load class names from JSON
with open('class_names.json', 'r') as f:
    class_names = json.load(f)

st.title("🌱 Vegetable Leaf Disease Detector")

uploaded_file = st.file_uploader("Upload a leaf image", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((224, 224))
    img_arr = np.expand_dims(np.array(img) / 255.0, axis=0)

    pred = model.predict(img_arr)
    predicted_class = class_names[np.argmax(pred)]

    st.success(f"✅ Prediction: **{predicted_class}**")
