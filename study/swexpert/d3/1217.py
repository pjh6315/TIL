def my_pow(a,b):
    if b == 0:
        return 1
    else:
        return a*my_pow(a,b-1) 


for tc in range(1,11):
    n = int(input())
    a,b = map(int,input().split())

    print(f'#{tc} {my_pow(a,b)}')