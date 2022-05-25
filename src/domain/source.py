from dataclasses import dataclass
from typing import List

from src.domain.collection import MappableCollection


@dataclass
class Source:
    id: str
    name: str
    url: str
    thumbnail: str


@dataclass
class SourceList(MappableCollection[Source]):
    values: List[Source]
