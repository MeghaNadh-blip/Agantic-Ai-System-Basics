import getpass
import gradio as gr
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# API Key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

# Load Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Chat Function
def chat_with_gemini(message, history):
    response = model.invoke(message)
    return response.content

# Gradio Interface
demo = gr.ChatInterface(
    fn=chat_with_gemini,
    title="Simple Gemini Chatbot"
)

# Launch App
demo.launch(share=True)
