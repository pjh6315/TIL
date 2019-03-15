result = []
result2 = []
def norecur():

    for x in range(1,100):
        for y in range(x,100):
            for z in range(y,100):
                if x+y+z == 100:
                    result.append([x,y,z])


def recur(now,sum,cnt,temp=None):
    if temp == None:
        temp = []

    if now > 98:
        return
    if cnt == 3 and sum == 100 and temp not in result2:
        result2.append(temp)
    elif cnt > 3 or sum > 100:
        return

    else:
        new_temp = temp + [now]

        recur(now,sum+now,cnt+1,new_temp)

        recur(now+1,sum+now,cnt+1,new_temp)
        recur(now+1,sum,cnt,temp)


norecur()
print(len(result))
print(result)

recur(1,0,0)
print(len(result2))
print(result2)
