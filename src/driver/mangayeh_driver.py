from typing import Any, Dict, List

import aiohttp
from bs4 import BeautifulSoup, ResultSet
from src.domain.category import Categories
from src.interface.driver.category_driver import CategoryDriverAbstract
from src.interface.driver.manga_driver import MangaDriverAbstract
from src.util.format import str_format


def soup_to_dict(mangaset: ResultSet) -> Dict[str, List[Dict[str, Any]]]:
    return {
        'mangas': [
            {
                'url': m.find('a')['href'],
                'title': str_format(m.find('div', class_='mtitle').contents[-1]),
                'thumbnail': m.find('img')['src'],
                'categories': [
                    span.string
                    for span in m.find_all('span', class_='tag is-light is-small')
                ],
            }
            for m in mangaset
        ]
    }


class MangayehMangaDriver(MangaDriverAbstract):
    BASE_URL = 'https://mangayeh.com'

    async def get_list(self, page: int) -> dict:
        params = {'page': page} if page is not None else {}

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'{self.BASE_URL}/category/all',
                params=params,
            ) as response:
                print(response.url)
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

        main_div = soup.find('div', class_='columns is-multiline')
        manga_div_list = main_div.find_all('div', class_='column is-half')

        return soup_to_dict(manga_div_list)

    async def get_latest(self, page: int) -> dict:
        params = {'page': page} if page is not None else {}

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'{self.BASE_URL}/category/latest',
                params=params,
            ) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

        main_div = soup.find('div', class_='columns is-multiline')
        manga_div_list = main_div.find_all('div', class_='column is-half')

        return soup_to_dict(manga_div_list)


class MangayehCategoryDriver(CategoryDriverAbstract):
    BASE_URL = 'https://mangayeh.com'

    async def get_list(self) -> Categories:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

        categories_div = soup.find(
            'div', class_='columns is-multiline is-mobile pl-1 pr-1'
        )
        category_div_list = categories_div.find_all('a')

        return {
            'categories': [
                {'url': c['href'], 'name': c.string} for c in category_div_list
            ]
        }
