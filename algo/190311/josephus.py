class Node:
    def __init__(self,data,pre=None,next=None):
        self.data = data
        self.pre = pre
        self.next = next


data = [0 for i in range(41)]

for i in range(41):
    data[i] = Node(i+1)

for i in range(41):
    data[i].next = data[(i+1)%41]
    data[i].pre = data[i-1]




# for index in range(41):
#     print('%d -> %d -> %d' %(data[index].pre.data,data[index].data,data[index].next.data))

p = data[2]

while p.pre.data != p.next.data:
    temp_pre = p.pre
    p = p.next
    p.pre = temp_pre
    temp_pre.next = p

    p = p.next.next





print(p.data,p.next.data,p.next.next.data)

