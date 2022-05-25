from abc import ABCMeta, abstractmethod

from src.domain.manga import MangaList


class MangaUsecaseAbstract(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self, page: int) -> MangaList:
        raise NotImplementedError

    @abstractmethod
    async def get_latest(self, page: int) -> MangaList:
        raise NotImplementedError
