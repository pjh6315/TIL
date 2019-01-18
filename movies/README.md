### 1. 영화진흥위원회 오픈 API (주간/ 주말 박스오피스 데이터)



#### 활용한 API

* kobis_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
* `    kobis_res = requests.get(kobis_url, params={'key': os.getenv('KOBIS_KEY'), 'targetDt': day[i], 'weekGb': '0'})`    
* key: 발급받은 key 값 입력
* targetDt : 조회할 날짜 입력
* weekGb : 0 으로 주간 데이터 선택
* 

### 2. 영화진흥위원회 오픈 API (영화상세정보)

* url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
* `    res = requests.get(url, params={'key': os.getenv('KOBIS_KEY'),'movieCd':code[i]})`    
* key : key 값입력
* movieCd : 영화코드값 입력



### 3. 네이버 영화검색 API

* https://openapi.naver.com/v1/search/movie.json
* query



### 4. 영화 포스터 이미지 저장

* ```PYTHON
  # image 저장하기
      image_url = img_url[i]
      image_file = requests.get(image_url)
      with open('./images/'+ code[i] + '.jpg','wb') as f:
          f.write(image_file.content)
  ```
