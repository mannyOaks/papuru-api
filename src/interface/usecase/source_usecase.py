from abc import ABCMeta, abstractmethod

from src.domain.source import Sources


class SourceUsecaseContract(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self) -> Sources:
        raise NotImplementedError
