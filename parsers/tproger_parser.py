import requests
from bs4 import BeautifulSoup
from .dto import ContentDTO


MAIN_URL = 'https://tproger.ru/'
SUBURL = 'tag/python/'
ATTRS = {
    'q': 'python',
    'target_type': 'posts',
    'order': 'relevance'
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url=MAIN_URL, headers=HEADERS)


soup = BeautifulSoup(response.text, 'lxml')


def main():
    result = []
    all_content = soup.find_all(
        'article', attrs={'class': 'article'})
    for content in all_content:
        tmp = {}

        title = content.find('h2', attrs={'class': 'article__title'})
        description = content.find(
            'div', attrs={'class': 'article__container-excerpt'})
        link = title.find('a').get('href')
        img = content.find('img', attrs={'class': 'article__icon-image'})
        if img:
            tmp['img_link'] = img.get('src')
        else:
            tmp['img_link'] = None
        tmp['title'] = title.text.strip()
        tmp['description'] = description.text.strip()
        tmp['link'] = link
        tmp['site_name'] = 'tproger'

        result.append(tmp)
    return ContentDTO(result)


if __name__ == '__main__':
    main()
