class Connector:

	state = 0 # To store the state of the connection
	

	def __init__(self):
		self.connections = list() # To store the all the taps onto this connection

	def tap(self,element,mode):
		self.connections.append([element,mode]) # Add an element to the connections list
		
	#This fucntion is called when the value of the connection changes
	def trigger(self):

		for i in self.connections:
			if i[1] == 'input':
				i[0].trigger()
