def palin(s):
    if s == s[::-1]:
        return True
    else:
        return False


for tc in range(1, 11):
    n = int(input())
    ans = 101
    garo = []
    sero = []
    check = 0
    for i in range(100):
        garo.append(input())
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += garo[j][i]
        sero.append(temp)

    while ans >= 1 and check == 0:
        ans -= 1
        for i in range(100):
            for j in range(0, 101 - ans):
                if palin(garo[i][j:j + ans]):
                    check = 1
                if palin(sero[i][j:j + ans]):
                    check = 1
                if check == 1:
                    break
            if check == 1:
                break

    print(f'#{tc} {ans}')