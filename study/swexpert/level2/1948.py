n = int(input())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range (1,n+1):
    day = 0
    temp = list(map(int,input().split()))
    # 같은 월
    if temp[0] == temp[2]:
        day = temp[3] - temp[1] +1
    # 1달 차이
    elif temp[2]-temp[0] == 1:
        day += temp[3] + month[temp[0]]-temp[1] +1
    # 그외
    else:
        for i in range (temp[0]+1,temp[2]):
            day += month[i]
        day += temp[3] + month[temp[0]]-temp[1] +1
    
    print(f'#{tc} {day}')