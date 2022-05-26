from dataclasses import dataclass
from typing import List


@dataclass
class Source:
    id: str
    name: str
    thumbnail: str


@dataclass
class Sources(list[Source]):
    values: List[Source]
