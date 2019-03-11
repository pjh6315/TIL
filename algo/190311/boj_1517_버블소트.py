import sys

sys.stdin = open('1517.txt')

n = int(input())

data = list(map(int,input().split()))
cnt = 0

def merge(left,right):
    global cnt
    i = 0
    j = 0
    k = 0
    len_left = len(left)
    len_right = len(right)
    result_len = len_left + len_right
    result = [0 for i in range(result_len)]

    while k < result_len:

        if i == len_left:
            result[k] = right[j]
            j += 1

        elif j == len_right:
            result[k] = left[i]
            i += 1

        elif left[i] > right[j]:
            cnt += i-k+1
            result[k] = right[j]
            j += 1

        else:
            cnt += j-k+1
            result[k] = left[i]
            i += 1
        k += 1

    return result


def merge_sort(llist):
    len_list = len(llist)
    if len_list <= 1:
        return llist
    left = merge_sort(llist[:len_list//2])
    right = merge_sort(llist[len_list//2:])

    return merge(left,right)

# def merge(start,middle,end):
#     global cnt
#     i = start
#     j = middle + 1
#     k = 0
#     result = [0 for i in range(end-start+1)]
#
#
#     while k < end-start+1:
#
#         if i == middle:
#             result[k] = data[j]
#             j += 1
#
#         elif j == end:
#             result[k] = data[i]
#             i += 1
#
#         elif data[i] > data[j]:
#             cnt += middle - start + 1
#             result[k] = data[j]
#             j += 1
#
#         else:
#             cnt += end-middle
#             result[k] = data[i]
#             i += 1
#         k += 1
#
#
#
#     # if data[start] > data[end]:
#     #     data[start],data[end] = data[end],data[start]
#     #
#     # if data[middle+1] > data[end]:
#     #     data[middle+1],data[end] = data[end],data[middle+1]
#
#
# def merge_sort(start,end):
#     if start >= end:
#         return
#     m = (start+end) // 2
#     merge_sort(start,m)
#     merge_sort(m+1,end)
#     merge(start,m,end)

print(merge_sort(data))
print(cnt)
