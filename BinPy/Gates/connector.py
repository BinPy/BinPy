class Connector:

    def __init__(self, state=None):
        self.connections = {"output": [], "input": []}
            # To store the all the taps onto this connection
        self.state = state  # To store the state of the connection
        self.oldstate = None

    def tap(self, element, mode):
        # Can't serve output for multiple devices
        if mode == "output":
            self.connections["output"] = []

        if element not in self.connections[mode]:
            self.connections[mode].append(
                element)  # Add an element to the connections list

    def untap(self, element, mode):
        if element in self.connections[mode]:
            self.connections[mode].remove(
                element)  # Delete an element from the connections list
        else:
            raise Exception(
                "ERROR:Connector is not the %s of the passed element" %
                mode)

    def isInputof(self, element):
        return element in self.connections["input"]

    def isOutputof(self, element):
        return element in self.connections["output"]

    # This function is called when the value of the connection changes
    def trigger(self):
        for i in self.connections["input"]:
            i.trigger()

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
        return 1 if self.state == 1 else 0

    def __repr__(self):
        return str(self.state)

    def __str__(self):
        return "Connector; State: " + str(self.state)
