import thread
import time

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

	def getTimePeriod(self):
		return self.time_period

	def getInitialState(self):
		return self.init_state

	def getname(self):
		return self.name

	def getState(self):
		return self.curr_state

	def __toggleState(self):
		if self.curr_state==1:
			self.curr_state = 0
		else:
			self.curr_state = 1

	def main_func(self):
		while(True):
			time.sleep(self.time_period)
			self.__toggleState()

	def start(self):
		thread.start_new_thread(self.main_func, ())