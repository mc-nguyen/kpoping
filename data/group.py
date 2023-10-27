import requests
from bs4 import BeautifulSoup


class Group:
    def __init__(self, url):
        response = requests.get(url)

        # Parse the HTML content of the webpage.
        soup = BeautifulSoup(response.content, "html.parser")
        self.__title = soup.find("title").text

    def __str__(self):
        return self.__title
