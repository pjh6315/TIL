import sys

sys.stdin = open('ex1_input.txt','r')

data = list(map(int,input().split()))

result = 0

for i in range(len(data)):
    max_box = len(data) - i - 1
    for j in range(i+1,len(data)):
        if data[i] <= data[j]:
            max_box -= 1
    if result < max_box:
        result = max_box


print(result)