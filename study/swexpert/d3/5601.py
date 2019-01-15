t = int(input())

for tc in range(1,t+1):
    n = int(input())
    result='1/'+str(n)

    print(f'#{tc}',end=" ")

    for i in range(0,n):
        print(result,end=' ')
    print()

    