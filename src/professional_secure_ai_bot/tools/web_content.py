import requests
from langchain.agents import tool


@tool
def get_web_content(url: str) -> str:
    """This tool makes a request to an internet resource and returns the content.
    :return: HTML code of a webpage"""

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Request failed with status code: {response.status_code}"
