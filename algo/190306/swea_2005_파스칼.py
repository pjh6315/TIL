n = int(input())

for tc in range(1, n + 1):
    x = int(input())

    tri = [[0] * (x + 1) for i in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, i + 1):
            if i == 1:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
    print('#%d' %tc)

    for tt in tri:
        print(tt)

    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print(tri[i][j], end=' ')
        print()
