import sys
import time
import threading
from BinPy import *


class Clock(threading.Thread):

    """
    This class uses threading technique to create a clock with a certain time period.

    USAGE
    =====

    >>> my_clock = Clock(0,time_period=2,name="My First Clock")
    >>> my_clock.get_state()
    0

    PARAMETERS
    ==========

        frequency   :   It will decide time interval of the clock, use SI unit i.e. Hertz
        time_period :   It will also decide time interval of the clock, use SI unit i.e. second
        init_state  :   It is the initial state of the clock(1 by default)
        name        :   It is the name of the clock.(optional)

        If time_period and frequency both have been provided, then time_period
        will override frequency
        If nothing is provided, then it will set time_period = 1s by default

    METHODS/ PROPERTIES
    ===================

        start()     : [ Depricated ] To start the clock thread.
                      Clock starts at __init__ itself. This need not be used.
        get_state() : Get the current state of the clock.
        set_state() : To set the current state of the clock.
        kill()      : To kill the clock thread.

        state       : [ Property ] Return the state of the clock.
        name        : [ Property ] Return the name of the clock.
        time_period : [ Property ] Return the time period of the clock.
        frequency   : [ Property ] Return the current frequency of the clock.

    NOTE
    ====

    Once you are done with the clock, use my_clock.kill() to kill the clock.
    Running too many clocks will unnecessarily overload the CPU.

    All operations are thread safe and synchronized between inter / intra thread calls.

    """

    def __init__(
            self,
            init_state=1,
            frequency=None,
            time_period=None,
            name=None):

        threading.Thread.__init__(self)
        if frequency is not None:
            self._time_period = float(1) / float(frequency)
        if time_period is not None:
            self._time_period = time_period
        if time_period is None and frequency is None:
            self._time_period = 1

        self._name = name
        self._state = init_state
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
        if self._state == 1:
            self._state = 0
            self.A.state = self._state
            # self.A.trigger()
        else:
            self._state = 1
            self.A.state = self._state
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
        return self._state

    @property
    def state(self):
        """
        Returns the currentd state of the clock as a property.
        """
        return self._state

    def set_state(self, value):
        """
        Resets the state of the clock to the passed value
        """
        if self._state == value:
            return
        self._state = value
        self.A.state = self._state
        # self.A.trigger()

    @property
    def frequency(self):
        return (float(1) / float(self.time_period))

    @property
    def time_period(self):
        return self._time_period

    @property
    def name(self):
        """
        Returns the name of the clock
        """
        return self._name

    def kill(self):
        """
        Kills the clock(Thread)
        """
        self._exit = True
