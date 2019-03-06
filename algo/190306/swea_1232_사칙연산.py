import sys

sys.stdin = open("1232.txt")

for tc in range(1,11):
    n = int(input())

    data = []

    for i in range(n):
        data.append(list(input().split()))

    for i in range(n-1,-1,-1):
        if len(data[i]) == 4:
            left = float(data[int(data[i][2]) - 1][1])
            right = float(data[int(data[i][3]) - 1][1])
            cal = data[i][1]

            if cal == '+':
                data[i][1] = left + right
            elif cal == '-':
                data[i][1] = left - right
            elif cal == '*':
                data[i][1] = left * right
            elif cal == '/':
                data[i][1] = left / right

    print('#%d %d' %(tc,int(data[0][1])))
