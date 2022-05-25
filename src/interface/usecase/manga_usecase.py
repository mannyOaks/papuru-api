from abc import ABCMeta, abstractmethod

from src.domain.manga import MangaList


class MangaUsecase(metaclass=ABCMeta):
    @abstractmethod
    async def get_latest(self, page: int) -> MangaList:
        raise NotImplementedError