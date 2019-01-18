import requests
import os
import csv

name = []
result={}
code = []

# csv 읽어오기
with open('boxoffice.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        code.append(row['movie_code'])

with open('movie.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name.append(row['ko'])

naver_url='https://openapi.naver.com/v1/search/movie.json'
headers = {
    'X-Naver-Client-Id': os.getenv('NAVER_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}
for i in range(len(name)):
    naver_res = requests.get(naver_url,params={'query':name[i]},headers=headers)
    movie = naver_res.json()['items']
    result.update({code[i]:[movie[0]['image'],movie[0]['link'],movie[0]['userRating']]})

with open('movie_naver.csv','w',newline='',encoding='utf8') as f :
    writer = csv.DictWriter(f, fieldnames=['movie_code','thumb_url','link_url','user_rating'])
    writer.writeheader()
    for key,value in result.items():
        writer.writerow({'movie_code':key,'thumb_url':value[0],'link_url':value[1],'user_rating':value[2]})

