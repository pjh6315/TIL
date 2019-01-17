for tc in range(1,11):
    n, s = input().split()
    chk = 0
    s = list(s)
    while chk==0:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                break
            elif i == len(s)-2:
                chk = 1
    s = ''.join(s)
    print(f'#{tc} {s}')
                
