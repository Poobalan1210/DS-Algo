class Dequeue:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	def size(self):
		return len(self.items)

	def addFront(self,data):
		self.items.append(data)

	def addRear(self,data):
		self.items.insert(0,data)

	def delFront(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			return "Dequeue empty"

	def delRear(self):
		if not self.isEmpty():
			return self.items.pop(0)
		else:
			return "Dequeue empty"

if __name__=="__main__":
	dequeue=Dequeue()
	print(dequeue.isEmpty())
	print(dequeue.size())
	dequeue.addFront(1)
	dequeue.addRear(2)
	dequeue.addFront(3)
	dequeue.addRear(4)
	dequeue.addRear(5)
	print(dequeue.delFront())
	print(dequeue.delRear())
	print(dequeue.size())
	print(dequeue.isEmpty())