import sys

sys.stdin = open("input.txt",'r')

data = list(map(int,input().split()))

n = len(data)
result = []
for i in range(1<<n):
    temp_sum = 0
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp_sum += data[j]
            temp.append(data[j])

    if temp_sum == 0 and len(temp) != 0:
        result.append(tuple(temp))

print(result)