from abc import ABCMeta, abstractmethod


class MangaDriver(metaclass=ABCMeta):
    @abstractmethod
    async def get_latest(self, page: int) -> dict:
        raise NotImplementedError
