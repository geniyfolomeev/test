from dataclasses import dataclass
from bs4.element import Tag


@dataclass
class Row:
    websites: str
    popularity: str
    front_end: str
    back_end: str
    database: str
    notes: str

    @property
    def float_popularity(self) -> float:
        return float("".join([i for i in self.popularity if i.isdigit()]))


@dataclass
class Table:
    rows: list[Row]

    @classmethod
    def build(cls, table: Tag):
        rows = []
        for table_row in table.find_all("tr"):
            cells = table_row.find_all("td")
            if cells:
                cell_data = []
                for cell in cells:
                    value = cell.get_text(strip=True)
                    cell_data.append(value)
                rows.append(Row(*cell_data))
        return cls(rows=rows)
