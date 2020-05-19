#Author- Aman Pandya
#Date- 11 May 2020
#Topic- Linked List, an important linear data structure

class Node:
	'''The following class implements the Node of a linked list. It has 2 parts- data and reference to next node.
	It has getter and setter methods for accessing and manipulating data and reference part  by external entites'''

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

class LinkedList:
	'''This following class implements a LinkedList using the Node class inside it. It has a start pointer pointing to the head of the linked list.
	It has a constructor, insert at Beginning, ending and before, after some element methods.
	It has methods to delete at beginning,ending, and before, after a particular element.
	It has count method to return the number of nodes in the list
	It has a search method to search a node in the list using linear search in O(n) time complexity and O(1) space complexity
	It has a traverse method to display all the nodes in the list
	It has a valueAtIndex method to get an element at a particular position
	'''

	def __init__(self):
		self.start=None
	
	def insertBegin(self,data):
		node=Node(data)
		node.next=self.start
		self.start=node
		
	def insertLast(self,data):
		node=Node(data)
		if self.start==None:
			self.start=node
		else:
			temp=self.start
			while(temp.getNext()!=None):
				temp=temp.getNext()
			temp.setNext(node)
	
	def valueAtIndex(self,index):
		if self.start==None:
			print("The LinkedList is empty")
		else:
			pos=0
			temp=self.start
			ans=None
			while(temp!=None):
				if pos==index:
					ans=temp.data
					break
				else:
					temp=temp.next
					pos+=1
			if ans==None:
				print("Index Exceed the list size")
			else:
				return ans

	def search(self,value):
		if self.start==None:
			print("The linked list is empty")
		else:
			temp=self.start
			pos=0
			ans=-1
			while(temp!=None):
				if(temp.data==value):
					ans=pos
					break
				else:
					temp=temp.next
					pos+=1
			return ans

	def insertBefore(self,data,before_what):
		node=Node(data)
		if self.start==None:
			self.start=node
		else:
			temp=self.start
			before=temp
			while(temp!=None):
				print(temp.getData())
				if(temp.getData()==before_what):
					before.next=node
					node.next=temp
					break
				before=temp
				temp=temp.next
		
	def insertAfter(self,data,after_what):
		node=Node(data)
		if self.start==None:
			self.start=node
		else:
			temp=self.start
			while(temp!=None and temp.getData()!=after_what):
				temp=temp.getNext()
				if temp!=None:
					print(temp.getData())
			if temp==None:
				print("That node doesn't exist in LinkedList")
			else:
				afternext=temp.next
				temp.next=node
				node.next=afternext

	def countNode(self):
		if self.start==None:
			return 0
		else:
			temp=self.start
			count=0
			while(temp!=None):
				count+=1
				temp=temp.getNext()
			return count
	
	def traverse(self):
		if self.start==None:
			print("Linked List is empty")
		else:
			temp=self.start
			while(temp!=None):
				print("%d"%temp.getData())
				temp=temp.getNext()
	

	def deleteFirst(self):
		if self.start==None:
			print("Linked List has 0 nodes")
		else:
			self.start=self.start.next
	
	def deleteLast(self):
		if self.start==None:
			print("Linked List has 0 nodes")
		else:
			temp=self.start
			before=temp
			while(temp.getNext()!=None):
				before=temp
				temp=temp.getNext()
			before.next=None

	def deleteAfter(self,after_data):
		if self.start==None:
			print("List is empty")
		else:
			temp=self.start
			while temp!=None:
				if temp.data==after_data:
					temp2=temp.next
					temp3=temp2.next
					temp.next=temp3
					break
				else:
					temp=temp.next

	def deleteBefore(self,before_data):
		if self.start==None:
			print("Linked list has 0 nodes")
		else:
			temp=self.start
			if temp.next==None or temp.data==before_data:
				print("No element before this")
			elif temp.next.data==before_data:
				self.start=temp.next
			else:
				a=temp
				b=temp.next
				c=b.next
				while(c!=None):
					if c.data==before_data:
						a.next=c
						break
					else:
						a=a.next
						b=b.next
						c=c.next
			
	def isEmpty(self):
		return self.head==None

	def deleteLinkedList(self):
		if self.start==None:
			print("Linked list is already empty")
		else:
			current=self.start
			while(current):
				prev=current.next
				del current.data
				current=prev
		self.start=None

	def countRecCall(self):
		if self.start==None:
			return 0
		else:
			return self.countRecursion(self.start)

	def countRecursion(self,node):
		if node==None:
			return 0
		else:
			return 1+self.countRecursion(node.next)

	def searchRecCall(self,item):
		if self.start==None:
			return "List empty"
		else:
			return self.searchRecursion(self.start,item)

	def searchRecursion(self,node,item):
		if node==None:
			return -1
		elif node.data==item:
			return "Found"
		else:
			return searchRecursion(node.next) 

	def nthNodeFromLast(self,n):
		if self.start==None:
			print("Linked List empty")
		else:
			temp=self.start
			reference=self.start
			index=0
			while(index<n):
				reference=reference.next
				index+=1
			while(reference!=None):
				reference=reference.next
				temp=temp.next
			return temp.data

	def delByValue(self,item):
		if self.start and self.start.data==item:
			self.start=self.start.next
			self.start=None
		else:
			prev=None
			cur_node=self.start
			while  cur_node and cur_node.data!=item:
				prev=cur_node
				cur_node=cur_node.next
			if cur_node is None:
				return
			prev.next=cur_node.next
			cur_node=None

if __name__=="__main__":
	LL=LinkedList()
	LL.insertLast(5)
	LL.insertLast(7)
	LL.insertLast(9)
	LL.insertLast(11)
	LL.insertLast(56)
	print(LL.countRecCall())
	LL.delByValue(7)
	#LL.deleteBefore(56)
	LL.traverse()
	#LL.deleteLinkedList()
	#LL.traverse()
	print(LL.countRecCall())
	print(LL.nthNodeFromLast(4))