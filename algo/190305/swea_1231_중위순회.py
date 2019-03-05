import sys

sys.stdin = open("1231.txt")

def inorder_traversal(now):
    global n
    if now <= n:
        if now * 2 <= n :
            inorder_traversal(now*2)
        print(tree[now],end='')
        if now * 2 + 1 <= n :
            inorder_traversal(now*2+1)


for tc in range(1,11):
    n = int(input())

    tree = [0]

    for k in range(n):
        data = list(input().split())
        tree.append(data[1])

    # print(tree)
    print('#%d' %(tc),end=' ')
    inorder_traversal(1)
    print()