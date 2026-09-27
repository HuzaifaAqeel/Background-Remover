import streamlit as st
import time
import warnings
import onnxruntime  # noqa: F401  (import order fix for GPU access quirks)
from rembg import remove, new_session
from PIL import Image


warnings.filterwarnings("ignore")
st.title("Remove Background")
st.divider()

model_choice = st.selectbox(
    "Model",
    options=["u2netp (fast, lightweight)", "u2net (high quality, needs more RAM)"],
    index=0,
    help="u2netp is a 4.7MB model that runs anywhere; u2net is 176MB and more accurate.",
)
session_name = "u2net" if model_choice.startswith("u2net (") else "u2netp"

uploaded_file = st.file_uploader("Upload a png file to remove background", type="png")

if uploaded_file:
    st.image(uploaded_file, caption='Original')
    if st.button("Remove"):
        with st.spinner("Removing..."):
            input = Image.open(uploaded_file)
            session = new_session(session_name)
            output = remove(input, session=session)
            now = str(time.strftime("%Y%m%d-%H%M%S"))
            filename = now + ".png"
            output.save(filename)
            st.image(output, caption='Result')
