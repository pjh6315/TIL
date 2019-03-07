n = int(input())

for tc in range(1, n + 1):
    n, k = map(int, input().split())
    puzzle = []
    cnt = 0
    for i in range(0, n):
        puzzle.append(list(map(str, input().split())))

    ver_puzzle = [[0] * (n) for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            ver_puzzle[i][j] = puzzle[j][i]

    for i in range(0, n):
        for j in range(0, n):
            if puzzle[i][j] == '0':
                puzzle[i][j] = ' '
            if ver_puzzle[i][j] == '0':
                ver_puzzle[i][j] = ' '

    for i in range(0, n):
        puzzle[i] = ''.join(puzzle[i])
        puzzle[i] = puzzle[i].split()
        ver_puzzle[i] = ''.join(ver_puzzle[i])
        ver_puzzle[i] = ver_puzzle[i].split()

    for i in range(0, n):
        cnt += puzzle[i].count('1' * k)
        cnt += ver_puzzle[i].count('1' * k)
    print(f'#{tc} {cnt}')