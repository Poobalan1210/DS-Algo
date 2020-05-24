from SingleLinkedList import LinkedList

def removeDuplicates(L1):
	search_table={}
	curr=L1.getStart()
	index=0
	while(curr!=None):
		if curr.data in search_table:
			L1.delByPosition(index)
			curr=curr.getNext()
		else:
			search_table[curr.data]=1
			index+=1
			curr=curr.getNext()
	return L1

if __name__=="__main__":
	L1=LinkedList()
	L1.createLinkedList([1,2,3,5,2,7,3,2,1,7])
	print("\n***Traversing Duplicates containing L1***")
	L1.traverse()
	L1=removeDuplicates(L1)
	print("\n***Traversing Duplicates removed L1***")
	L1.traverse()
