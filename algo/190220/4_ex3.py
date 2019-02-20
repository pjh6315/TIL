import sys
sys.stdin = open("input.txt")

mymap = [[0] * 8 for i in range(8)]
visited = [0] * 8

def dfs(here):
    print(here)
    visited[here] = True

    for next in range(8):
        if mymap[here][next] and not visited[next]:
            dfs(next)



data = list(map(int,input().split()))
howmany = int(len(data)/2)

for i in range(howmany):
    start = data[i*2]
    stop = data[i*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

dfs(1)