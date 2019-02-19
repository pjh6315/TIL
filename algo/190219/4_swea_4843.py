import sys

sys.stdin = open("input.txt",'r')

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    num_list = list(map(int,input().split()))
    max_list = num_list[:]
    min_list = num_list[:]
    result = [0 for i in range(n)]

    for i in range(0,n,2):
        t_max = -987654321
        t_min = 987654321
        max_index = 0
        min_index = 0
        for k in range(n):
            if max_list[k] > t_max:
                t_max = max_list[k]
                max_index = k
            if min_list[k] < t_min:
                t_min = min_list[k]
                min_index = k

        max_list[max_index] = -987654321
        min_list[min_index] = 987654321
        result[i] = t_max
        result[i+1] = t_min



    print(f'#{tc}',end=' ')

    for index in range(10):
        print(result[index],end=' ')
    print()

