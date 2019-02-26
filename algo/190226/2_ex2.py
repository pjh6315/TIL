queue = [i for i in range(1,42)]
print(queue)

front = 0
rear = 40

while len(queue) > 2 :
	queue.append(queue.pop(0))
	queue.append(queue.pop(0))
	queue.pop(0)

print(queue)


queue = [0] * 1000

for i in range(1,42):
	queue[i-1] = i

print(queue)

front = 0
rear = 40
while rear - front > 1 :
	rear +=1
	queue[rear] = queue[front]
	front +=1

	rear += 1
	queue[rear] = queue[front]
	front += 1

	front += 1

print(queue[front])
print(queue[rear])
print(queue)

