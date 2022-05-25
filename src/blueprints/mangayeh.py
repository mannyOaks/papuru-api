from flask import Blueprint

from src.driver.mangayeh_driver import MangayehDriver
from src.interactor.manga_interactor import MangaInteractor
from src.repository.manga_repository import MangaRepository
from src.resource.manga_resource import MangaResource

bp = Blueprint('mangayeh', __name__, url_prefix='/mangayeh')

mangayeh_resource = MangaResource(
    manga_usecase=MangaInteractor(
        manga_repository=MangaRepository(manga_driver=MangayehDriver(), ),
    ),
)

bp.add_url_rule('/latest', view_func=mangayeh_resource.latest)
