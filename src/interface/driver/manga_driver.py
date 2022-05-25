from abc import ABCMeta, abstractmethod


class MangaDriverAbstract(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self, page: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def get_latest(self, page: int) -> dict:
        raise NotImplementedError
