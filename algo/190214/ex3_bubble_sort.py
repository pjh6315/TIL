data = list(map(int,input().split()))

def bubblesort(num):

    for i in range(len(num)-1):
        for j in range(0,i):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]



bubblesort(data)
print(data)