class Queue:
	def __init__(self):
		self.items=[]

	def enqueue(self,data):
		self.items.insert(0,data)

	def dequeue(self):
		if self.items!=[]:
			return self.items.pop()
		else:
			return None

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items==[]

if __name__=="__main__":
	queue=Queue()
	print(queue.isEmpty())
	print(queue.size())
	queue.enqueue(1)
	queue.enqueue(2)
	print(queue.isEmpty())
	queue.enqueue(3)
	print(queue.size())
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())