from dequeue import Dequeue 

def checkPalindrome(input_string):
	dequeue=Dequeue()
	for character in input_string:
		dequeue.addRear(character)

	stillEqual=True
	while(dequeue.size()>1 and stillEqual):
		first=dequeue.delFront()
		last=dequeue.delRear()
		if first!=last:
			stillEqual=False
		
	return stillEqual

if __name__=="__main__":
	string=input()
	print(checkPalindrome(string))