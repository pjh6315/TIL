import requests
import os
import csv

kobis_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

# # 1번

day = ['20190113','20190106','20181230','20181223','20181216','20181209','20181202','20181125','20181118','20181111']


movie_dict = {}

for i in range(len(day)-1,-1,-1):
    kobis_res = requests.get(kobis_url, params={'key': os.getenv('KOBIS_KEY'), 'targetDt': day[i], 'weekGb': '0'})

    for movie in kobis_res.json()['boxOfficeResult']["weeklyBoxOfficeList"]:
        movie_dict.update({movie['movieCd']:[movie['movieNm'],movie['audiAcc'],day[i]]})


with open('boxoffice.csv','w',newline='',encoding='utf8') as f :
    writer = csv.DictWriter(f, fieldnames=['movie_code','title','audience','recorded_at'])
    writer.writeheader()
    for key,value in movie_dict.items():
        writer.writerow({'movie_code':key,'title':value[0],'audience':value[1],'recorded_at':value[2]})





