for tc in range(10):
    n = int(input())
    num = []
    for i in range(100):
        num.append(list(map(int,input().split())))
    sum_list =[]

    for i in range(100):
        sum_list.append(sum(num[i]))
    
    for i in range(100):
        temp = 0
        for j in range(100):
            temp+=num[j][i]
        sum_list.append(temp)
    temp = 0
    for i in range(100):
        temp+=num[i][i]
    sum_list.append(temp)
    temp = 0
    for i in range(100):
        temp+=num[i][100-1-i]
    sum_list.append(temp)



    print(f'#{n} {max(sum_list)}')