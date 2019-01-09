n = int(input())
def palin(s):
    if s == s[::-1]:
        return 1
    else:
        return 0


for tc in range(1,n+1):
    s = input()
    
    print(f'#{tc} {palin(s.rstrip())}')