import requests
import os
import csv

# 영진위
kobis_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
kobis_res = requests.get(kobis_url,params={'key':os.getenv('KOBIS_KEY') , 'targetDt': '20190113' ,'weekGb':'0'})




naver_url='https://openapi.naver.com/v1/search/movie.json'
headers = {
    'X-Naver-Client-Id': os.getenv('NAVER_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}
naver_res = requests.get(naver_url,params={'query':'말모이'},headers=headers)


data = {
    'title':'말모이',
    'director':'엄유나'
}

# csv 저장하기
with open('test.csv','w',newline='',encoding='utf8') as f :
    writer = csv.DictWriter(f, fieldnames=['title','director'])
    writer.writeheader()
    writer.writerow(data)

# csv 읽어오기
with open('test.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['title'],row['director'])

# image 저장하기
image_url = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167699_P40_175859.jpg'
image_file = requests.get(image_url)
with open('test.jpg','wb') as f:
    f.write(image_file.content)