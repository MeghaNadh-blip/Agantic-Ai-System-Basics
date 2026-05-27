# AI Concepts and Notes 🚀

# 1. Introduction to Artificial Intelligence (AI)

Artificial Intelligence (AI) is a technology that enables machines to mimic human intelligence and perform tasks such as learning, reasoning, problem-solving, and decision-making.

AI is mainly divided into four major fields:

* **ML** → Machine Learning
* **DL** → Deep Learning
* **CV** → Computer Vision
* **NLP** → Natural Language Processing

---

## Definitions

* AI mimics or simulates human intelligence.
* AI systems work based on data.
* “No data, no AI.”
* Deep Learning is often called the “brain” of modern AI.
* Computer Vision gives “eyes” to computers so they can analyze images and videos.
* NLP helps machines understand, process, and generate human language.
* Computers understand machine language in binary format (0s and 1s).

---

# 2. Traditional AI vs Generative AI

## Brief History of AI

* Alan Turing is considered one of the pioneers of AI.
* Neural Networks became highly popular after advancements in Deep Learning around 2012–2016.

---

## Traditional (Rule-Based) AI

Traditional AI mainly uses:

* If-else conditions
* Fixed rules
* Pattern matching
* Predefined logic

### Features

* Performs specific tasks
* Stores and processes data
* Follows programmed instructions
* Limited creativity

### Examples

* Calculator
* Spam filters
* Basic chatbots

---

## Generative AI

Generative AI is a type of AI that can create new content that does not already exist.

It can generate:

1. Images
2. Videos
3. Code
4. Audio
5. Text

### Popular Generative AI Tools

* OpenAI ChatGPT
* Google Gemini
* Anthropic Claude

### Advantages

* Saves time
* Improves productivity
* Assists developers and creators
* Automates repetitive tasks

---

# 3. Agentic AI

## What is Agentic AI?

Agentic AI is an advanced form of AI that can:

* Make decisions independently
* Perform tasks autonomously
* Plan actions step-by-step
* Interact with tools and environments

---

## Difference Between Normal AI and Agentic AI

| Normal AI                | Agentic AI                      |
| ------------------------ | ------------------------------- |
| Performs assigned tasks  | Makes decisions independently   |
| Needs human instructions | Can work autonomously           |
| Limited reasoning        | Advanced reasoning and planning |
| Single-step tasks        | Multi-step workflows            |

---

## Applications of Agentic AI

* Healthcare
* Finance
* Customer Service
* Education
* Robotics
* Smart Assistants

---

## AI Agent

An AI Agent is a software system that can:

* Observe
* Think
* Decide
* Act

without constant human intervention.

---

# 4. Generative AI Platforms & Python Packages

## Python Basics

### Installing Packages

```python id="yod37t"
pip install package_name
```

### Importing Packages

```python id="u8o6cc"
import package_name
```

---

## Generative AI Utilities

AI can process:

* Text
* Images
* Audio
* Videos
* Code

---

## Popular Platforms

