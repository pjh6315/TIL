import sys

sys.stdin = open("input.txt")

mymax = 0

def dfs(start,cost):
     global n,mymax
     visited[start] = 1
     if cost > 40:
         t_cost = cost - money[start]
         if mymax < t_cost:
             mymax = t_cost
         return
     else:
         for i in range(n):
             if visited[i] == 0 :
                 dfs(i,cost + money[i])



b = int(input())
n = int(input())

money = list(map(int,input().split()))



for i in range(n):
    visited = [0 for i in range(n + 1)]
    dfs(i,0)

print(mymax)
