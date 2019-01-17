t = int(input())

for tc in range(1,t+1):
    s = str(input())

    cnt = 0
    if s[0] == '1':
        cnt+=1

    for i in range(0,len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1

    print(f'#{tc} {cnt}')