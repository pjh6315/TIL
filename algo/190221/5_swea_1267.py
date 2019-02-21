import sys
sys.stdin = open("input.txt")

path = []

def delete

def dfs(my_map,length):

	for y in range(1,length):
		if my_map[y].count(1) == 0 and y not in path:
			path.append(y)


for tc in range(1,3):
	v, e = map(int,input().split())
	path=[]
	data = list(map(int,input().split()))

	my_map = [[0 for i in range(v+1)] for i in range(v+1)]



	my_data = []

	for i in range(0,2*e,2):
		my_map[data[i+1]][data[i]] = 1

	print(my_map)

