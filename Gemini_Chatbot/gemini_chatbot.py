import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# API Key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

# Load Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Chat Loop
while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    response = model.invoke(user_input)

    print("\nAI:", response.content)
