import sys

sys.stdin = open("input.txt",'r')

def selection_sort(llist):

    for index in range(len(llist)-1):
        min_value = llist[index]
        min_index = index
        for index2 in range(index,len(llist)):
            if min_value > llist[index2]:
                min_value = llist[index2]
                min_index = index2
        llist[index],llist[min_index] = llist[min_index],llist[index]

    return llist

data = list(map(int,input().split()))

print(selection_sort(data))