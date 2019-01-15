n = int(input())

for i in range (0,n):
    k = int(input())
    num = list(map(int,input().split()))
    ans = max(num,key=num.count)
    print(f'#{k} {ans}')
        


    