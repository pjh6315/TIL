import sys
sys.stdin = open("input.txt")

#input
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

mymap = [[0] * 8 for i in range(8)]
visited = [0] * 8

def dfs(here):
    print(here)
    visited[here] = True

    for next in range(8):
        if mymap[here][next] and not visited[next]:
            dfs(next)

# 비재귀
def dfs2(here):




data = list(map(int,input().split()))
howmany = int(len(data)/2)

for i in range(howmany):
    start = data[i*2]
    stop = data[i*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

dfs(1)