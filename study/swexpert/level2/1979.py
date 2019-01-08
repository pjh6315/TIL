n = int(input())

for tc in range(1,n+1):
    n,k = map(int,input().split())
    puzzle =[]
    cnt = 0
    for i in range(0,n):
        puzzle.append(list(map(str,input().split())))
    
    for i in range(0,n):
        for j in range(0,n):
            if puzzle[i][j] == '0':
                puzzle[i][j] = ' '
    print(puzzle)
    
    for i in range(0,n):
        puzzle[i] = ''.join(puzzle[i])
        puzzle[i] = puzzle[i].split()
    print(puzzle)