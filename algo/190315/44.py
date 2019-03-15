data = [5,1,-4,2,-1,-5,-2,8,-3,6]

rangesum = [0] * 10

rangelist = [[]] * 10

def max_sum(now):

    if now == 0:
        if data[now] >= 0:
            rangesum[now] = data[now]
            rangelist[now] += [data[now]]
        else:
            rangesum[now] = 0
            rangelist[now] = []
    else:
        rangesum[now] = max(rangesum[now-1] + data[now],data[now])
        if rangesum[now-1] + data[now] >data[now] :
            rangelist[now] = rangelist[now-1] + [data[now]]
        else:
            rangelist[now] = [data[now]]

    if now < 9:
        max_sum(now + 1)
    # return max(rangesum[now-1] + data[now],data[now])


max_sum(0)
# print(rangesum)
# print(rangelist)

print(max(rangesum))
print(rangelist[rangesum.index(max(rangesum))])