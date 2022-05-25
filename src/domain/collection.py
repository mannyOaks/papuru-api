from typing import Generic, TypeVar

from attr import dataclass

T = TypeVar('T')


@dataclass(frozen=True)
class MappableCollection(Generic[T]):
    values: T

    def map(self, func) -> map:
        return map(func, self.values)
