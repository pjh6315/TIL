n = int(input())

for tc in range(1,n+1):
    s = input()
    ans = 0

    for i in range(1,11):
        check = s[0:i]
        if check == s[i:2*i]:
            break
        
    print(f'#{tc} {i}')