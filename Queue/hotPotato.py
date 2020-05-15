from queue import Queue 

def hotPotato(namelist,count):
	#Creating the queue
	name_queue=Queue()
	for name in namelist:
		name_queue.enqueue(name)
	
	num_check=0
	print(name_queue.items)
	#applying the logic
	while name_queue.size()>1:
		for j in range(count):
			name_queue.enqueue(name_queue.dequeue())
			print(name_queue.items)
		print(name_queue.items)
		name_queue.dequeue()
		print(name_queue.items)
	return name_queue.dequeue()

if __name__=="__main__":
	n=int(input())
	namelist=[]
	for i in range(n):
		namelist.append(input())
	count=int(input())	
	winner=hotPotato(namelist,count)
	print(f"The winner of this contest is {winner}")