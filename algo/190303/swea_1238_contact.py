import sys

sys.stdin = open("1238.txt")

def bfs(startt):
    global mymap,visited
    queue = []

    queue.append(startt)

    while queue:
        a = queue.pop(0)
        visited[a] = 1

        for next in range(1,101):
            if mymap[a][next] == 1 and visited[next] == 0 and next not in queue:
                queue.append(next)
                distance[next] = distance[a] + 1


for tc in range(1,11):
    n , start = map(int,input().split())

    data = list(map(int,input().split()))

    mymap = [[0 for i in range(100+1)] for i in range(100+1) ]
    visited = [0 for i in range(100+1)]
    distance= [0 for i in range(100+1)]
    for index in range(0,n,2):
        mymap[data[index]][data[index+1]] = 1


    bfs(start)
    t = max(distance)
    for index in range(len(distance)):
        if distance[index] == t:
            result = index

    print('#%d %d' %(tc,result))