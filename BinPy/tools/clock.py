import time
import threading

class Clock:
	def __init__(self, frequency=None, init_state=1, time_period=None, name=None):
		if time_period == None:
			self.time_period = 1.0/frequency
		if time_period==None and frequency==None:
			self.time_period = 1
		self.time_period = time_period
		self.init_state = init_state
		self.name = name
		self.curr_state = init_state
		self.details = {'time_period':self.time_period,'curr_state':self.curr_state}
		self.thread = myThread(self.details)
	
	def getTimePeriod(self):
		return self.time_period

	def getname(self):
		return self.name

	def getState(self):
		return self.thread.getState()

	def start(self):
		self.thread.start()

	def exit(self):
		self.thread.exit()


class myThread (threading.Thread):
	def __init__(self,details):
		threading.Thread.__init__(self)
		self.time_period = details['time_period']
		self.curr_state = details['curr_state']
		self.exitFlag = 0

	def run(self):
		self.main_func()

	def exit(self):
		self.exitFlag = 1

	def __toggleState(self):
		if self.curr_state==1:
			self.curr_state = 0
		else:
			self.curr_state = 1

	def main_func(self):
		while True:
			if self.exitFlag:
				thread.exit()
			time.sleep(self.time_period)
			try:
				self.__toggleState()
			except:
				pass

	def getState(self):
		return self.curr_state