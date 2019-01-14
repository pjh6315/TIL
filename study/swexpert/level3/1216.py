def palin(s):
    if s == s[::-1]:
        return True
    else:
        return False

for tc in range(1,2):
    n = int(input())
    ans = 0
    llist = []
    cnt = []
    for i in range(100):
        llist.append(input())
    print(type(llist[0]))

    
    print(f'#{tc} {ans}')