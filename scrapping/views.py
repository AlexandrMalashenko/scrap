from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as BS

from .models import Results


def search(request):
    data = JSONParser().parse(request)
    arg1 = data['arg1']
    arg2 = str(data['arg2'])
    session = requests.Session()
    url = 'https://yandex.ru/search/?lr=119392&text={}'.format(arg1)
    req = session.get(url)
    div = None
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        div = bsObj.find_all('li', attrs={'class': 'serp-item'})

    row_number = 1
    for row in div:
        if row_number < 4:
            title = row.find('h2')
            href = title.a['href']
            if arg2 in href:
                result = Results(query=arg1, row_number=row_number)
                result.save()
            row_number += 1
    response = HttpResponse(content_type='application/json')
    response.content = 'ok'
    return response
