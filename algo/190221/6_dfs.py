import sys
sys.stdin = open("input.txt")

#input
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

mymap = [[0]*8 for i in range(8)]
stack = [0]*10
visited = [0] * 8
top = -1

def push(x):
	global top
	top += 1
	stack[top] = x

def pop():
	global top
	if top == -1:
		return 0
	x = stack[top]

	top -= 1
	return x


def findnext(here):
	for next in range(8):
		if mymap[here][next] and not visited[next]:
			return next


def DFS(here) :
    global top
    print(here)
    visited[here] = True
    while here:
        next = findnext(here)
        if next :
	        push(here)

        while next :
                print(next)
                visited[next] = True
                push(next)
                here= next
                next = findnext(here)
        here = pop()




Data =  list(map(int,input().split()))
howmany = int(len(Data) / 2)

for i in range(howmany):
     Start= Data[i*2]
     Stop = Data[i*2+1]
     mymap[Start][Stop] = 1
     mymap[Stop][Start] = 1

DFS(1)