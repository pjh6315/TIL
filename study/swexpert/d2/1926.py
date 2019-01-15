n = int(input())

three = ['3','6','9']
temp = ''
for i in range(1,n+1):
    cnt = 0
    for j in str(i):
        if j in three:
            cnt += 1
        else:
            temp += j
    if cnt > 0 :
        for k in range(cnt):
            print('-',end='')
            cnt = 0
    else:
        print(temp,end='')
    temp=''
    print(' ',end='')
