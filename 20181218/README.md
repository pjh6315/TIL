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



### 파일조작





###  파일명변경

1. `  os.chdir(r'폴더주소')`
2. ` os.listdir('.')`:  현재  working directory의 파일 목록 리스트로
3. `os.rename('바꾸려는 이름','바꿀이름')` 

