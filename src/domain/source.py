from dataclasses import dataclass
from typing import List

from src.domain.collection import MappableCollection


@dataclass
class Source:
    id: str
    name: str
    thumbnail: str


@dataclass
class Sources(list[Source]):
    values: List[Source]
