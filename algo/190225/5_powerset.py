import sys

sys.stdin = open("powerset.txt")

result = []

def powerset(now,llist,now_sum,end,now_list=None):
	if now_list is None:
		now_list = []

	if now_sum == end:
		result.append(now_list)
	elif now < 10 :
		# 현재값 선택
		temp = now_list + [llist[now]]
		powerset(now+1,llist,now_sum+llist[now],end,temp)
		# 현재값 선택 X
		powerset(now+1,llist,now_sum,end,now_list)



data = list(map(int,input().split()))

powerset(0,data,0,10)

print(result)
