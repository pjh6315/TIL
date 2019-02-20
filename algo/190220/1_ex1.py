import sys
sys.stdin = open("input.txt")

stack = [0] * 10
top = -1

for i in range(1,4):
    top+=1
    stack[top] = i


while top != -1:
    print(print(stack[top]))
    top -=1