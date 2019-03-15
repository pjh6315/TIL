data = [1,2,3,4,5]

result= []
def re_combination(n,r,now=0,cnt=0,temp=None):

    if temp == None:
        temp = []

    if cnt == r:
        if temp not in result:
            result.append(temp)
        return

    if now < n :
        # 선택
        new_temp = []
        new_temp = temp + [data[now]]
        re_combination(n,r,now,cnt+1,new_temp)

        re_combination(n,r,now+1,cnt+1,new_temp)
        re_combination(n,r,now+1,cnt,temp)


re_combination(5,3)
print(result)
print(len(result))


