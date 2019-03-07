result = []
data = [1,2,3,4,5]
def combination(n,r,now=0,cnt=0,temp=None):
    global result
    if temp == None:
        temp = []
    if cnt == r:
        result.append(temp)
    elif n-now < r-cnt:
        return
    elif now < n:
        # 선택
        new_temp = temp + [data[now]]
        combination(n, r, now + 1, cnt + 1, new_temp)
        # 선택x
        combination(n,r,now+1,cnt,temp)



combination(5,3)

print(result)