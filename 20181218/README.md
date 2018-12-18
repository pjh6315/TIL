# 20181218 DAY02



### Git 설정 

* `git config --global user.name '이름'`
* `git config --global user.email '이메일'`

*  `git init` : Git 초기화, git 으로 관리하겠다!
* `git remote add origin 주소`: 원격저장소 등록
  * `git remote set-url origin 주소` : 원격저장소 수정

### Git Commit & Push

* `git status` : 현재 폴더의 git의 상태
* `git add . ` :현재폴더의 변경사항들을 commit하기 위해 준비
* `git commit -m 'day 02 입니다'` : commit, 변경 사항 저장 메세지는 자유롭게 작성가능
* `git push -u origin master` : remote로 등록된 원격저장소(remote repository)
  * 이후에는 `git push`  만 입력해도 동작합니다.



### Markdown 으로 기록

*  typora vs VSCode
* Github student developer pack



###  파일명변경

1. `  os.chdir(r'폴더주소')`
2. ` os.listdir('.')`:  현재  working directory의 파일 목록 리스트로
3. `os.rename('바꾸려는 이름','바꿀이름')` 



###  크롤링

###### 네이버검색순위

```python
import requests
import bs4

response = requests.get('https://www.naver.com/').text

soup = bs4.BeautifulSoup(response,'html.parser')

# result = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_k')
# result = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_r')

result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')

for item in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one('.ah_k').text
    print(f'{rank} / {keyword}')
```

###### 멜론 우회

```python
import requests
import bs4

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.melon.com/chart/index.htm',headers=headers).text

print(response)


```

