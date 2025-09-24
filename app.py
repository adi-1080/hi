import streamlit as st
from PIL import Image
import io
from ultralytics import YOLO
from src.utilities.get_prediction import get_prediction
from src.utilities.read_image import readImage

import cv2, sys
print("cv2 file:", cv2.__file__)
print("python:", sys.version)

# Set page config
st.set_page_config(
    page_title="Cattle & Buffalo Breed Classification",
    page_icon="🐄",
    layout="centered"
)

# Title
st.title("Cattle & Buffalo Breed Classification")
st.write("Upload an image of cattle or buffalo to identify its breed")

# Load the model
@st.cache_resource
def load_model():
    model = YOLO('src/models/yolo11n-cls.pt')
    return model

model = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    # Make prediction when button is clicked
    if st.button('Detect Breed'):
        with st.spinner('Analyzing image...'):
            # Convert uploaded file to bytes
            bytes_data = uploaded_file.getvalue()
            # Read image using the existing utility
            processed_image = readImage(bytes_data)
            
            # Get prediction
            pred_class, confidence = get_prediction(model, processed_image)
            
            # Display results
            st.success('Analysis Complete!')
            st.write('### Results:')
            st.write(f'**Predicted Breed:** {pred_class}')
            st.write(f'**Confidence Score:** {confidence:.2%}')

# Add information about the model
st.sidebar.header("About")
st.sidebar.write("""
This application uses a YOLO model trained to classify cattle and buffalo breeds.
Upload a clear image of cattle or buffalo to identify its breed.

The model can identify various indigenous and cross-bred varieties of:
- Cattle (Cows)
- Buffaloes
""")