* [Medium](https://medium.com?utm_source=chatgpt.com)
* [Hugging Face](https://huggingface.co?utm_source=chatgpt.com)
* [Kaggle](https://www.kaggle.com?utm_source=chatgpt.com)

---

# Transformers

Transformers are deep learning architectures used in modern AI models.

They help:

* Understand language
* Generate text
* Translate languages
* Build AI applications

### Popular Transformer Libraries

* Hugging Face Transformers
* LangChain Integrations

---

# Ollama

[Ollama](https://ollama.com?utm_source=chatgpt.com) is a platform that allows users to run Large Language Models (LLMs) locally on their computers.

It helps developers and AI enthusiasts use powerful AI models without depending completely on cloud services.

---

## Features of Ollama

* Offline AI usage
* Privacy-focused
* Supports multiple AI models
* Easy local deployment
* Fast model execution
* Works with Python and APIs

---

# Installation

## macOS

```bash id="k71d7y"
brew install ollama
```

## Windows

Download from:

[Ollama Download Page](https://ollama.com/download?utm_source=chatgpt.com)

## Linux

```bash id="8qvwvh"
curl -fsSL https://ollama.com/install.sh | sh
```

---

# Basic Ollama Commands

## Start Ollama Server

```bash id="8x8u8m"
ollama serve
```

## Download a Model

```bash id="cik2oq"
ollama pull llama3
```

## Run a Model

```bash id="4t2vzc"
ollama run llama3
```

---

## Run Other Models

### DeepSeek

```bash id="u0h9rt"
ollama run deepseek-r1
```

### Mistral

```bash id="ubjxvt"
ollama run mistral
```

### Gemma

```bash id="t1e3vi"
ollama run gemma
```

---

## List Installed Models

```bash id="4n2d6v"
ollama list
```

## Remove a Model

```bash id="bjq9e5"
ollama rm llama3
```

---

# Using Ollama with Python

## Install Python Package

```bash id="c10rwc"
pip install ollama
```

## Python Example

```python id="k5i7dv"
import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'Explain Artificial Intelligence'
        }
    ]
)

print(response['message']['content'])
```

---

## Popular Ollama Models

* llama3
* mistral
* deepseek-r1
* gemma
* codellama
* phi3

---

## Applications of Ollama

* AI Chatbots
* Coding Assistants
* AI Agents
* Offline AI Systems
* Educational Projects
* Research Applications
* Website AI Integration

---

## Advantages of Ollama

* Runs AI locally on your device
* Improves privacy and security
* No internet required after downloading models
* Easy integration with Python
* Beginner-friendly setup

---

# 5. Applications of Ollama & AI Agents

## Applications

AI agents can be used in:

* Business automation
* Education systems
* Chat interfaces
* Websites
* Healthcare
* Fitness and gym systems

---

## Agent Structure

An AI Agent generally requires:

* Goal
* Instructions
* Rules
* Memory
* Tools

---

# Agno Framework

Agno is a framework used to build AI agents and workflows.

It helps developers:

* Create autonomous agents
* Manage workflows
* Connect AI with tools and APIs

---

# Ollama as the “Brain”

Ollama can act as the “brain” of AI agents by running LLMs locally and providing intelligent responses.

---

# 6. Google AI Studio & LangChain

## Google AI Studio Steps

1. Open [Google AI Studio](https://aistudio.google.com?utm_source=chatgpt.com)
2. Generate an API Key
3. Connect it with Google Colab or Python projects

---

# LangChain

[LangChain](https://www.langchain.com?utm_source=chatgpt.com) is an open-source framework used for building applications powered by Large Language Models (LLMs).

---

## Features of LangChain

* Prompt management
* AI workflows
* Memory handling
* Tool integration
* Agent creation

---

## Python Imports

### Secure API Key Input

```python id="4v29c9"
import getpass
```

Used for securely entering API keys without displaying them on the screen.

---

### OS Module

```python id="m3u5xg"
import os
```

Used for:

* Environment variables
* File handling
* System operations

---

# 7. Gradio

## Gradio Library

[Gradio](https://gradio.app?utm_source=chatgpt.com) is used to create web interfaces for AI applications quickly.

---

## Features of Gradio

* Easy UI creation
* Works on mobile and desktop
* Supports multiple users
* Generates temporary shareable links
* Integrates easily with Python

---

## Example Use Cases

* Chatbots
* Image generators
* AI demos
* Voice assistants

---

# 8. Prompt Engineering Techniques

## Zero-Shot Prompting

Directly asking AI without providing examples.

### Example

```text id="tns3oh"
Explain Artificial Intelligence.
```

---

## Few-Shot Prompting

Providing a few examples before asking the AI to perform a task.

---

## Chain of Thought (CoT) Prompting

The AI thinks step-by-step before giving the final answer.

### Example

```text id="z9m8ct"
Solve the problem step-by-step.
```

---

## Role-Based Prompting

Assigning a role to AI.

### Example

```text id="uxfr1o"
Act as a Python expert.
```

---

# 9. Simple Chatbot using Groq

## Workflow

User → Groq API → AI Model → Response

---

## Steps to Build

1. Open [Groq](https://groq.com?utm_source=chatgpt.com)
2. Go to the Developers section
3. Generate an API Key
4. Use the API key in Python

---

## Features of Groq

* Fast inference speed
* Supports multiple AI models
* Easy API integration
* Useful for chatbot development

---

# 10. Future of AI 🌍

Artificial Intelligence is rapidly growing and transforming industries worldwide.

Future AI technologies may include:

* Fully autonomous AI agents
* Advanced robotics
* Personalized education systems
* AI-powered healthcare
* Smarter virtual assistants

AI is expected to become one of the most influential technologies of the future.

---

# Topics Covered

* AI Basics
* Machine Learning
* Deep Learning
* Generative AI
* Agentic AI
* LangChain
* Ollama
* Gradio
* Prompt Engineering
* Groq Chatbot Basics
* AI Agents
* Transformers

---

# Author

**Meghanadhsai Nalluri** ✨
