t = int(input())

for tc in range(1,t+1):
    n = int(input())
    myheap = []
    result = []
    for i in range(n):
        temp = list(map(int,input().split()))
        result.append(hheap(temp,myheap))
    print(f'#{tc} ',end="")
    for n in result:
        if n is not None:
            if n != len(result)-1:
                print(n,end=" ")
            else:
                print(n)
    print()
