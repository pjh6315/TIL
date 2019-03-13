import sys

sys.stdin = open('5110.txt')

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
        head.pre = new_node


t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    head = None
    data = []


    for i in range(m):
        data.append(list(map(int,input().split())))

    for i in range(m):

        num_list = data[i]

        if i == 0:
            for num in num_list:
                enqueue(num)

        else:
            compare = num_list[0]
            p = head

            if p.data > compare:
                for i in range(len(num_list)):
                    new_node = Node(num_list[i])
                    if i == 0:
                        new_node.next = p
                        head = new_node
                        p = head
                    else:
                        new_node.next = p.next
                        p.next = new_node
                        p=p.next

            else:
                while p.next != None and p.next.data <= compare:
                    p = p.next

                for num in num_list:
                    new_node = Node(num)
                    new_node.next = p.next
                    new_node.pre = p.pre
                    # if p.next:
                    #     p.next.pre= new_node
                    p.next = new_node

                    p = p.next

   

    p = head

    result = []
    for i in range(n*m - 10):
        p = p.next

    for i in range(10):
        result.append(p.data)
        p=p.next
    result.reverse()

    print('#%d' %tc , end=' ')
    print(*result)




