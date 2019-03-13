import sys

sys.stdin = open('5108.txt')

class Node:
    def __init__(self,data,pre=None,next=None):
        self.data = data
        self.pre = pre
        self.next = next


def enqueue(item):
    global head
    new_node = Node(item)
    if head == None:
        head = new_node
    else:
        p = head
        while p.next:
            p = p.next
        p.next = new_node
        new_node.pre = p


def insert(index,num):
    global head
    new_node = Node(num)
    p = head
    if index == 0:
        new_node.pre = head.pre
        head.pre = new_node
        new_node.next = head
        head = new_node

    else:
        for i in range(index):
            p = p.next

        new_node.pre = p.pre
        p.pre.next = new_node
        p.pre = new_node
        new_node.next = p

t= int(input())

for tc in range(1,t+1):
    n,m,l = map(int,input().split())
    data = list(map(int,input().split()))

    head = None

    # for index in range(n):
    #     print('%d -> %d -> %d' % (data[index].pre.data, data[index].data, data[index].next.data))

    for k in data:
        enqueue(k)



    for i in range(m):
        index, num = map(int,input().split())
        insert(index,num)

    p = head

    for i in range(l):
        p = p.next

    print('#%d %d' %(tc,p.data))
