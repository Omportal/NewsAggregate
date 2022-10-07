'https://itproger.com/search/python'

import pprint
import requests
from bs4 import BeautifulSoup


MAIN_URL = 'https://itproger.com/'
SUBURL = 'search/python'
ATTRS = {
    'q': 'python',
    'target_type': 'posts',
    'order': 'relevance'
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url=MAIN_URL + SUBURL, headers=HEADERS)


soup = BeautifulSoup(response.text, 'lxml')


result = []
all_content = soup.find_all(
    'div', attrs={'class': 'article'})
for content in all_content:
    tmp = {}

    link = content.find('a')
    title = link
    img = content.find('img')
    description = img.findNext('span').findNext('span')
    tmp['img_link'] = MAIN_URL + img.get('src')
    tmp['title'] = title.text.strip()
    tmp['description'] = description.text.strip()
    tmp['link'] = MAIN_URL + link.get('href')

    result.append(tmp)

pprint.pprint(result)
