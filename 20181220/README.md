# DAY4

* 딕셔너리를 사용했다.

* ```python
  ssafy = {
      "location": ["서울", "대전", "구미", "광주"],
      "language": {
          "python": {
              "python standard library": ["os", "random", "webbrowser"],
              "frameworks": {
                  "flask": "micro",
                  "django": "full-functioning"
              },
              "data_science": ["numpy", "pandas", "scipy", "sklearn"],
              "scrapying": ["requests", "bs4"],
          },
          "web" : ["HTML", "CSS"]
      },
      "classes": {
          "gm":  {
              "lecturer": "junwoo",
              "manager": "pro-gm",
              "class president": "엄윤주",
              "groups": {
                  "1조": ["강대현", "권민재", "서민수", "이규진"],
                  "2조": ["박재형", "서민호", "윤종원", "이지현"],
                  "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                  "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
              }
          },
          "gj": {
              "lecturer": "change",
              "manager": "pro-gj"
          }
      }
  }
  # 1번
  print(len(ssafy['location']))
  
  # 2번
  print('requests' in ssafy['language']['python']['python standard library'])
  
  # 3번
  print(ssafy['classes']['gm']['class president'])
  
  # 4번
  for lang in ssafy['language'].keys():
      print(lang)
  
  # 5번
  for name in ssafy['classes']['gj'].values():
      print(name)
  
  # 6번
  for name, ex in ssafy['language']['python']['frameworks'].items():
      print(f'{name}는 {ex}이다.')
  
  # 7번
  new_list = ssafy['classes']['gm']['groups']['4조']
  print(f'오늘의 당번은 {random.choice(new_list)}')
  
  ```

## Dictionary

* API를 활용하는데에 있어 가장많이  사용되는 자료형 웹을 하면서 계속 만나게 될 자료형
* key 와  value의 구조
* `key` 는 `string`, `integer`,`float`,`boolean`형이 가능하다 (`list` `dictionary`는 안된다)
*  `value`는 모든 자료형이 가능하다 `list` 와 `dictionary` 도가능하다.





