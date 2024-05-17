import requests
from bs4 import BeautifulSoup


def get_content_by_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    return text


if __name__ == "__main__":
    url = "https://qiita.com/Yu_unI1/items/af76bcf4ca655239ed6d"
    content = get_content_by_url(url)
    print(content)
