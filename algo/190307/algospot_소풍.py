import sys

sys.stdin = open('picnic.txt')

t = int(input())
result = []
def dfs(now,sub,temp=None):
    global n
    if temp == None:
        temp = []

    if len(sub) == 0:
        if len(temp) == n//2:
           result.append(temp)
    else:
        #선택
        new_temp = [sub[now]]
        new_temp = new_temp + temp
        a = sub[now][0]
        b = sub[now][1]
        new_sub = []
        for pairs in sub:
            if a not in pairs and b not in pairs:
                new_sub.append(pairs)
        dfs(now,new_sub,new_temp)

        #선택x
        sub.pop(0)
        dfs(now,sub,temp)

for tc in range(1,t+1):

    n , m = map(int,input().split())

    data = list(map(int,input().split()))
    result = []
    friends = []

    for i in range(0,len(data),2):
        friends.append([data[i],data[i+1]])

    # print(friends)

    dfs(0,friends)

    print(len(result))