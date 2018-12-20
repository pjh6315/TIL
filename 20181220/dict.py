#딕셔너리 만들기

lunch = {
    '중국집' : '02-123-123',
    '양식집' : '054-123-123',
    '한식집' : '053-444-2222'
}

dinner = dict(중국집='02-323-3232')

#딕셔너리에 내용 추가하기
lunch['분식집'] = '053-123-123'

#딕셔너리 내용 가져오기
print(lunch['중국집'])  # -> 전화번호 

print(lunch)

idol = {
    'bts' : {
        '지민' : 24,
        'RM' : 25
    }
}
print(idol['bts'])
print(idol['bts']['RM'])

#딕셔너리 반복문 활용하기
#기본 활용
for key in lunch:
    print(key)  # -> key
    print(lunch[key]) #=> value

#key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)

#value만 가져오기 : .values()
for value in lunch.values():
    print(value)

#item  (key,value)  가져오기 : .items()

for item in lunch.items():
    print(item)

#문제

score = {
    '수학':80,
    '국어':90,
    '음악':100
}

#1. 평균점수
avg=0
for value in score.values():
    avg+=value
   

print(avg/len(score))

#다른방법
# total_score = sum(score.values())
# print(total_score)

#두번째 문제 반평균을 구하시오

scores = {
    'a' : {
    '수학':80,
    '국어':90,
    '음악':100
    },
    'b' : {
    '수학':70,
    '국어':50,
    '음악':35
    },
    'c' : {
    '수학':70,
    '국어':50,
    '음악':35
    }
}

total_score = 0
cnt=0
for stu in scores:
    for score in scores[stu]:
        total_score += scores[stu][score]
        cnt+=1

print(total_score/cnt)

#마지막 문제 도시별 최근 3일의 온도입니다.
city = {
    '서울' : [-6,-10,6],
    '대전' : [-3,-6,2],
    '광주' : [-0,-2,10],
    '구미' : [2,-2,9]
}
#3-1 도시별 최근 3일의 온도 평균은?

for a in city.keys():
    print(f'{a} : {round(sum(city[a])/len(city[a]),2)}')



for name, temp in city.items():
    avg_temp = sum(temp)/len(temp)
    print(f'{name} : {avg_temp}')



