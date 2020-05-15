class Stack:
	def __init__(self):
		self.items=[]
	
	def push(self,item):
		self.items.append(item)

	def isEmpty(self):
		return self.items==[]
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class StackReverse:
	def __init__(self):
		self.items=[]
	
	def push(self,item):
		self.items.insert(0,item)

	def isEmpty(self):
		return self.items==[]
	
	def pop(self):
		return self.items.pop(0)
	
	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

if __name__=="__main__":
	stk1=Stack()
	print(stk1.isEmpty())
	stk1.push(3)
	stk1.push(9)
	print(stk1.pop())
	print(stk1.peek())
	print(stk1.size())
	print(stk1.isEmpty())
	stk2=Stack()
	print(stk2.isEmpty())
	stk2.push(3)
	stk2.push(9)
	print(stk2.pop())
	print(stk2.peek())
	print(stk2.size())
	print(stk2.isEmpty())