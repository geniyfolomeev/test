import pytest
from parser.models import Table
from parser.helper import TableParser


@pytest.fixture(scope="session")
def wiki_table() -> Table:
    # Сделал сессионную фикстуру чтобы расшарить таблицу между тестами
    html_table = TableParser.get_table_by_class_name(
        url="https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites",
        class_name="wikitable",
    )
    table = Table.build(html_table)
    return table
