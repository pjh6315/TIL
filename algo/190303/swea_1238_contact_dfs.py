import sys

sys.stdin = open("1238.txt")

def dfs(start,dis):
    if distance[start] == 0:
        distance[start] = dis
    else:
        if distance[start] > dis:
            distance[start] = dis

    for next in range(1,101):
        if mymap[start][next] == 1 and visited[next] == 0 :
            visited[next] = 1
            dfs(next,dis+1)
            visited[next] = 0

for tc in range(1,11):
    n , start = map(int,input().split())

    data = list(map(int,input().split()))

    mymap = [[0 for i in range(100+1)] for i in range(100+1) ]
    visited = [0 for i in range(100+1)]
    distance= [0 for i in range(100+1)]
    for index in range(0,n,2):
        mymap[data[index]][data[index+1]] = 1

    visited[start] = 1
    dfs(start,0)

    t = max(distance)
    for index in range(len(distance)):
        if distance[index] == t:
            result = index

    print('#%d %d' %(tc,result))