import asyncio

from flask import jsonify, url_for
from src.domain.source import Sources
from src.interface.usecase.source_usecase import SourceUsecaseContract


class SourceResource:
    source_usecase: SourceUsecaseContract

    def __init__(self, source_usecase) -> None:
        self.source_usecase = source_usecase

    def index(self):
        sources: Sources = asyncio.run(self.source_usecase.get_list())
        return jsonify(
            {
                'items': [
                    {
                        'id': s.id,
                        'name': s.name,
                        'thumbnail': url_for(
                            'static',
                            filename=f'images/sources/{s.thumbnail}',
                        ),
                    }
                    for s in sources.values
                ]
            }
        )
