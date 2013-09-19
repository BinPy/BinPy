import sys
import time
import threading
from BinPy import Gates
class Clock(threading.Thread):
	"""
	This class uses threading technique to create a clock with a certain time interval.
	This is how you can create a clock with this class:

	>>> myClock = Clock(0,time_period=2,name="My First Clock")
	>>> myClock.start()		#Do not call run method
	>>> myClock.getState()
	0
	
	Note: Once you are done with the clock, use myClock.kill() to kill the clock.
		  Running too many clocks will unnecessarily overload the CPU. 
	
	Following are the parameters of the class

	frequency:		It will decide time interval of the clock, use SI unit i.e. Heartz
	time_period:	It will also decide time interval of the clock, use SI unit i.e. second

	If time_period and frequency both have been provided, then time_period will override frequency
	If nothing is provided, then it will set time_period = 1s by default

	init_state:		It is the initial state of the clock(1 by default)
	name:			It is the name of the clock.(optional)
	
	Methods :	start(), getState(), setState(value), getName(), getTimePeriod(), kill()

	"""
	def __init__(self, init_state=1, frequency=None, time_period=None, name=None):
		threading.Thread.__init__(self)
		if frequency != None:
			self.time_period = 1.0/frequency
		if time_period != None:
			self.time_period = time_period
		if time_period==None and frequency==None:
			self.time_period = 1

		self.init_state = init_state
		self.name = name
		self.curr_state = init_state
		self.exitFlag = 0
		self.daemon = True

	def __toggleState(self):
		"""
		This is an internal method to toggle the state of the output
		"""
		if self.curr_state==1:
			self.curr_state = 0
		else:
			self.curr_state = 1

	def __main_func(self):
		while True:
			if self.exitFlag:
				thread.exit()
			time.sleep(self.time_period)
			try:
				self.__toggleState()
			except:
				pass

	def getState(self):
		"""
		Returns the current state of the clock
		"""
		return self.curr_state

	def setState(self,value):
		"""
		Resets the state of the clock to the passed value
		"""
		if self.curr_state == value: return
		self.curr_state = value

	def getTimePeriod(self):
		"""
		Returns the time period of the clock
		"""
		return self.time_period

	def getName(self):
		"""
		Returns the name of the clock
		"""
		return self.name

	def kill(self):
		"""
		Kills the clock(Thread)
		"""
		self.exitFlag = 1

	def run(self):
		self.__main_func()


class DigitDisplay:
	def __init__(self,name=None):
		self.name = name
		self.gates = Gates()

	def set(self,pin_conf):
		if len(pin_conf)!=10:
			if len(pin_conf)!=7:
				raise Exception("There must be 10 or 7 values")
		if len(pin_conf)==10:
			vcc = self.gates.OR(pin_conf[2],pin_conf[7])
			a = pin_conf[6]
			b = pin_conf[5]
			c = pin_conf[3]
			d = pin_conf[1]
			e = pin_conf[0]
			f = pin_conf[8]
			g = pin_conf[9]
		if len(pin_conf)==7:
			a = pin_conf[0]
			b = pin_conf[1]
			c = pin_conf[2]
			d = pin_conf[3]
			e = pin_conf[4]
			f = pin_conf[5]
			g = pin_conf[6]
			vcc=1			
		if vcc:
			test = [a, b, c, d, e, f, g]
			data = {'0':[1,1,1,1,1,1,0],'1':[0,1,0,0,0,0,0],'2':[1,1,0,1,1,0,1],\
			'3':[1,1,1,1,0,0,1],'4':[0,1,1,0,0,1,1],'5':[1,0,1,1,0,1,1],'6':[1,0,1,1,1,1,1],\
			'7':[1,1,1,0,0,0,0],'8':[1,1,1,1,1,1,1],'9':[1,1,1,1,0,1,1]}
			for i in data:
				if test==data[i]:
					return int(i)
			return None
		else:
			return None