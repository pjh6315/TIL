import sys

sys.stdin = open("5177.txt")

t = int(input())


for tc in range(1,t+1):
    n = int(input())
    data = list(map(int,input().split()))

    result = [0]

    for node in data:
        if len(result) != 1:
            result.append(node)
            now_index = len(result) - 1
            parents_index = now_index // 2
            while parents_index > 0 :
                if result[now_index] < result[parents_index]:
                    result[now_index],result[parents_index] = result[parents_index],result[now_index]
                else:
                    break
                now_index,parents_index = parents_index,parents_index//2
        else:
            result.append(node)

    index = n
    temp = 0
    while index > 0 :
        index = index // 2
        temp += result[index]
    print(result)
    print('#%d %d' %(tc,temp))