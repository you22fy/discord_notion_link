import requests
from bs4 import BeautifulSoup
import asyncio


async def get_content_by_url(url: str):
    """
    urlを受け取ってそのページのタイトル、OGP画像、テキストを取得する
    Parameters
    ----------
    url : str
        取得したいページのURL
    Returns
    -------
    tuple
        ページのタイトル, OGP画像のURL, ページのテキスト
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup is None:
            raise Exception("soup is None. Failed to parse HTML.")

        text = soup.get_text()
        if len(text) < 100:
            raise Exception("text is too short. Probably not a valid article.")

        title = soup.title.string if soup.title else ""
        ogp_link = (
            soup.find("meta", property="og:image")["content"]
            if soup.find("meta", property="og:image")
            else ""
        )

        return (
            title,
            ogp_link,
            text,
        )

    except Exception as e:
        raise Exception(f"Error in get_content_by_url: {e}")


async def main():
    url = "https://ai.google.dev/competition?hl=ja"
    title, ogp, text = await get_content_by_url(url)
    print(title)
    print(ogp)
    print(text)


if __name__ == "__main__":
    asyncio.run(main())
