class Connector:

    def __init__(self,state = None):
        self.connections = {'output': [], 'input': []} # To store the all the taps onto this connection
        self.state = state  # To store the state of the connection

    def tap(self,element,mode):
        self.connections[mode].append(element) # Add an element to the connections list

    #This function is called when the value of the connection changes
    def trigger(self):
        for i in self.connections['input']:
            i.trigger()

    def __call__(self):
        return self.state