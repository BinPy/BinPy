from BinPy.Gates import *


class Ground:

    """Models a Ground from which various connectors can tap by connecting to it.
    taps: The list of all connectors connected to this ground.
    connect(): Takes in one or more connectors as input and connects them to the ground.
    disconnect(): Takes in one or more connectors as input and disconnects them from the ground."""

    def __init__(self):
        self.taps = []

    def connect(self, *connectors):
        """Takes in one or more connectors as an input and taps to the ground."""
        for connector in connectors:
            if not isinstance(connector, Connector):
                raise Exception("Error: Input given is not a connector")
            else:
                if len(connector.connections['output']) != 0:
                    raise Exception(
                        "ERROR: The connector is already an output of some other object")
                self.taps.append(connector)
                connector.state = 0
                connector.tap(self, 'output')
                connector.trigger()

    def disconnect(self, *connectors):
        """Takes in one or more connectors as an input and disconnects them from the ground.
        A floating connector has a value of None.
        A message is printed if a specified connector is not already tapping from this ground."""

        for connector in connectors:
            if isinstance(connector, Connector):
                try:
                    self.taps.remove(connector)
                    connector.state = None
                    connector.connections['output'].remove(self)
                    connector.trigger()
                except:
                    print (
                        "The specified connector is not tapped to this ground")
            else:
                raise Exception("Error: Input given is not a connector")
