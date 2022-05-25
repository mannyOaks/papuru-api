from src.domain.manga import MangaList
from src.interface.repository.manga_repository import MangaRepositoryAbstract
from src.interface.usecase.manga_usecase import MangaUsecaseAbstract


class MangaInteractor(MangaUsecaseAbstract):
    manga_repository: MangaRepositoryAbstract

    def __init__(self, manga_repository: MangaRepositoryAbstract) -> None:
        self.manga_repository = manga_repository

    async def get_list(self, page: int) -> MangaList:
        return await self.manga_repository.get_list(page)

    async def get_latest(self, page: int) -> MangaList:
        return await self.manga_repository.get_latest(page)
