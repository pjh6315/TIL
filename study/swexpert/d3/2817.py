t = int(input())

# def dfs(llist, start,want,visited=None,path=None):
#     if visited is None:
#         visited = []
#     if path is None:
#         path = [llist[start]]
    
#     visited.append(start)
#     print(visited)
#     paths=[]



    # for i in range(start+1,len(llist)):
    #     if i not in visited:
    #         print(llist[i])
    #         if sum(path) + llist[i] == want:
    #             temp = path + [llist[i]]
                
    #             paths.append(tuple(temp))
                
    #         elif sum(path) + llist[i] < want:
    #             temp = path + [llist[i]]
    #             paths.extend(dfs(llist,i,want,visited,temp))
    #         else:
    #             return paths
    # return paths

# def dfs(llist,start,want,result=None,temp=None):
#     if result == None:
#         result = []
#     if temp == None:
#         temp = []

#     for i in range(start,len(llist)):
#         t = sum(temp) + llist[i]
#         tttt = temp + [llist[i]]
#         if t < want :      
                                                                                                                   
#             result.extend(dfs(llist,start+1,want,result,tttt))
#         elif t == want :
#             result.append(tuple(tttt))

#     return result
        
def dfs (llist,current,ans,temp_list=None):
    result=[]
    if temp_list is None:
        temp_list=[]
    if current == len(llist)-1:
        if sum(temp_list) == ans:
            return tuple(temp_list)
        return result
    
    result.extend(dfs(llist,current+1,ans,temp_list.append(llist[current])))

    result.extend(dfs(llist,current+1,ans,temp_list))

    return result


                                    
for tc in range(1,t+1):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    all_paths = []


    # for i in range(n):
    #     if a[i] == k :
    #         all_paths.append(a[i])
    #     else:
    #         all_paths.extend(dfs(a,i,k))
    all_paths= dfs(a,0,k)
    print(all_paths)
    print(f'#{tc} {len(all_paths)}')