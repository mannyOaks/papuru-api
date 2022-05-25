from src.domain.manga import MangaList
from src.interface.usecase.manga_usecase import MangaUsecase
from src.interface.repository.manga_repository import MangaRepository


class MangaInteractor(MangaUsecase):
    manga_repository: MangaRepository

    def __init__(self, manga_repository: MangaRepository) -> None:
        self.manga_repository = manga_repository

    async def get_latest(self, page: int) -> MangaList:
        return await self.manga_repository.get_latest(page)
