class Node:
	'''
	Creating a Linked List node
	'''

	def __init__(self,data=0):
		self.data=data
		self.next=None

class CircularLinkedList:
	'''
	This class implements a Circular Linked List in which the last 
	node points back to the head of the list
	'''

	def __init__(self):
		self.head=None

    #Method to add a node at the end of the Circular Linked List
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

    #Method to print all the nodes of the Circular Linked List
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

    #Method to add a node at the front of the Circular Linked List
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

 
 	# Method to remove any node whose data part matches with deletion
	# key from the Circular Linked List
	def remove(self,deletion_key):
		if self.head==None:
			print("CircularLinkedList empty")
		else:
			#Logic to check where deletion key is present
			curr=self.head
			prev=None
			while curr.next!=self.head:
				if curr.data==deletion_key:
					key_found=True
					break
				prev=curr
				curr=curr.next

			'''
			Checking if the deletion key matches with the head node and
			if matches delete it
			'''
			if prev==None:
				if self.head==self.head.next:
					self.head=None
				else:
					temp=self.head
					while temp.next!=self.head:
						temp=temp.next
					temp.next=curr.next
					self.head=temp.next
			else:
				prev.next=curr.next

	def __len__(self):
		if self.head==None:
			return 0
		else:
			count=1
			curr=self.head
			while curr.next!=self.head:
				curr=curr.next
				count+=1
			return count

	def split_list(self):
		length=len(self)
		if length==0:
			return None
		if length==1:
			return self.head
		
		curr=self.head
		prev=None
		current_length=0
		while curr and current_length<length//2:
			prev=curr
			curr=curr.next
			current_length+=1
		prev.next=self.head

		split_clist=CircularLinkedList()
		head2=curr
		while curr.next!=self.head:
			split_clist.append(curr.data)
			curr=curr.next
		split_clist.append(curr.data)

		self.traverse()
		print("\n")
		split_clist.traverse()

if __name__=="__main__":
	CLL=CircularLinkedList()
	CLL.prepend(1)
	CLL.prepend(2)
	CLL.prepend(3)
	CLL.prepend(4)
	#CLL.prepend(5)
	CLL.traverse()
	print("\n")
	CLL.split_list()