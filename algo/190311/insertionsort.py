a = [1,9,3,6,7,0,4,9,5,5,11,19,2,2,2,2,2,2,2,2,2,2,2]

def insertion_sort(llist):

    for j in range(2,len(llist)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i -1
        a[i+1] = key


insertion_sort(a)

print(a)