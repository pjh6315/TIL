import requests
import os
import csv

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
code = []
result = {}

# csv 읽어오기
with open('boxoffice.csv','r',newline='',encoding='utf8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        code.append(row['movie_code'])
# 코드의 길이 만큼 반복문
for i in range(len(code)):
    #  genre 와 actor 미리 만들기
    genres = [] 
    actors = []
    res = requests.get(url, params={'key': os.getenv('KOBIS_KEY'),'movieCd':code[i]})
    movie = res.json()['movieInfoResult']['movieInfo']

    for genre in movie['genres']:
        genres.append(genre['genreNm'])
    for actor in movie['actors']:
        actors.append(actor['peopleNm'])

    temp_genre = '/'.join(genres)

    if len(actors) < 3 :
        actors.append(' ')
        actors.append(' ')
        actors.append(' ')
    # result 딕셔너리에 값들 업데이트
    result.update({code[i]:[movie['movieNm'],movie['movieNmEn'],movie['movieNmOg'],movie['prdtYear'],movie['directors'][0]['peopleNm'],movie['audits'][0]['watchGradeNm'],temp_genre,actors[0],actors[1],actors[2]]})


    # csv에 쓰기
with open('movie.csv','w',newline='',encoding='utf8') as f :
    writer = csv.DictWriter(f, fieldnames=['movie_code','ko','en','og','prdt','genres','directors','watch_grade','actor1','actor2','actor3'])
    writer.writeheader()
    for key,value in result.items():
        writer.writerow({'movie_code':key,'ko':value[0],'en':value[1],'og':value[2],'prdt':value[3],'genres':value[6],'directors':value[4],'watch_grade':value[5],'actor1':value[7],'actor2':value[8],'actor3':value[9]})





