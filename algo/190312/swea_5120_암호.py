import sys

sys.stdin = open('5120.txt')


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





for tc in range(1,t+1):
    n,m,k = map(int,input().split())

    data = list(map(int,input().split()))

    head = None
    rear = None

    for num in data:
        enqueue(num)

    p = head

    for i in range(k):
        for j in range(m):
            p=p.next

        temp_node = Node(p.pre.data + p.data)
        temp_node.pre = p.pre
        temp_node.next = p
        p.pre.next = temp_node
        p.pre = temp_node

        if p.pre == head:
            head = temp_node
        if p.pre == rear:
            rear = temp_node

        p = p.pre

        # print(temp_node.pre.data,temp_node.data,temp_node.next.data)

    p = head
    print('#%d' %tc, end='')
    cnt = 0

    for i in range(10):
        p = p.pre
        if i == 0:
            print(' %d' % p.data, end='')
        elif p == head.pre:
            break
        else:
            print(' %d' %p.data,end='')


    print()