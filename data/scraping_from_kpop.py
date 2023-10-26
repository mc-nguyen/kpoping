import re
import requests
from bs4 import BeautifulSoup


class ScrapingFromKPop:
    def __init__(self):
        self.__url = "https://kprofiles.com"

        response = requests.get(self.__url)

        # Parse the HTML content of the webpage.
        self.__soup = BeautifulSoup(response.content, "html.parser")

        # Extract the title of the webpage.
        self.__list = self.__soup.find_all("a", href=re.compile("-profile/"))

    def __str__(self):
        return str(self.__list)
