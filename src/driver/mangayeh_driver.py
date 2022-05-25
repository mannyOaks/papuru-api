import aiohttp
from bs4 import BeautifulSoup
from src.interface.driver.manga_driver import MangaDriverAbstract
from src.util.format import str_format


class MangayehDriver(MangaDriverAbstract):
    BASE_URL = 'https://mangayeh.com'

    async def get_latest(self, page: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/category/latest') as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

        main_div = soup.find('div', class_='columns is-multiline')
        manga_div_list = main_div.find_all('div', class_='column is-half')

        return {
            'mangas':
                [
                    {
                        'url':
                            html.find('a')['href'],
                        'title':
                            str_format(html.find('div', class_='mtitle').contents[-1]),
                        'thumbnail':
                            html.find('img')['src'],
                        'categories':
                            [
                                span.string for span in
                                html.find_all('span', class_='tag is-light is-small')
                            ],
                    } for html in manga_div_list
                ]
        }
