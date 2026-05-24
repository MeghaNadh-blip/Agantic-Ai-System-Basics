import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# API Key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter Google API Key: ")

# Load Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Task Decomposition Prompt
AGENT_PROMPT = """
You are an advanced AI Agent.

For every user request, follow these steps:

1. Understand the task
2. Decompose the task into smaller subtasks
3. Explain each subtask
4. Think step-by-step
5. Solve systematically
6. Provide the final answer

Use this format:

Task Understanding:
...

Task Decomposition:
1.
2.
3.

Step-by-Step Reasoning:
...

Final Answer:
...

User Request:
{question}
"""

# Chat Loop
while True:
    user_input = input("YOU: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    prompt = AGENT_PROMPT.format(question=user_input)
    response = model.invoke(prompt)

    print("\nAI:", response.content)
