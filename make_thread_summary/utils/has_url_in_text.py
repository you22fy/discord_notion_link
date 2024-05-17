import re


def has_url_in_text(text: str) -> str | None:
    url_pattern = r"(https?://\S+)"
    match = re.search(url_pattern, text)
    if match:
        return match.group(0)
    else:
        return None


if __name__ == "__main__":
    text = "Check out this cool website: https://www.example.com/hoge/fuga This is a cool website!"
    url = has_url_in_text(text)
    print(url)  # Output: https://www.example.com
