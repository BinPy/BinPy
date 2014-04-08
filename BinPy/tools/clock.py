import sys
import time
import threading
from BinPy import Connector


class Clock(threading.Thread):

    """
    This class uses threading technique to create a clock with a certain time period.
    This is how you can create a clock with this class:
        >>> myClock = Clock(0,time_period=2,name="My First Clock")
        >>> myClock.start()     #Do not call run method
        >>> myClock.getState()
        0

    Note: Once you are done with the clock, use myClock.kill() to kill the clock.
          Running too many clocks will unnecessarily overload the CPU.

    Following are the parameters of the class

        :param frequency:   It will decide time interval of the clock, use SI unit i.e. Hertz
        :param time_period: It will also decide time interval of the clock, use SI unit i.e. second
        :param init_state:  It is the initial state of the clock(1 by default)
        :param name:        It is the name of the clock.(optional)

        If time_period and frequency both have been provided, then time_period
        will override frequency
        If nothing is provided, then it will set time_period = 1s by default
    Methods :   start(), getState(), setState(value), getName(), getTimePeriod(), kill()
    """

    def __init__(
            self,
            init_state=1,
            frequency=None,
            time_period=None,
            name=None):
        threading.Thread.__init__(self)
        if frequency is not None:
            self.time_period = 1.0 / frequency
        if time_period is not None:
            self.time_period = time_period
        if time_period is None and frequency is None:
            self.time_period = 1

        self.init_state = init_state
        self.name = name
        self.curr_state = init_state
        self.exitFlag = 0
        self.daemon = True
        self.A = Connector(0)
        # self.A.trigger()

    def __toggleState(self):
        """
        This is an internal method to toggle the state of the output
        """
        if self.curr_state == 1:
            self.curr_state = 0
            self.A.state = self.curr_state
            # self.A.trigger()
        else:
            self.curr_state = 1
            self.A.state = self.curr_state
            # self.A.trigger()

    def __main_func(self):
        while True:
            if self.exitFlag:
                sys.exit()
            time.sleep(self.time_period)
            try:
                self.__toggleState()
            except:
                pass

    def getState(self):
        """
        Returns the current state of the clock
        """
        return self.curr_state

    def setState(self, value):
        """
        Resets the state of the clock to the passed value
        """
        if self.curr_state == value:
            return
        self.curr_state = value
        self.A.state = self.curr_state
        # self.A.trigger()

    def getTimePeriod(self):
        """
        Returns the time period of the clock
        """
        return self.time_period

    def getName(self):
        """
        Returns the name of the clock
        """
        return self.name

    def kill(self):
        """
        Kills the clock(Thread)
        """
        self.exitFlag = 1

    def run(self):
        self.__main_func()
