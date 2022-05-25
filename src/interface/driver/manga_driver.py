from abc import ABCMeta, abstractmethod


class MangaDriverContract(metaclass=ABCMeta):
    @abstractmethod
    async def get_latest(self, page: int) -> dict:
        raise NotImplementedError
