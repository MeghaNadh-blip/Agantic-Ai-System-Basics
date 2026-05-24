import getpass
import os
import gradio as gr
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = getpass.getpass("Enter Groq API Key: ")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_retries=2,
)

def chatbot(user_input, history):
    response = llm.invoke(user_input)
    return response.content

demo = gr.ChatInterface(
    fn=chatbot,
    title="Groq AI Chatbot",
    description="Chat with AI using Groq + Gradio"
)

demo.launch(share=True)
