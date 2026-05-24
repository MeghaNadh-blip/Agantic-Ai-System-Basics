import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# API Key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

# Load Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# ReAct Prompt
REACT_PROMPT = """
You are an intelligent AI Agent using the ReAct framework.

Follow this format:

Thought:
Action:
Observation:
Final Answer:

Question:
{question}
"""

# Chat Loop
while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    prompt = REACT_PROMPT.format(question=user_input)

    response = model.invoke(prompt)

    print("\nAI:", response.content)
