class Connector:
    
    state = 0
    
    def __init__(self,state=0):
        self.connections = list() # To store the all the taps onto this connection
        self.state = state  # To store the state of the connection
        self.prev_state = 0
            
    def tap(self,element,mode):
        self.connections.append([element,mode]) # Add an element to the connections list

    #This fucntion is called when the value of the connection changes
    def trigger(self):
        
        if self.prev_state == self.state:
            #No Change in state... hence no need to trigger - This will avoid recursive triggering
            #When connector is used as a wire to loopback outputs. (Ex. in JKFlipFlop)
            #Avoids circular reference error.
            return
        
        for i in self.connections:
            if i[1] == 'input':
                i[0].trigger()        

        self.prev_state = self.state
    
    #Overloads the int method
    def __int__(self):
        return self.state
    
    #Overloads the bool() method
    def __nonzero__(self):
        return bool(self.state)
    
    #To return the state of the connector
    def __call__(self):
        return self.state
