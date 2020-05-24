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

	def getStart(self):
		return self.start
		
	def createLinkedList(self,node_list):
		for key in node_list:
			self.insertLast(key)
	
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

	def nthNodeLast2ndAlgo(self,n):
		if self.start==None:
			print("LinkedList empty")
		else:
			index=self.countRecCall()
			curr=self.start
			while(curr!=None):
				if index==n:
					break
				else:
					curr=curr.next
					index-=1
			if curr==None:
				return
			else:
				return curr.data 

	def delByValue(self,item):
		if self.start and self.start.data==item:
			self.start=self.start.next
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

	def removeDuplicates(self):
		cur=self.start
		prev=None
		dup_values=dict()
		while(cur!=None):
			if cur.data in dup_values:
				prev.next=cur.next
				cur=None
			else:
				dup_values[cur.data]=1
				prev=cur
			cur=prev.next

	def delByPosition(self,pos):
		if self.start and pos==0:
			self.start=self.start.next
		else:
			prev=None
			cur_node=self.start
			index=0
			while cur_node and index!=pos:
				prev=cur_node
				cur_node=cur_node.next
				index+=1
			if cur_node is None:
				return
			prev.next=cur_node.next
			cur_node=None

	def swapNodes(self,key1,key2):
		if key1==key2:
			return
		
		prev1=None
		curr1=self.start
		while curr1 and curr1.data!=key1:
			prev1=curr1
			curr1=curr1.next
		
		prev2=None
		curr2=self.start
		while curr2 and curr2.data!=key2:
			prev2=curr2
			curr2=curr2.next

		if not curr1 or not curr2:
			return

		if prev1:
			prev1.next=curr2
		else:
			self.start=curr2

		if prev2:
			prev2.next=curr1
		else:
			self.start=curr1

		curr1.next, curr2.next=curr2.next,curr1.next

	def reverse(self):
		if self.start==None:
			return
		else:
			prev=None
			curr=self.start
			while curr:
				temp=curr.next
				curr.next=prev
				prev=curr
				curr=temp
			self.start=prev

	def reverse_recursive(self):

		def _reverse_recursive(prev,curr):
			if not curr:
				return prev
			temp=curr.next
			curr.next=prev
			prev=curr
			curr=temp
			return _reverse_recursive(prev,curr)

		self.start=_reverse_recursive(prev=None,curr=self.start)

	def rotateByVal(self,pivot):
		if self.start==None:
			print("Linked List empty")
		else:
			curr=self.start
			pivot_node=None
			while(curr.getNext()!=None):
				if curr.getData()==pivot:
					pivot_node=curr
				curr=curr.getNext()
			curr.setNext(self.start)
			self.start=pivot_node.getNext()
			pivot_node.next=None

	def rotateByPos(self,pos):
		if self.start and self.start.next:
			p=self.start
			q=self.start
			prev=None
			count=0

			while p and count<pos:
				prev=p
				p=p.getNext()
				q=q.getNext()
				count+=1
			p=prev

			while q:
				prev=q
				q=q.getNext()
			q=prev

			q.setNext(self.start)
			self.start=p.getNext()
			p.setNext(None)

	def isPalindrome1(self):
		s=""
		curr=self.start
		while(curr!=None):
			s+=str(curr.getData())
			curr=curr.getNext()
		return s==s[::-1]

	def isPalindrome2(self):
		stack_list=[]
		curr=self.start
		while(curr!=None):
			stack_list.append(curr.getData())
			curr=curr.getNext()

		curr=self.start
		isPalindrome=True
		while(curr!=None and isPalindrome):
			item=stack_list.pop()
			if curr.getData()!=item:
				isPalindrome=False
				break
			curr=curr.getNext()
		
		return isPalindrome

	def isPalindrome3(self):
		if self.start:
			p=self.start
			q=self.start
			prev=[]

			i=0
			while q:
				prev.append(q)
				q=q.getNext()
				i+=1
			q=prev[i-1]

			count=1
			while count<=i//2+1:
			 	if prev[-count].getData()!=p.getData():
			 		return False
			 	count+=1
			 	p=p.getNext()
			return True
		else:
			return True

if __name__=="__main__":
	LL=LinkedList()
	LL.createLinkedList([1,2,3,2,1])
	print("\n***Traversing LL***")
	LL.traverse()
	print(LL.isPalindrome1())
	print(LL.isPalindrome2())
	print(LL.isPalindrome3())