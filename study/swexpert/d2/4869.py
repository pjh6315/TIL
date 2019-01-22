t = int(input())

def check(n):
    result = []
    stack  = []
    visit = []
    
    stack.append(10)
    while stack:
        if sum(stack) == n and stack not in result :
            result.append(stack)
            visit.append(stack.pop())
        elif sum(stack) > n :
            visit.append(stack.pop())
        
        



for tc in range(1,t+1):
    n = int(input())


