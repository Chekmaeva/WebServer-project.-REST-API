# coding: utf-8
from requests import get
import JSON
 
print(get('http://localhost:8080/news').json())
print(get('http://localhost:8080/news/1').json())
print(get('http://localhost:8080/news/8').json()) # ошибка
# новости с id=8 нет в базе