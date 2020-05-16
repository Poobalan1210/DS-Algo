class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

	def setData(self,data):
		self.data=data

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self,next):
		self.next=next

class OrderedList:
	def __init__(self):
		self.head=None
		
	def add(self,new_data):
		new_node=Node(new_data)
		current=self.head
		previous=None
		stop=False
		while current!=None and not stop:
			if current.getData()>new_data:
				stop=True
			else:
				previous=current
				current=current.getNext()
		if previous==None:
			new_node.setNext(self.head)
			self.head=new_node
		else:
			new_node.setNext(previous.getNext())
			previous.setNext(new_node)

	def traverse(self):
		if self.head==None:
			print("OrderedList empty")
		else:
			current=self.head
			while(current!=None):
				print(current.getData())
				current=current.getNext()

	def remove(self,item):
		if self.head==None:
			print("OrderedList empty")
		else:
			current=self.head
			previous=None
			found=False
			while(not found):
				previous=current
				if current.getData()==item:
					found=True
					break
				current=current.getNext()
			if current==self.head:
				self.head=current.getNext()
			else:
				previous.setNext(current.getNext())

	def search(self,item):
		if self.head==None:
			print("OrderedList empty")
		else:
			current=self.head
			while(current!=None):
				if current.getData()==item:
					return True
				elif current.getData()>item:
					return False
				else:
					current=current.getNext()
			return False

	def isEmpty(self):
		return self.head==None

	def size(self):
		if self.head==None:
			return 0
		else:
			current=self.head
			count=0
			while(current!=None):
				current=current.getNext()
				count+=1
			return count

	def index(self,new_data):
		if self.head==None:
			return "OrderedList empty"
		else:
			current=self.head
			index=0
			while(current.getData()!=new_data):
				current=current.getNext()
				index+=1
			return index

	def pop(self,pos=-1):
		if pos==-1:
			pos=self.size()-1
		if self.head==None:
			print("OrderedList empty")
		else:
			previous=None
			current=self.head
			index=0
			while(index!=pos):
				index+=1
				previous=current
				current=current.getNext()
			ans=current.getData()
			if previous==None:
				self.head=current.getNext()
			else:
				previous.setNext(current.getNext())
			return ans

if __name__=="__main__":
	order_list=OrderedList()
	print(order_list.isEmpty())
	print("Popped element: ",order_list.pop())
	order_list.add(1)
	order_list.add(-5)
	order_list.remove(-5)
	order_list.add(88)
	order_list.add(0)
	order_list.add(12)
	print("Traversing on---------------")
	order_list.traverse()
	print("Traversing done-------------")
	print("Popped element: ",order_list.pop())
	print("Popped element: ",order_list.pop(1))
	print("Search Result: ",order_list.search(1))
	print("Size of list: ",order_list.size())
	print(order_list.isEmpty())