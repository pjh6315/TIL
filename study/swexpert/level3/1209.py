for tc in range(1,11):
    n = int(input())
    num = list(map(int,input().split()))
    max = 0
    temp = 0

    for i in range(0,10000,100):
        for j in range(100):
            temp += num[i+j]
        if max < temp:
            max = temp
            
    for i in range(100):
        for j in range(0,10000,100):
            temp+= num[i+j]
        if max < temp:
            max = temp
            