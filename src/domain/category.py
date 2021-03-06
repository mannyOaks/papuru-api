from dataclasses import dataclass
from typing import List

from src.domain.collection import MappableCollection


@dataclass(frozen=True)
class Category:
    id: str
    name: str


@dataclass(frozen=True)
class Categories(MappableCollection[Category]):
    values: List[Category]
