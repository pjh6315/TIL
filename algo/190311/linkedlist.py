class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
#
# node1.link= node2
# node2.link= node3
# node3.link= node4
# node4.link= node5
#
# head = node1
#
# p = head
#
# while p:
#     print(p.data)
#     p = p.link

def enqueue(item):
    global head
    new_node = Node(item)
    if head == None:
        head = new_node
    else:
        p = head
        while p.link:
            p = p.link
        p.link = new_node


def pri_queue(item):
    global head
    new_node = Node(item)
    if head == None:
        head = new_node
    else:
        p = head
        while True:
            if p.link == None:
                p.link = new_node
                break
            elif p.link.data < item:
                p = p.link
            elif p.link.data >= item:
                temp = p.link
                p.link = new_node
                p.link.link = temp
                break



head = None



# enqueue(1)
# enqueue(5)
# enqueue(2)
# enqueue(4)
# enqueue(3)

pri_queue(1)
pri_queue(5)
pri_queue(2)
pri_queue(4)
pri_queue(3)

p = head

while p:
    print(p.data)
    p = p.link