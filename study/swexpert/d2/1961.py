n = int(input())

for tc in range(1,n+1):
    line = int(input())
    num =[]
    for i in range(0,line):
        num.append(list(map(int,input().split())))
    
    print(f'#{tc}')
    for i in range (0,line):
        for j in range(line-1,-1,-1):
            print(num[j][i],end='')
        print(' ',end='')
        for j in range(line-1,-1,-1):
            print(num[line-i-1][j],end='')
        print(' ',end='')
        for j in range(0,line):
            print(num[j][line-i-1],end='')
        print()
