from queue import queue

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

	def newTask(self,new_task):
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

