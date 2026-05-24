import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

REACT_PROMPT = """
Thought:
Action:
Observation:
Final Answer:

Question:
{question}
"""

while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    prompt = REACT_PROMPT.format(question=user_input)
    response = model.invoke(prompt)

    print("\nAI:", response.content)
