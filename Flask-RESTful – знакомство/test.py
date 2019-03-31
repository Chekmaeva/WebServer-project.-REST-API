# coding: utf-8
# test.py

import JSON
from requests import get, post 

print(delete('http://localhost:8080/news/8').json())   # ошибка
# новости с id=8 нет в базе
print(delete('http://localhost:8080/news/3').json())