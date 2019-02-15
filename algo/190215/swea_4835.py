t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())

    number = list(map(int,input().split()))

    temp_sum = []


    for index in range(len(number)-m+1):
        temp = 0
        for index2 in range(index,index+m):
            temp += number[index2]
        temp_sum.append(temp)


    print(f'#{tc} {max(temp_sum)-min(temp_sum)}')



