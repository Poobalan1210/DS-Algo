'''This is the implementation of LinkedList only but according to what I studied
on Runestone academy. Here the Linked List items do not follow an arrangement,hence it is 
Unordered'''

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

	def getData(self):
		return self.data

	def setData(self,data):
		self.data=data

	def getNext(self):
		return self.next

	def setNext(self,next):
		self.next=next

class UnorderedList:
	def __init__(self):
		self.head=None

	def isEmpty(self):
		return self.head==None

	def add(self,new_data):
		new_node=Node(data)
		if self.head==None:
			self.head=new_node
		new_node.setNext(self.head)
		self.head=new_node

	def size(self):
		if self.head==None:
			return 0
		else:
			current=self.head
			count=0
			while(temp!=None):
				temp=temp.getNext()
				count+=1
			return count
