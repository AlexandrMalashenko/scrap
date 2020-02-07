import requests
from bs4 import BeautifulSoup as BS

from .models import Results

if __name__ == "__main__":
    search = input()
    site = input()
    session = requests.Session()
    url = 'https://yandex.ru/search/?lr=119392&text={}'.format(search)
    req = session.get(url)
    div = None
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        div = bsObj.find_all('li', attrs={'class': 'serp-item'})

    row_number = 1
    for row in div:
        title = row.find('h2')
        href = title.a['href']
        if site in href:
            print(href, row_number)
        row_number += 1
