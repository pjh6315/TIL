import sys

sys.stdin = open("input.txt",'r')

for tc in range(10):
    n = int(input())
    num = []
    for i in range(100):
        num.append(list(map(int, input().split())))
    sum_list = []
    #가로
    for i in range(100):
        sum_list.append(sum(num[i]))
    #세로
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += num[j][i]
        sum_list.append(temp)
    #대각 우하
    temp = 0
    for i in range(100):
        temp += num[i][i]
    sum_list.append(temp)
    #대각 좌하
    temp = 0
    for i in range(100):
        temp += num[i][100 - 1 - i]
    sum_list.append(temp)

    print(f'#{n} {max(sum_list)}')