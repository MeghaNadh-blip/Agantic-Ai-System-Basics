import getpass
import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = getpass.getpass("Enter Groq API Key: ")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_retries=2,
)

while True:
    user_input = input("YOU: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye")
        break

    response = llm.invoke(user_input)
    print("\nAI:", response.content)
