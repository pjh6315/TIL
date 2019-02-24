import sys
sys.stdin = open("input.txt")

path = []
visited= []

def delete(my_map,x,length):
	for y in range(1,length+1):
		my_map[y][x] = 0


def dfs(my_map,length):

	while len(path) < length:
		for y in range(1,length+1):
			if sum(my_map[y]) == 0 and y not in path:
				path.append(y)
				delete(my_map,y,length)






for tc in range(1,11):
	v, e = map(int,input().split())
	path=[]
	data = list(map(int,input().split()))
	my_map = [[0 for i in range(v+1)] for i in range(v+1)]



	my_data = []

	for i in range(0,2*e,2):
		my_map[data[i+1]][data[i]] = 1


	dfs(my_map,v)

	print(f'#{tc} {" ".join(map(str,path))}')




