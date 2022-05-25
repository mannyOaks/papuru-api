from src.domain.source import SourceList
from src.interface.repository.category_repository import CategoryRepositoryAbstract
from src.interface.usecase.category_usecase import CategoryUsecaseAbstract


class CategoryInteractor(CategoryUsecaseAbstract):
    category_repository: CategoryRepositoryAbstract

    def __init__(self, category_repository: CategoryRepositoryAbstract) -> None:
        self.category_repository = category_repository

    async def get_list(self) -> SourceList:
        return await self.category_repository.get_list()
