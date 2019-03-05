def preorder_traverse(now):
    print(now,end=' ')
    if l_child[now] != 0:
        preorder_traverse(l_child[now])
    if r_child[now] != 0:
        preorder_traverse(r_child[now])

    return


def inorder_traverse(now):
    if l_child[now] != 0:
        inorder_traverse(l_child[now])
    print(now, end=' ')
    if r_child[now] != 0:
        inorder_traverse(r_child[now])

    return


def postorder_traverse(now):
    if l_child[now] != 0:
        inorder_traverse(l_child[now])

    if r_child[now] != 0:
        inorder_traverse(r_child[now])

    print(now, end=' ')
    return

n = 13

data = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
l_child = [0 for i in range(n+1)]
r_child = [0 for i in range(n+1)]
parents = [0 for i in range(n+1)]
child = [0 for i in range(n+1)]
level = [0 for i in range(n+1)]

for i in range(0,len(data),2):
    start = data[i]
    end = data[i+1]
    # if end % 2 :
    #     r_child[start] = end
    # else:
    #     l_child[start] = end

    if l_child[start] == 0:
        l_child[start] = end
    else:
        r_child[start] = end


    parents[end] = start
    child[start] += 1
    level[end] = level[start] + 1

# print(l_child)
# print(r_child)
# print(child)
# print(parents)
# print(level)
print('전위순회: ',end='')
preorder_traverse(1)
print()
print('중위순회: ',end='')
inorder_traverse(1)
print()
print('후위순회: ',end='')
postorder_traverse(1)
print()


# for i in range(1,14):
#     print('%d 의 l_child : %d r_child : %d 자녀수: %d 부모: %d level: %d' %(i,l_child[i],r_child[i],child[i],parents[i],level[i]))
