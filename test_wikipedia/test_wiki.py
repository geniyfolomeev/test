import pytest
from parser.models import Table, Row


def error_message(row: Row, threshold: float) -> str:
    # Можно также вывести в консоль, но поскольку pytest уже умеет выводить построчно, решил не делать
    return f"{row.websites} (Frontend:{row.front_end}|Backend:{row.back_end}) has {row.popularity} unique visitors " \
           f"per month. (Expected more than {threshold})"


@pytest.mark.parametrize(
    'threshold', [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
)
def test_check_popularity(
        wiki_table: Table,
        threshold: float,
):
    diff = []
    for row in wiki_table.rows:
        if row.float_popularity < threshold:
            diff.append(error_message(row, threshold))

    assert '\n'.join(diff) == ''

