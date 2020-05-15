from queue import Queue

class Printer:
	def __init__(self,ppm):
		self.page_rate=ppm
		self.currentTask=None
		self.timeRemaining=0

	def tick(self):
		if self.currentTask!=None:
			self.timeRemaining-=1
			if self.timeRemaining<=0:
				self.currentTask=None

	def busy(self):
		if self.currentTask!=None:
			return True
		else:
			return False

	def startNext(self,new_task):
		self.currentTask=new_task
		self.timeRemaining=new_task.getPages()*60/self.page_rate

import random

class Task:
	def __init__(self,timestamp):
		self.timestamp=timestamp
		self.pages=random.randrange(1,21)

	def getPages(self):
		return self.pages

	def getTimestamp(self):
		return self.timestamp

	def waitTime(self,current_time):
		return current_time-self.timestamp

def simulation(numSeconds,pages_per_minute):
	lab_printer=Printer(pages_per_minute)
	printing_queue=Queue()
	waiting_times=[]

	for current_second in range(numSeconds):
		
		if newPrintTask():
			#print("I am in")
			task=Task(current_second)
			printing_queue.enqueue(task)
		
		if((not lab_printer.busy()) and (not printing_queue.isEmpty())):
			next_task=printing_queue.dequeue()
			waiting_times.append(next_task.waitTime(current_second))
			lab_printer.startNext(next_task)
		lab_printer.tick()

	averageWait=sum(waiting_times)/(len(waiting_times))
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printing_queue.size()))

def newPrintTask():
	num=random.randrange(1,181)
	if num==180:
		return True
	else:
		return False

if __name__=="__main__":
	for i in range(10):
		simulation(3600,10)