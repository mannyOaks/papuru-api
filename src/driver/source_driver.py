from src.domain.source import Source
from src.interface.driver.source_driver import SourceDriverContract

SOURCES = [
    Source(
        id='https://mangayeh.com/',
        name='Mangayeh',
        thumbnail='mangayeh_ic_64.png',
    ),
]


class SourceDriver(SourceDriverContract):
    async def get_list(self) -> dict:

        return {
            'sources': [
                {
                    'id': s.id,
                    'name': s.name,
                    'thumbnail': s.thumbnail,
                }
                for s in SOURCES
            ]
        }
