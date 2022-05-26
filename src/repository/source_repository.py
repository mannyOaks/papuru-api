from src.domain.source import Source, Sources
from src.interface.driver.source_driver import SourceDriverContract
from src.interface.repository.source_repository import SourceRepositoryContract


class SourceRepository(SourceRepositoryContract):
    source_driver: SourceDriverContract

    def __init__(self, source_driver: SourceDriverContract) -> None:
        self.source_driver = source_driver

    async def get_list(self) -> Sources:
        res = await self.source_driver.get_list()
        return Sources(
            values=[
                Source(
                    id=s['id'],
                    name=s['name'],
                    thumbnail=s['thumbnail'],
                )
                for s in res['sources']
            ]
        )
