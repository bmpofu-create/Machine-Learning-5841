import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
import pandas as pd

# Load model
model = load_model("driver_model.h5")

# Class names
class_names = [
    "drinking",
    "hair and makeup",
    "operating the radio",
    "reaching behind",
    "safe driving",
    "talking on the phone",
    "talking to passenger",
    "texting"
]

st.title("🚗 Distracted Driver Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array, verbose=0)[0]

    pred_idx = int(np.argmax(preds))
    pred_class = class_names[pred_idx]
    confidence = preds[pred_idx]

    st.subheader(f"Prediction: {pred_class}")
    st.write(f"Confidence: {confidence:.2%}")

    # Top 3
    st.subheader("Top 3 Predictions")
    top3 = np.argsort(preds)[::-1][:3]
    for i in top3:
        st.write(f"{class_names[i]}: {preds[i]:.2%}")

    # ✅ Bar chart (NOW IN CORRECT PLACE)
    st.subheader("Prediction Confidence Distribution")

    pred_df = pd.DataFrame({
        "Class": class_names,
        "Confidence": preds
    }).sort_values(by="Confidence", ascending=False)

    st.bar_chart(pred_df.set_index("Class"))