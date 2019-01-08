n = int(input())

def sudoku(llist):
    for i in range(0,9):
        if sum(llist[i]) != 45:
            return 0
    


for tc in range (1,n+1):
    num =[]
    ans = 1
    for i in range(0,9):
        num.append(list(map(int,input().split())))
    
    sudoku(num)