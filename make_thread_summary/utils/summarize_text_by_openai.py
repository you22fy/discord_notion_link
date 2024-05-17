from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def summarize_text(text):
    client = OpenAI()
    OpenAI.api_key = OPENAI_API_KEY
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "あなたは与えられたテキストを要約するAIです。",
            },
            {
                "role": "system",
                "content": "これからユーザーがテキストを入力します。そのテキストを日本語で要約してください",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    sample_text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
    summary = summarize_text("")
    print(summary)
