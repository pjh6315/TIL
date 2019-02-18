import sys

sys.stdin = open("input.txt",'r')

def sequentialsearch(llist,key):
    for index in range(len(llist)):
        if llist[index] == key:
            return index

def binary_search(llist,key):
    temp_list = llist[:]
    temp_list.sort()
    print(temp_list)
    start = 0
    end = len(temp_list)-1

    while start <= end:
        if key == temp_list[start+end//2]:
            return (start+end)//2
        elif key > temp_list[(start+end)//2]:
            start = (start+end)//2 + 1
        else:
            end = (start+end)//2 - 1

    return False

data = list(map(int,input().split()))

print(sequentialsearch(data,-6))

print(binary_search(data,0))