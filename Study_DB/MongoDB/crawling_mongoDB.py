import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    rank_tag = tr.select_one('img')
    text_tag = tr.select_one('td.title > div > a')
    rating_tag = tr.select_one('td.point')

    if text_tag != None:
        rank = rank_tag['alt']
        title = text_tag.text
        rating = rating_tag.text
        doc = {'rank': rank,
               'title': title,
               'rating': rating}

        db.movies.insert_one(doc)