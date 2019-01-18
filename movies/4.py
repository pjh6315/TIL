import requests
import os
import csv

img_url = []
code = []
with open('movie_naver.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        img_url.append(row['thumb_url'])
        code.append(row['movie_code'])

naver_url='https://openapi.naver.com/v1/search/movie.json'
headers = {
    'X-Naver-Client-Id': os.getenv('NAVER_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}
for i in range(len(img_url)):
    
    # image 저장하기
    image_url = img_url[i]
    image_file = requests.get(image_url)
    with open('./images/'+ code[i] + '.jpg','wb') as f:
        f.write(image_file.content)

