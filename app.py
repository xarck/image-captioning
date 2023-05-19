import streamlit as st
from io import StringIO
from PIL import Image
import io
from main import predict_caption

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    image = Image.open(io.BytesIO(bytes_data))
    preds = predict_caption(image)
    st.write(preds[0])
