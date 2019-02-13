t = int(input())

def check(film,d,w,k):
    for i in range(w):
        cnt = 1
        chk = 0
        for j in range(d):
            if j == 0 :
                temp = film[j][i]
            elif temp == film[j][i]:
                cnt += 1
            if cnt == k :
                chk = 1
                break
            elif temp != film[j][i]:
                cnt = 1
                temp = film[j][i]
        if chk == 0 :
            return False
    return True

def medi(film,now,d,w,k,cnt=0):
    a,b,c = 13,13,13
    # if now == d-1 :
    #     if check(film,d,w,k):
    #         return cnt
    if now == d:
        if check(film,d,w,k):
            return cnt
    else:
        # x
        a = medi(film,now+1,d,w,k,cnt)
        # a
        temp = film[now]
        film[now] = [0] * w
        b = medi(film,now+1,d,w,k,cnt+1)
        film[now] = temp
        # b
        temp = film[now]
        film[now] = [1] * w
        c = medi(film,now+1,d,w,k,cnt+1)
        film[now] = temp

    return min(a,b,c)
        

for tc in range(1,t+1):
    d,w,k = map(int,input().split())

    film = []

    for i in range(d):
        film.append(list(map(int,input().split())))

    if k == 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {medi(film,0,d,w,k)}')
    