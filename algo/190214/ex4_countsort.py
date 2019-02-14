data = list(map(int,input().split()))



def counting_sort(number):
    counts = [0] * 100

    result = [0] * len(number)

    for n in number:
        counts[n] += 1


    for i in range(1,len(counts)):
        counts[i] += counts[i-1]

    for n in number:
        result[counts[n]-1] = n
        counts[n] -= 1

    return result



print(counting_sort(data))