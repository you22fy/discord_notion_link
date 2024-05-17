from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def summarize_text(text):
    client = OpenAI()
    OpenAI.api_key = OPENAI_API_KEY
    system_prompt = """
    あなたはwebサイト上からスクレイピングされたテキストを要約するAIです。
    これからユーザーがテキストを入力します。そのテキストを日本語で要約してください.
    要約する際には以下の点を考慮してください:
    - 要約の結果にはマークダウンを用いることができます。
    - 要約でできるだけテキストだけではなく、箇条書きやリストを用いてわかりやすく要約してください
    - 元の記事が構造的になっている場合、箇条書き等を用いてわかりやすく要約してください
    - 要約時は元のテキストの要点を押さえ、冗長な情報は省いてください
    - 要約の結果は日本語で出力してください
    - 要約の結果には、元のテキストのリンクを含めないでください
    - 元のテキストには記事の本文以外にも、広告やコメントなどが含まれることがありますが、要約の際には本文のみを要約してください
    """
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
        max_tokens=1000,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    sample_text = "Python is a programming language that lets you work quickly and integrate systems more effectively."
    summary = summarize_text("")
    print(summary)
