from collections import defaultdict

t = int(input())

def dfs(g,v,visited=None,path=None):
    if visited is None:
        visited = []
    if path is None:
        path = [v]
    
    visited.append(v)
    paths=[]
    for point in g[v]:
        if point not in visited:
            temp_path = path + [point]
            paths.append(tuple(temp_path))
            paths.extend(dfs(g,point,visited[:],temp_path))
    return paths

for tc in range(1,t+1):
    n,m = map(int,input().split())
    point = []
    all_paths = []
    max_len = 0
    graph = {}
    if m == 0:
        max_len = 1
    else:
        for i in range(m):
            point.append(list(map(int,input().split())))
        
        graph = defaultdict(list)
        for s,t in point:
            graph[s].append(t)
            graph[t].append(s)

        for point in graph.keys():
            all_paths.extend(dfs(graph,point))
        
        max_len = max(len(path) for path in all_paths )
        print(all_paths)
    print(f'#{tc} {max_len}')
    


