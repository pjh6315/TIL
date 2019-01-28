t = int(input())

def dfs(llist, start,want,visited=None,path=None):
    if visited is None:
        visited = []
    if path is None:
        path = [llist[start]]
    
    visited.append(start)
    print(visited)
    paths=[]
    for i in range(start+1,len(llist)):
        if i not in visited:
            print(llist[i])
            if sum(path) + llist[i] == want:
                temp = path + [llist[i]]
                # paths.extend(dfs(llist,i,want,visited,temp))
                paths.append(tuple(temp))
                # temp = None
                # dfs(llist,start,want,visited,temp)
            elif sum(path) + llist[i] < want:
                temp = path + [llist[i]]
                paths.extend(dfs(llist,i,want,visited,temp))
            else:
                return paths
    return paths



for tc in range(1,t+1):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    all_paths = []


    for i in range(n):
        if a[i] == k :
            all_paths.append(a[i])
        else:
            all_paths.extend(dfs(a,i,k))
    print(all_paths)
    print(f'#{tc} {len(all_paths)}')