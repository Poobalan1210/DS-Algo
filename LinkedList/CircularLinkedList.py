class Node:
	def __init__(self,data=0):
		self.data=data
		self.next=None

class CircularLinkedList:
	def __init__(self):
		self.head=None

	def insertLast(self,new_data):
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

if __name__=="__main__":
	CLL=CircularLinkedList()
	CLL.insertLast(1)
	CLL.insertLast(2)
	CLL.insertLast(3)
	CLL.insertLast(4)
	CLL.insertLast(5)
	CLL.traverse()