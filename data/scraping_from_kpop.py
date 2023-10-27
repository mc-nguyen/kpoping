import requests
from bs4 import BeautifulSoup


class ScrapingFromKPop:
    def __init__(self):
        self.__url = "https://kprofiles.com"
        response = requests.get(self.__url)

        # Parse the HTML content of the webpage.
        soup = BeautifulSoup(response.content, "html.parser")

        self.__links = {}
        soup_links = soup.find_all(attrs={
            "class": "textwidget"
        })
        for soup_link in soup_links:
            find_tags = soup_link.find_all('a')
            if len(find_tags) != 0:
                for tag in find_tags:
                    self.__links[tag.text] = tag.get('href')

    def get_all_profile_category(self):
        return self.__links.keys()

    def get_link(self, category):
        return self.__links[category]

    def __str__(self):
        return str(self.__links)
