import sys

sys.stdin = open("input.txt",'r')

def binary_search(pages,key):
    start = 1
    end = pages

    cnt = 0
    while start <= end:
        middle = int((start + end) / 2)
        cnt+=1
        if key == middle:
            return cnt
        elif key > middle:

            start = middle
        else:
            end = middle



t = int(input())



for tc in range(1,t+1):
    p,a,b = map(int,input().split())

    a_cnt = binary_search(p,a)
    b_cnt = binary_search(p, b)


    if a_cnt < b_cnt:
        print(f'#{tc} A')
    elif a_cnt == b_cnt:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
