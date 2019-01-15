t = int(input())
for tc in range(1,t+1):
    n = int(input())
    num = set()
    a = n
    cnt = 1
    while len(num) != 10:
        while a:
            num.add(a%10)
            a //= 10
        cnt +=1
        a = n * cnt
    print(f'#{tc} {a-n}')