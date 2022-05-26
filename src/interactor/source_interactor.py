from src.domain.manga import MangaList
from src.interface.repository.source_repository import SourceRepositoryContract
from src.interface.usecase.source_usecase import SourceUsecaseContract


class SourceInteractor(SourceUsecaseContract):
    source_repository: SourceRepositoryContract

    def __init__(self, source_repository: SourceRepositoryContract) -> None:
        self.source_repository = source_repository

    async def get_list(self) -> MangaList:
        return await self.source_repository.get_list()
