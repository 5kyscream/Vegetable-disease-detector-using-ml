# 🥦🌿 Vegetable Disease Detector using Machine Learning

This project is an end-to-end deep learning pipeline to **detect diseases in vegetable leaves**.  
It uses **TensorFlow**, **Keras**, and a **Streamlit web app** for easy image classification.

---

## 🚀 Features

✅ Trained deep learning model (MobileNetV2)  
✅ Supports multiple vegetable crops and disease types  
✅ Simple Streamlit app for uploading and predicting leaf health  
✅ Organized dataset with train/test splits  
✅ Runs on CPU or GPU

---

## 📁 Project Structure

📂 leaf-disease-detector/
│
├── train.py # Model training script
├── app.py # Streamlit app for prediction
├── veg_disease_model.h5 # Saved trained model
├── requirements.txt # Python dependencies
├── .gitignore # Ignoring large files & datasets
├── dataset/ # (ignored in Git) Raw & split image data
├── raw/ # (ignored) Original raw images
├── generated_for_paper/ # (ignored) Extra generated data
├── README.md # This file!


---

## ⚡️ Quick Start

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/Vegetable-disease-detector-using-ml.git
cd Vegetable-disease-detector-using-ml

2️⃣ Install dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Run the Streamlit app

streamlit run app.py

Visit http://localhost:8501 in your browser, upload a leaf image, and check the prediction!
📈 Model Details

    Base model: MobileNetV2 with transfer learning

    Classes: Multiple vegetables (Tomato, Potato, Corn, Pepper, etc.) with healthy & diseased states

    Input: Single leaf per image (works best when the leaf is clear & centered)

🔮 Future Work

✅ Improve detection on images with multiple leaves
✅ Add object detection to locate each leaf and classify individually
✅ Add more vegetable classes & diseases
✅ Deploy on mobile devices with TensorFlow Lite
✅ Integrate a feedback loop for users to help improve model accuracy
📝 License

This project is open-source.
Feel free to fork it, improve it, and contribute!
🙌 Acknowledgments

    PlantVillage dataset

    TensorFlow, Keras, Streamlit

    BFG Repo-Cleaner for keeping this repo small and clean!

Made with ❤️ for smart farming.
>>>>>>> 667c4572bca9b0e22d6732da57d9f9ebe0f780d3
