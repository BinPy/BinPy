import sys
import time
import threading
from BinPy import Connector


class Multivibrator(threading.Thread):

    """
    This class uses threading technique to create a multivibrator with a certain time period.
    USAGE:
        >>> m1 = Multivibrator()
        >>> m1.start()     # Start this thread
        >>> m1.trigger()   # or m1()
        >>> m1.getState()  # or m1.A.state
        0
        >>> m1.setMode(2)
        >>> m1.trigger()
        >>> m1.getstate()
        >>> conn = Connector()
        >>> m1.setOutput(conn) # To set the output to connector conn
        >>> conn()             # Retrieves the current state

    Note: Once you are done with the multivibrator, use m1.kill() to kill the Multivibrators.
        >>> m1.kill()

    Following are the parameters of the class

        frequency:      It will decide time interval of the Multivibrator, use SI unit i.e. Hertz
        time_period:    It will also decide time interval of the Multivibrator, use SI unit i.e. second

        If time_period and frequency both have been provided, then time_period will override frequency
        If nothing is provided, then it will set time_period = 1s by default

        init_state:     It is the initial state of the multivibrator(1 by default)

        mode:           It is the mode of operation.
                        1 --> Monostable
                        2 --> Astable
                        3 --> Bistable

    Methods :   trigger(),setMode(), getState(), setState(value), getTimePeriod(), kill(), stop(), setOutput()
    """

    def __init__(
            self,
            init_state=1,
            mode=1,
            frequency=None,
            time_period=None,
            on_time=None,
            off_time=None):

        threading.Thread.__init__(self)

        if frequency is not None:
            self.time_period = 1.0 / frequency
        if time_period is not None:
            self.time_period = time_period
        if time_period is None and frequency is None:
            self.time_period = 1
        self.mode = mode

        if on_time is not None and off_time is not None:
            self.on_time = on_time
            self.off_time = off_time
        else:
            self.on_time = self.time_period / 2
            self.off_time = self.time_period / 2

        self.init_state = init_state
        self.curr_state = init_state
        self.exitFlag = False
        self.daemon = True
        self.A = Connector(self.init_state)
        self.update = False

    def _toggleState(self):
        """
        This is an internal method to toggle the state of the output
        """
        self.A.state = 0 if self.A.state else 1
        self.A.trigger()

    def setMode(self, mode):
        """
        Sets the mode of the Multivibrator
        """
        self.mode = mode
        self.update = False

    def getState(self):
        """
        Returns the current state
        """
        return self.A.state

    def setState(self, value):
        """
        Resets the state of the clock to the passed value
        """
        self.A.state = value

    def getTimePeriod(self):
        """
        Returns the time period of the clock
        """
        return self.time_period

    def kill(self):
        """
        Kills the Thread
        """
        self.exitFlag = True

    def _updater(self):
        while True:
            if self.exitFlag:
                sys.exit()
            if self.update is True:
                if self.mode == 1:
                    self.A.state = 1
                    self.A.trigger()
                    time.sleep(self.time_period)
                    self._toggleState()
                    self.update = False

                elif self.mode == 2:
                    while (self.mode == 2) and (self.update) and (not self.exitFlag):
                        self._toggleState()
                        if self.A.state == 1:
                            time.sleep(self.on_time)
                        else:
                            time.sleep(self.off_time)

                elif self.mode == 3:
                    self._toggleState()
                    self.update = False

    def __call__(self):
        self.update = True

    trigger = __call__

    def setOutput(self, conn):
        a = self.A
        self.A = conn if isinstance(conn, Connector) else a

    def stop(self):
        # For stopping the multivibrator in astable mode.
        self.update = False

    def run(self):
        self._updater()
