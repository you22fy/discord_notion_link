import os
import requests

from dotenv import load_dotenv
import asyncio

load_dotenv()
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")


async def insert_notion(title: str, url: str, ogp_url: str | None, body: str) -> None:
    """
    [title]と[url]と[body]を引数として受け取り、それをNotion API経由でNotionのDBに追加する関数
    """
    base_url = "https://api.notion.com/v1/pages"
    headers = {
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
    }
    json_data = {
        "parent": {
            "database_id": NOTION_DB_ID,
        },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {"content": title},
                    },
                ],
            },
            "link": {
                "url": url,
            },
        },
        "children": [
            {
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {
                        "url": (
                            ogp_url
                            if ogp_url
                            else "https://stat.ameba.jp/user_images/55/19/10063987699.gif"
                        ),
                    },
                },
            },
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "要約",
                            },
                        }
                    ]
                },
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "text": {
                                "content": body,
                            },
                        },
                    ],
                },
            },
        ],
    }
    r = requests.post(
        base_url,
        headers=headers,
        json=json_data,
    )
    return


async def main():
    await insert_notion(
        "pythonで追加",
        "https://example.com",
        "https://stat.ameba.jp/user_images/55/19/10063987699.gif",
        "body",
    )


if __name__ == "__main__":
    asyncio.run(main())
