from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize GenerativeModel
model = genai.GenerativeModel("gemini-pro-vision")
model2 = genai.GenerativeModel("gemini-pro")
# Streamlit UI
st.set_page_config(page_title="Image DEMO")
with open("designing.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.header("Chat with AI")
rad = st.sidebar.radio("Select", ['image', 'input'])
# Function to get response
if rad == 'image':
    def get_response(image, input_text):
        if input_text != "":
            response = model.generate_content(image, input_text)
        else:
            response = model.generate_content(image)
        return response.text

# File uploader
    uploaded_file = st.file_uploader("""# """, type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Button to generate response
    submit = st.button("Tell me about the image")
    if submit:
        response = get_response(image, "")  # Passing empty string for input_text
        st.subheader("The response is: ")
        st.write(response)
chat = model2.start_chat(history=[])
# for message in chat.history:
#   (f'**{message.role}**: {message.parts[0].text}'))
if rad == 'input':
    def get_response(question):
        response = model2.generate_content(question)
        return response.text

    inputs = st.text_input("Input: ", key="inputs")
    submit = st.button("Ask the question")
    if submit:
        response = get_response(inputs)
        st.subheader("The Answer is: ")
        st.write(response)
