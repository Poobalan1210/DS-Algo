from SingleLinkedList import LinkedList 

def moveTail(linked_list):
	head=linked_list.getStart()
	prev=None
	curr=head
	while(curr.getNext()!=None):
		prev=curr
		curr=curr.getNext()
	curr.setNext(head)
	linked_list.setStart(curr)
	prev.setNext(None)

def main():
	L1=LinkedList()
	L1.createLinkedList([1,2,3,4,5,6])
	print("\n***Original Linked List***")
	L1.traverse()
	moveTail(L1)
	print("\n***Linked list after moving tail***")
	L1.traverse()

if __name__ == '__main__':
	main()