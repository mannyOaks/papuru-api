from abc import ABCMeta, abstractmethod

from src.domain.category import Categories


class CategoryDriverAbstract(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self) -> Categories:
        raise NotImplementedError
