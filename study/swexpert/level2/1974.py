n = int(input())

def sudoku(llist):
    # 가로
    for i in range(0,9):
        if sum(llist[i]) != 45:
            return 0
    # 세로
    for i in range(0,9):
        temp = 0
        for j in range(0,9):
            temp += llist[j][i]
        if temp != 45:
            return 0
    # 3 X 3
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp =0
            for k in range(0,3):
                for o in range(0,3):
                    temp += llist[i+k][j+o]
                    # print(llist[i+k][j+o])
            if temp != 45:
                return 0

    return 1




for tc in range (1,n+1):
    num =[]
    ans = 1
    for i in range(0,9):
        num.append(list(map(int,input().split())))
    
    print(f'#{tc} {sudoku(num)}')