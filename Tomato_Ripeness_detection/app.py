import streamlit as st
import pickle
from utils.data_utils import preprocess_image

st.set_page_config(page_title="Tomato Ripeness Classifier", layout="centered")
st.title("🍅 Tomato Ripeness Classifier")
st.write("Upload a tomato image to check if it's **Riped** or **Unriped**.")

# Load model
@st.cache_resource
def load_model():
    with open("model/logistic_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Upload image
uploaded_file = st.file_uploader("Choose a tomato image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    temp_path = f"temp_image.{uploaded_file.type.split('/')[-1]}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    img_rgb, img_flat = preprocess_image(temp_path)
    prediction = model.predict(img_flat)[0]
    label = "🍅 Riped" if prediction == 1 else "🟢 Unriped"

    st.image(img_rgb, caption=f"Prediction: {label}", use_column_width=True)
