class Connector:

    def __init__(self, state=3, name=''):
        validate_state(state)
        self.connections = {"output": [], "input": []}
            # To store all the taps onto this connection
        self.state = state  # To store the state of the connection
        self.name = name
        self.oldstate = None

    def tap(self, element, mode):
        if element not in self.connections[mode]:
            self.connections[mode].append(
                element)  # Add an element to the connections list
        if self not in element.inputs and self != element.output:
            if mode == 'input':
                element.connect(element.output, element.inputs + self)
            elif mode == 'output':
                element.connect(self, element.inputs)


    # This function is called when the value of the connection changes
    def trigger(self):
        outputs = self.connections['output']
        if 3 in outputs:
            self.state = 3
        elif 1 in outputs and 0 in outputs:
            self.state = 3
        elif 1 in outputs and self.state == 0:
            self.state = 3
        elif 0 in outputs and self.state == 1:
            self.state = 3
        for i in self.connections["input"]:
            i.trigger()

    def set(self, state):
        validate_state(state)
        self.state = state
        self.trigger()

    def __call__(self):
        return self.state

    # Overloads the bool method
    # For python3
    def __bool__(self):
        return True if self.state == 1 else False

    # To be compatible with Python 2.x
    __nonzero__ = __bool__

    # Overloads the int() method
    def __int__(self):
        return self.state


# States: 0, 1, Hi-Z, undefined
def validate_state(state):
    if state not in (0,1,2,3):
        raise Exception("Invalid state.")

def is_connector(*connectors):
    for i in connectors:
        if not isinstance(i, Connector):
            raise Exception("Connector Class instance/s expected")