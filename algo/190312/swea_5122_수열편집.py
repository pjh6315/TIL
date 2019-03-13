import sys

sys.stdin = open('5122.txt')

t = int(input())

class Node:
    def __init__(self,data,pre=None,next=None):
        self.data = data
        self.pre = pre
        self.next = next

def enqueue(item):
    global head,rear
    new_node = Node(item)
    if head == None:
        head = new_node
    if rear == None:
        rear = new_node
        head.pre = rear
        rear.pre = head
        head.next = rear
        rear.next = head
    else:
        p = head
        q = rear


        q.next = new_node
        new_node.pre = q
        new_node.next = p
        p.pre = new_node

        rear = new_node

def insert(index,num):
    global head
    p = head

    for i in range(index):
        p = p.next

    new_node = Node(num)

    new_node.next = p
    new_node.pre = p.pre
    p.pre.next = new_node
    p.pre = new_node

    if index == 0:
        head = new_node

def delete(index):
    global head
    p = head

    for i in range(index):
        p = p.next

    p.pre.next = p.next
    p.next.pre = p.pre

    if index == 0:
        head = p.next

def change(index,num):
    global head
    p =head

    for i in range(index):
        p = p.next

    p.data = num

def ok(index):
    global head

    p = head
    for i in range(index):
        if p.next == head:
            if i != index-1:
                return False

        p = p.next
    return p.data

for tc in range(1,t+1):
    n,m,l = map(int,input().split())

    data = list(map(int,input().split()))

    head = None
    rear = None

    for i in range(n):
        enqueue(data[i])

    for i in range(m):
        data = input().split()

        if data[0] == 'I':
            insert(int(data[1]),int(data[2]))
        elif data[0] == 'D':
            delete(int(data[1]))
        else:
            change(int(data[1]),int(data[2]))

    # p = head
    # for i in range(10):
    #     print(p.data,end=' ')
    #     p=p.next
    # print()
    if ok(l):
        print('#%d %d' %(tc,ok(l)))
    else:
        print('#%d -1' %tc)