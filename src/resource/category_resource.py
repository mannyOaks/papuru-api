import asyncio

from flask import jsonify, request as req

from src.domain.category import Categories
from src.interface.usecase.category_usecase import CategoryUsecaseAbstract


class CategoryResource:
    category_usecase: CategoryUsecaseAbstract

    def __init__(self, category_usecase: CategoryUsecaseAbstract) -> None:
        self.category_usecase = category_usecase

    def get_list(self):
        categories: Categories = asyncio.run(self.category_usecase.get_list())
        return jsonify(
            {
                'results': [
                    {'id': category.id, 'name': category.name}
                    for category in categories.values
                ]
            }
        )
