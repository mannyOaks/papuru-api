from abc import ABCMeta, abstractmethod

from app.domain.manga import MangaList


class MangaRepositoryContract(metaclass=ABCMeta):
    @abstractmethod
    async def get_latest(self, page: int) -> MangaList:
        raise NotImplementedError