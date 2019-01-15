t = int(input())

for tc in range(1,t+1):
    n = int(input())
    llist = [int(input()) for i in range(n)]
    temp = 0
    avg = sum(llist)/n
    for i in range(n):
        temp += abs(avg-llist[i])
    print(f'#{tc} {int(temp/2)}')