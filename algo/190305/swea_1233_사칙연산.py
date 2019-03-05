import sys

sys.stdin = open("1233.txt")

check = ['-','*','/','+']

def isok(now):
    global n,chk

    left = now*2
    right = now*2+1
    if left <= n and right <= n:
        isok(left)
        isok(right)
    elif tree[now] in check:
        chk = False


for tc in range(1,11):
    n = int(input())
    chk = True
    tree = [0]

    for i in range(n):
        data=list(input().split())
        tree.append(data[1])
    isok(1)
    if chk:
        print('#%d 1' %tc)
    else:
        print('#%d 0' % tc)
