class Connector:

    def __init__(self, state=3):
        validate_state(state)
        self.connections = {"output": [], "input": []}
            # To store all the taps onto this connection
        self.state = state  # To store the state of the connection
        self.oldstate = None

    def tap(self, element, mode):
        if element not in self.connections[mode]:
            self.connections[mode].append(
                element)  # Add an element to the connections list

    # This function is called when the value of the connection changes
    def trigger(self):
        for i in self.connections["input"]:
            i.trigger()

    def set(self, state):
        """
        Allows to easily change the state of the connector, as long as no output
        is connected to it, since that could create a conflict. Example of usage:
        >>> c = Connector(0)
        >>> c.set(1)
        """
        if self.connections["output"]:
            raise Exception("No 'output' connections allowed")
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