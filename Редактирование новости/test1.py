# coding: utf-8
# test.py

import JSON
from requests import get, post
 
print(post('http://localhost:8080/news').json())
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок'}).json())
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1}).json())