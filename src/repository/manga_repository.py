from typing import Any, Dict, List
from src.domain.category import Category
from src.domain.manga import Manga, MangaList
from src.interface.driver.manga_driver import MangaDriverAbstract
from src.interface.repository.manga_repository import MangaRepositoryAbstract


class MangaRepository(MangaRepositoryAbstract):
    manga_driver: MangaDriverAbstract

    def __init__(self, manga_driver: MangaDriverAbstract) -> None:
        self.manga_driver = manga_driver

    async def get_list(self, page: int) -> MangaList:
        result = await self.manga_driver.get_list(page)
        return mangalist_from_dictlist(result['mangas'])

    async def get_latest(self, page: int) -> MangaList:
        result = await self.manga_driver.get_latest(page)
        return mangalist_from_dictlist(result['mangas'])


def mangalist_from_dictlist(mangas: List[Dict[str, Any]]) -> MangaList:
    return MangaList(
        values=[
            Manga(
                id=m['url'],
                title=m['title'],
                thumbnail=m['thumbnail'],
                categories=[Category(id=c.lower(), name=c) for c in m['categories']],
            )
            for m in mangas
        ]
    )
