from abc import ABCMeta, abstractmethod


class SourceDriverContract(metaclass=ABCMeta):
    @abstractmethod
    async def get_list(self) -> dict:
        raise NotImplementedError
