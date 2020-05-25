class Node:
	def __init__(self,data=0):
		self.data=data
		self.next=None

class CircularLinkedList:
	def __init__(self):
		self.head=None

	def append(self,new_data):
		new_node=Node(new_data)
		if self.head==None:
			self.head=new_node
			new_node.next=self.head
		else:
			curr=self.head
			while curr.next!=self.head:
				curr=curr.next
			curr.next=new_node
			new_node.next=self.head

	def traverse(self):
		if self.head==None:
			print("CircularLinkedList empty")
		else:
			curr=self.head
			while True:
				print(curr.data,end=" ")
				curr=curr.next
				if curr==self.head:
					break

	def prepend(self,new_data):
		new_node=Node(new_data)
		if self.head==None:
			self.head=new_node
			new_node.next=self.head
		else:
			curr=self.head
			while curr.next!=self.head:
				curr=curr.next
			curr.next=new_node
			new_node.next=self.head
			self.head=new_node

if __name__=="__main__":
	CLL=CircularLinkedList()
	CLL.prepend(1)
	CLL.prepend(2)
	CLL.prepend(3)
	CLL.prepend(4)
	CLL.prepend(5)
	CLL.traverse()