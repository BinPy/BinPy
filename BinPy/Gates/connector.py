class Connector:

    state = None  # To store the state of the connection

    def __init__(self):
        # To store the all the taps onto this connection
        self.connections = {'output': [], 'input': []}

    def tap(self, element, mode):
        # Add an element to the connections list
        self.connections[mode].append(element)

    # This function is called when the value of the connection changes
    def trigger(self):
        for i in self.connections['input']:
            i.trigger()
