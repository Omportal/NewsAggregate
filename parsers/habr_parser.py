from bs4 import BeautifulSoup
import requests
from .dto import ContentDTO


MAIN_URL = 'https://habr.com/ru'
SUBURL = '/search/'
ATTRS = {
    'q': 'python',
    'target_type': 'posts',
    'order': 'relevance'
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


response = requests.get(url=MAIN_URL, headers=HEADERS)


soup = BeautifulSoup(response.text, 'lxml')


def main_habr():
    result = []

    all_content = soup.find_all(
        'article', attrs={'data-test-id': 'articles-list-item'})
    for content in all_content:
        tmp = {}

        title = content.find('h2', attrs={'data-test-id': 'articleTitle'})
        description = content.find(
            'div', attrs={'class': 'article-formatted-body'})
        link = MAIN_URL[:-3] + content.find(
            'a', attrs={'class': "tm-article-snippet__title-link"}).get('href')
        img = content.find('img', attrs={'data-test-id': 'articleLeadImage'})
        another_img = description.find('img')
        if img:
            tmp['img_link'] = img.get('src')
        elif another_img:
            tmp['img_link'] = another_img.get('src')
        else:
            tmp['img_link'] = None
        tmp['title'] = title.text
        tmp['description'] = description.text
        tmp['link'] = link
        tmp['site_name'] = 'habr'
        result.append(tmp)
    return ContentDTO(result)


if __name__ == '__main__':
    main_habr()
