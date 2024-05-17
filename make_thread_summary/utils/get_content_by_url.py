import requests
from bs4 import BeautifulSoup


def get_content_by_url(url: str):
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

        title = soup.title if soup.title else ""
        ogp_link = (
            soup.find("meta", property="og:image")["content"] if soup.title else ""
        )

        text = soup.get_text()
        return (
            title,
            ogp_link,
            text,
        )

    except Exception as e:
        return (f"Error in get_content_by_url: {e}", "", "")


if __name__ == "__main__":
    url = "https://platform.openai.com/docs/api-reference/chat/object"
    title, ogp, text = get_content_by_url(url)
    print(title)
    print(ogp)
    print(text)
