import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

COT_PROMPT = """
Think step-by-step and give final answer clearly.

Question:
{question}
"""

while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    prompt = COT_PROMPT.format(question=user_input)
    response = model.invoke(prompt)

    print("\nAI:", response.content)
