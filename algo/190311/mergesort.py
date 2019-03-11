data = [38,27,43,3,9,82,10]


# def merge(left,right):
#     i = 0
#     j = 0
#     k = 0
#     result_len = len(left) + len(right)
#     result = [0 for i in range(result_len)]
#
#     while k < result_len:
#         if i == len(left):
#             result[k] = right[j]
#             j += 1
#
#         elif j == len(right):
#             result[k] = left[i]
#             i += 1
#
#         elif left[i] > right[j]:
#             result[k] = right[j]
#             j += 1
#
#         else:
#             result[k] = left[i]
#             i += 1
#         k += 1
#
#     return result
#
#
# def merge_sort(llist):
#     if len(llist) <= 1:
#         return llist
#     left = merge_sort(llist[:len(llist)//2])
#     right = merge_sort(llist[len(llist)//2:])
#
#     return merge(left,right)

def merge(start,middle,end):
    if data[start] > data[middle]:
        data[start],data[middle] = data[middle],data[start]

    if data[middle+1] > data[end]:
        data[middle+1],data[end] = data[end],data[middle+1]


def merge_sort(start,end):
    if start >= end:
        return
    m = (start+end) // 2
    merge_sort(start,m)
    merge_sort(m+1,end)
    merge(start,m.end)


# print(data)



print(merge_sort(0,len(data)-1))

print(data)