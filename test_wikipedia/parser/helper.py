import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class TableParser:

    @staticmethod
    def get_table_by_class_name(url: str, class_name: str) -> Tag:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find(name="table", attrs={"class": class_name})
        return table
