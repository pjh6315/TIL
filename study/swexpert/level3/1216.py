def palin(s):
    if s == s[::-1]:
        return True
    else:
        return False

for tc in range(1,11):
    n = int(input())
    llist = []
    cnt = 0
    for i in range(100):
        llist.append(input())
    
    for i in range(0,100):
        for j in range(0,101-n):
            temp = ''
            for k in range(0,n):
                temp+=llist[i][j+k]
            if palin(temp):
                cnt+=1

    for i in range(0,101-n):
        for j in range(0,100):
            temp = ''
            for k in range(0,n):
                temp+=llist[i+k][j]
            if palin(temp):
                cnt+=1
    
    print(f'#{tc} {cnt}')