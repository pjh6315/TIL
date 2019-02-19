import sys

sys.stdin = open("input.txt", 'r')

t = int(input())
a = [i for i in range(1, 13)]
all_sub_set = []

def select_bit(now,now_cnt,max_cnt,mybit):
    temp = mybit[:]
    if  now_cnt == max_cnt:
        all_sub_set.append(temp)
    elif now >= len(mybit):
        return
    else:
        temp[now] = 1
        select_bit(now+1,now_cnt+1,max_cnt,temp)
        temp[now] = 0
        select_bit(now+1, now_cnt, max_cnt,temp)

def check_sum(a,sub_set,ans):
    cnt = 0
    for sub in sub_set:
        temp = 0
        for i in range(12):
            if sub[i] == 1:
                temp += a[i]
        if temp == ans:
            cnt += 1

    return cnt


for tc in range(1, t+1):
    n, k = map(int, input().split())
    chk = False
    bit = [0 for i in range(12)]
    subsetcnt = 0
    select_bit(0,0,n,bit)
    # print(all_sub_set)
    # check_sum(a, all_sub_set, k)
    print(f'#{tc} {check_sum(a,all_sub_set,k)}')

    # for i in range(1 << 12):
    #     temp_sum = 0
    #     temp = []
    #     cnt = 0
    #     for j in range(12):
    #         if i & (1 << j):
    #             temp_sum += a[j]
    #             temp.append(a[j])
    #             cnt += 1
    #     if temp_sum == k and cnt == n:
    #         subsetcnt += 1
    #
    # print(f'#{tc} {subsetcnt}')


    all_sub_set = []