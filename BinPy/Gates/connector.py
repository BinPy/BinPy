class Connector:
        ''' Connector is analogous to wire (in VHDL)
        Can have three states: 1 (True), 0 (False), None (High Impedance State)
        Can get an output from more than one logic objects. A warning is printed when there is a logic contention
        Can provide input to more than one logic objects.'''

	state = None # To store the state of the connector
	
	def __init__(self):
		self.input_to = list() # To store all the objects to which this connector is an input
		self.output_of = list() # To store all the objects to which this connector is an output

	def tap(self,element,mode):
                if (mode == 'input'):
                        self.input_to.append(element)
                else if (mode == 'output'):
                        self.output_of.append(element)
		
	#This fucntion is called when the value of the connection changes
	def trigger(self):

		for i in self.input_to:
                        i.trigger()
