import asyncio

from flask import jsonify

from src.domain.manga import Manga, MangaList
from src.interface.usecase.manga_usecase import MangaUsecase


class MangaResource:
    manga_usecase: MangaUsecase

    def __init__(self, manga_usecase: MangaUsecase) -> None:
        self.manga_usecase = manga_usecase

    def latest(self):
        latest_manga: MangaList = asyncio.run(self.manga_usecase.get_latest(0))
        return jsonify(manga_response(latest_manga))


def manga_response(manga_list: MangaList) -> dict:
    return {
        "results": [{
            "id": manga.id,
            "body": manga.body
        } for manga in manga_list.values]
    }