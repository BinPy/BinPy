import sys
import time
import threading
from BinPy import *


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

        self.name = name
        self.curr_state = init_state
        self._exit = False
        self.daemon = True

        self.A = Connector(init_state)

        self._strtd = False
        self.start()

    def start(self):
        """ Do not use this method """
        # Kept to make it compatible with older versions of BinPy
        if not self._strtd:
            threading.Thread.start(self)
            self._strtd = True

    def _toggle_state(self):
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

    def run(self):
        while True:
            if self._exit:
                sys.exit()
            time.sleep(self.time_period)
            try:
                self._toggle_state()
            except:
                pass

    def get_state(self):
        """
        Returns the current state of the clock
        """
        return self.curr_state

    def set_state(self, value):
        """
        Resets the state of the clock to the passed value
        """
        if self.curr_state == value:
            return
        self.curr_state = value
        self.A.state = self.curr_state
        # self.A.trigger()

    def time_period(self):
        """
        Returns the time period of the clock
        """
        return self.time_period

    def name(self):
        """
        Returns the name of the clock
        """
        return self.name

    def kill(self):
        """
        Kills the clock(Thread)
        """
        self._exit = True
