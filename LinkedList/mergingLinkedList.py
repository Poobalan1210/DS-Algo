from SingleLinkedList import LinkedList 

def mergeLinkedList(curr1,curr2):

	L3=LinkedList()
	while(curr1!=None and curr2!=None):
		
		if curr1.data<=curr2.data:
			L3.insertLast(curr1.data)
			curr1=curr1.getNext()

		else:
			L3.insertLast(curr2.data)
			curr2=curr2.getNext()

	while(curr1!=None):
		L3.insertLast(curr1.data)
		curr1=curr1.getNext()

	while(curr2!=None):
		L3.insertLast(curr2.data)
		curr2=curr2.getNext()

	return L3

if __name__=="__main__":
	L1=LinkedList()
	L1.createLinkedList([1,6,16,28,67])
	print("\n***Traversing L1***")
	L1.traverse()
	L2=LinkedList()
	L2.createLinkedList([3,8,56,68,678])
	print("\n***Traversing L2***")
	L2.traverse()
	L3=mergeLinkedList(L1.getStart(),L2.getStart())
	print("\n***Traversing L3***")
	L3.traverse()
