from src.domain.category import Categories, Category
from src.interface.driver.category_driver import CategoryDriverAbstract
from src.interface.repository.category_repository import CategoryRepositoryAbstract


class CategoryRepository(CategoryRepositoryAbstract):
    category_driver: CategoryDriverAbstract

    def __init__(self, category_driver: CategoryDriverAbstract) -> None:
        self.category_driver = category_driver

    async def get_list(self) -> Categories:
        result = await self.category_driver.get_list()

        return Categories(
            values=[
                Category(
                    id=m['url'],
                    name=m['name'],
                )
                for m in result['categories']
            ]
        )
