import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

COT_PROMPT = """
Think step-by-step and answer clearly.

Question:
{question}
"""

while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        break

    prompt = COT_PROMPT.format(question=user_input)

    response = model.invoke(prompt)

    print(response.content)
