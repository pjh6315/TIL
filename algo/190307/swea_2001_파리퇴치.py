n = int(input())

for tc in range(1, n + 1):
    n, m = map(int, input().split())

    max = 0
    paris = []

    for i in range(n):
        paris.append(list(map(int, input().split())))

    for i in range(0, n - m + 1):
        for j in range(0, n - m + 1):
            temp = 0
            for k in range(0, m):
                for y in range(0, m):
                    temp += paris[i + k][j + y]
            if temp > max:
                max = temp

    print(f'#{tc} {max}')
