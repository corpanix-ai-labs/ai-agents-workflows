# 🚀 LinkedIn Post Generator via OpenAI SDK

> **AI-powered LinkedIn post generator that creates engaging, viral-worthy content tailored to your topics**

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-purple.svg)](https://openai.com/)

## 📖 Overview

This project leverages OpenAI's GPT-4o model to automatically generate professional, engaging LinkedIn posts. Simply provide a topic, and the AI will craft a compelling post optimized for LinkedIn's platform, complete with proper formatting and engagement strategies.

## ✨ Features

- 🤖 **AI-Powered Content**: Uses OpenAI's GPT-4o for intelligent post generation
- �� **Topic-Focused**: Generates content specifically tailored to your input topic
- 📱 **LinkedIn-Optimized**: Content structured for maximum engagement on LinkedIn
- 🚀 **Viral Potential**: Designed to create shareable, engaging content
- ⚡ **Fast & Simple**: Get professional posts in seconds with minimal input
- 🔒 **Secure**: Uses environment variables for API key management

## 🛠️ Prerequisites

- Python 3.13 or higher
- OpenAI API key
- Internet connection

## 🛠️ OpenAI SDK
```bash
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
```

## �� Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd linkedin-post-via-openai-api
```

### 2. Install Dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or using `pip`:
```bash
pip install python-dotenv requests
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

**Get your OpenAI API key from:** [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 4. Run the Application

```bash
# Using uv
uv run python main.py

# Using python directly
python main.py
```

### 5. Generate Your Post

1. Enter your LinkedIn post topic when prompted
2. Wait for the AI to generate your content
3. Copy the generated post to LinkedIn
