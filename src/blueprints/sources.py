from flask import Blueprint
from src.driver.source_driver import SourceDriver
from src.interactor.source_interactor import SourceInteractor
from src.repository.source_repository import SourceRepository

from src.resource.source_resource import SourceResource


bp = Blueprint('sources', __name__, url_prefix='/sources')

source_resource = SourceResource(
    source_usecase=SourceInteractor(
        source_repository=SourceRepository(
            source_driver=SourceDriver(),
        ),
    ),
)

bp.add_url_rule('/', view_func=source_resource.index)
