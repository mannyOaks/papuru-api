from typing import Collection, List
from dataclasses import dataclass

from .collection import MappableCollection

from .category import Category


@dataclass(frozen=True)
class Manga:
    id: str
    title: str
    thumbnail: str
    categories: List[Category]


@dataclass(frozen=True)
class MangaList(MappableCollection[Manga]):
    values: List[Manga]
