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
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    ogp_link = soup.find("meta", property="og:image")["content"]
    text = soup.get_text()
    return (title, ogp_link, text)


if __name__ == "__main__":
    url = "https://qiita.com/Yu_unI1/items/af76bcf4ca655239ed6d"
    title, ogp, text = get_content_by_url(url)
    print(title)
    print(ogp)
    print(text)
