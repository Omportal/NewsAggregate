from bs4 import BeautifulSoup
import requests
import pprint

MAIN_URL = 'https://habr.com/ru'
SUBURL = '/search/'
ATTRS = {
    'q':'python',
    'target_type': 'posts',
    'order':'relevance'
}
HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

response = requests.get(url=MAIN_URL + SUBURL, headers=HEADERS, params=ATTRS)


soup = BeautifulSoup(response.text, 'lxml')


result = []
all_content = soup.find_all('article', attrs={'data-test-id':'articles-list-item'})
for content in all_content:
    tmp = {}

    title = content.find('h2', attrs={'data-test-id':'articleTitle'}) 
    descriprtion = content.find('div', attrs={'class':'article-formatted-body'})
    link = MAIN_URL[:-3] + content.find('a', attrs={'class':"tm-article-snippet__title-link"}).get('href')
    img = content.find('img', attrs={'data-test-id':'articleLeadImage'})
    another_img = descriprtion.find('img')
    if img:
        tmp['img_link'] = img.get('src')
    if another_img:
        tmp['img_link'] = another_img.get('src')

    tmp['title'] = title.text
    tmp['descriprtion'] = descriprtion.text
    tmp['link'] = link
    

    result.append(tmp)


    