class Node:
	def __init__(self,data,prev=None,next=None):
		self.data=data
		self.prev=prev
		self.next=next

class DoublyLinkedList:
	def __init__(self):
		self.head=None

	def insertFront(self,new_data):
		new_node=Node(new_data)
		new_node.prev=None
		new_node.next=self.head

		if self.head is not None:
			self.head.prev=new_node

		self.head=new_node

	def insertEnd(self,new_data):
		new_node=Node(new_data)
		new_node.prev=None
		new_node.next=None

		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while temp.next!=None:
				temp=temp.next
			temp.next=new_node
			new_node.prev=temp

		
	def insertAfter(self,after_what,new_data):
		new_node=Node(new_data)
		if self.head==None:
			print("The after node doesn't exist")
		else:
			temp=self.head
			while(temp!=None and temp.data!=after_what):
				temp=temp.next
			if temp==None:
				print("after node doesn't exist")
			elif temp.next==None:
				self.insertEnd(new_data)
			else:
				new_node.next=temp.next
				new_node.prev=temp
				temp.next.prev=new_node
				temp.next=new_node

	def insertBefore(self,before_what,new_data):
		new_node=Node(new_data)
		if self.head==None:
			print("Linked List is empty")
		elif self.head.data==before_what:
			self.insertFront(new_data)
		else:
			temp=self.head
			while(temp!=None and temp.data!=before_what):
				temp=temp.next
			if temp==None:
				print("before node doesn't exist")
			else:
				new_node.prev=temp.prev
				temp.prev.next=new_node
				new_node.next=temp
				temp.prev=new_node

	def count(self):
		if self.head==0:
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
			print("DoublyLinkedList empty")
		else:
			index=0
			temp=self.head
			found=False
			while(temp and not found):
				if(temp.data==item):
					found=True
					break
				temp=temp.next
				index+=1
			if found==True:
				return index
			else:
				return -1

	def searchByPos(self,pos):
		if self.head==None:
			print("DoublyLinkedList empty")
		else:
			temp=self.head
			index=0
			found=False
			while(temp and not found):
				if(index==pos):
					found=True
					break
				temp=temp.next
				index+=1
			if found==True:
				return temp.data
			else:
				return "Position greater than length of list"

	def deleteFront(self):
		if self.head==None:
			print("DoublyLinkedList empty")
		elif self.head.next==None:
			self.head=None
		else:
			self.head=self.head.next
			self.head.prev=None

	def deleteEnd(self):
		if self.head==None:
			print("DoublyLinkedList empty")
		elif self.head.next==None:
			self.head=None
		else:
			temp=self.head
			while(temp.next.next!=None):
				temp=temp.next
			temp.next=None

	def deleteBefore(self,before_what):
		if self.head==None:
			print("DoublyLinkedList empty")
		elif self.head.data==before_what:
			print("No element before this node")
		elif self.head.next.data==before_what:
			self.head=self.head.next
			self.head.prev=None
		else:
			temp=self.head
			while(temp!=None and temp.data!=before_what):
				temp=temp.next
			#print(temp.prev.data)
			if temp==None:
				print("before node not present")
			else:
				previous=temp.prev.prev
				previous.next=temp
				temp.prev=previous

	def deleteAfter(self,after_what):
		if self.head==None:
			print("DoublyLinkedList empty")
		else:
			temp=self.head
			while(temp!=None and temp.data!=after_what):
				temp=temp.next
			if temp==None:
				print("after node doesn't present")
			elif temp.next==None:
				print("No node present to delete")
			elif temp.next.next==None:
				temp.next=None
			else:
				super_next=temp.next.next
				super_next.prev=temp
				temp.next=super_next

	def traverse(self):
		if self.head==None:
			print("DoublyLinkedList empty")
		else:
			temp=self.head
			while(temp!=None):
				print(temp.data,sep=" ")
				temp=temp.next

if __name__=="__main__":
	DLL=DoublyLinkedList()
	#DLL.insertFront(0)


	#DLL.insertBefore(0,1)
	#DLL.insertBefore(0,2)
	#DLL.insertBefore(3,8)
	#DLL.traverse()
	#DLL.count()
	
	DLL.insertEnd(0)
	DLL.insertAfter(0,1)
	DLL.insertAfter(0,2)
	DLL.insertAfter(2,3)
	#DLL.insertAfter(4,5)
	DLL.traverse()
	#print(DLL.count())
	
	#DLL.deleteFront()
	#DLL.deleteEnd()
	#DLL.deleteBefore(0)
	#DLL.deleteBefore(1)
	#DLL.deleteBefore(1)
	#DLL.deleteBefore(7)
	#DLL.traverse()
	
	#DLL.deleteAfter(0)
	#DLL.deleteAfter(1)
	#DLL.deleteAfter(7)
	#DLL.traverse()
	print("---------------")
	print(DLL.search(3))
	print(DLL.searchByPos(3))
	print(DLL.search(5))
	print(DLL.searchByPos(7))