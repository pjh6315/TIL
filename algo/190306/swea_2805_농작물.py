t = int(input())

for tc in range(1,t+1):
    n = int(input())
    result = 0
    j =2
    llist = []
    for i in range(n):
        llist.append(list(map(int,input())))

    for i in range(n):
        if i <= int(n/2):
            result += sum(llist[i][int(n/2)-i:int(n/2+1)+i])
        else:
            result += sum(llist[i][int(n/2)-i+j:int(n/2+1)+i-j])
            j+=2W
    print(f'#{tc} {result}')