import sys

sys.stdin = open("input.txt",'r')

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    num_list = list(map(int,input().split()))

    nasa = []
    for index in range(0,2*n,2):
        nasa.append((num_list[index],num_list[index+1]))


    result = []

    while len(result) < 2*n:
        if len(result) == 0:
            result += [nasa[0][0]] + [nasa[0][1]]
        else:
            for k in nasa:

                if k[0] == result[-1]:
                    result += [k[0]] + [k[1]]
                elif k[1]== result[0]:
                    result = [k[0]] + [k[1]] + result


    print(f'#{tc}',end=' ')

    for num in result:
        print(num,end=' ')
    print()
