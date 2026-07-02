from typing import Any


class Dataset:

    def __init__(self, values: list[Any]):
        self.values = values

    def get(self, index: int) -> Any:
        return self.values[index]

    def size(self) -> int:
        return len(self.values)

    def is_empty(self) -> bool:
        return len(self.values) == 0