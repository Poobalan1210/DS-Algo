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
		new_node=Node(new_data)
		if self.head==None:
			new_node.setNext(None)
			self.head=new_node
		else:
			new_node.setNext(self.head)
			self.head=new_node

	def size(self):
		if self.head==None:
			return 0
		else:
			temp=self.head
			count=0
			while(temp!=None):
				temp=temp.next
				count+=1
			return count

	def search(self,item):
		if self.head==None:
			return False
		else:
			temp=self.head
			found=False
			while(temp!=None and not found):
				if temp.getData()==item:
					found=True
					break
				temp=temp.getNext()
			return found

	def remove(self,item):
		if self.head==None:
			print("Unordered list empty")
		else:
			temp=self.head
			previous=None
			found=False
			while(not found):
				if temp.getData()==item:
					found=True
				else:
					previous=temp
					temp=temp.next
			if previous==None:
				self.head=temp.getNext()
			else:
				previous.setNext(temp.getNext())

	def index(self,item):
		if self.head==None:
			print("Unordered list empty")
		else:
			temp=self.head
			found=False
			index=0
			while(found==False and temp!=None):
				if temp.getData()==item:
					found=True
				else:
					temp=temp.getNext()
					index+=1
			if found==True:
				return index
			else:
				return -1

if __name__=="__main__":
	node_list=UnorderedList()
	print(node_list.isEmpty())
	print(node_list.size())
	print(node_list.search(1))
	node_list.add(4)
	node_list.add(3)
	node_list.add(2)
	node_list.add(1)
	print(node_list.index(2))
	print(node_list.isEmpty())
	print(node_list.size())
	print(node_list.search(1))
	node_list.remove(1)
