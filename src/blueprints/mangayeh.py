from flask import Blueprint

from src.driver.mangayeh_driver import MangayehCategoryDriver, MangayehMangaDriver
from src.interactor.category_interactor import CategoryInteractor
from src.interactor.manga_interactor import MangaInteractor
from src.repository.category_repository import CategoryRepository
from src.repository.manga_repository import MangaRepository
from src.resource.category_resource import CategoryResource
from src.resource.manga_resource import MangaResource

bp = Blueprint('mangayeh', __name__, url_prefix='/mangayeh')

manga_resource = MangaResource(
    manga_usecase=MangaInteractor(
        manga_repository=MangaRepository(
            manga_driver=MangayehMangaDriver(),
        ),
    ),
)

category_resource = CategoryResource(
    category_usecase=CategoryInteractor(
        category_repository=CategoryRepository(
            category_driver=MangayehCategoryDriver(),
        )
    )
)

bp.add_url_rule('/', view_func=manga_resource.index)
bp.add_url_rule('/latest', view_func=manga_resource.latest)
bp.add_url_rule('/categories', view_func=category_resource.get_list)
