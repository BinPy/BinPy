from __future__ import print_function
import time
from itertools import chain
from BinPy.connectors import *
from BinPy.draw import symbols
import threading
import sys

try:
    range = xrange  # This is to make the sampler more efficient in python2
except:
    pass


class Oscilloscope(threading.Thread):

    """
    Oscilloscope is helpful in visualizing simulations.

    USAGE:
    # A clock of 1 hertz frequency
    clock = Clock(1, 1)
    clk_conn = clock.A

    bc = BinaryCounter()
    os1 = Oscilloscope( (bc.out[1],'lsb') , (bc.out[0],'msb'))
    #Triggering the counter:
    for i in range(5):
        b.trigger()
        print (b.state())
    os1.stop()
    os1.display()
    """

    def __init__(self, *inputs):
        threading.Thread.__init__(self)
        self.daemon = True

        self.MAX_INP = 15
        self.WIDTH = 150

        self.inputs = []
        self.labels = {}
        self.logic_array = [[]]
        self._clear_LA()
        self.len_inputs = 0

        self.exit = False
        self.colour = "\x1b[0m"

        if len(inputs) > 0:
            self.set_inputs(*inputs)

        self.active = False
        self.scale = 1

        self._strtd = False
        self.start()

    def start(self):
        """ Do not use this method """
        # Kept to make it compatible with older versions of BinPy
        if not self._strtd:
            threading.Thread.start(self)
            self._strtd = True

    def _clear_LA(self):
        self.logic_array = [
            [0 for x in range(self.WIDTH)] for x in range(self.MAX_INP)]

    def set_width(self, w=150):
        """
        Set the maximum width of the oscilloscope.
        This is dependent on your current monitor configuration.
        """
        if w in range(50, 300):
            self.WIDTH = w
        else:
            print("ERROR:Invalid width. Width reverted to old value")

    def set_scale(self, scale=0.05):
        """
        This decides the time per unit xWidth.
        To avoid waveform distortion, follow NYQUIST sampling theorem.
        That is if the least time period of the waveform is T;
        Set the scale to be greater than T/2 [ preferably T/5 - To avoid edge sampling effects ]

        There is a lower bound on the scale value [ use trial and error to identify this for your particular PC ]
        This limitation is set by the processing time taken to set a plot etc.
        """
        self.scale = scale

    def set_inputs(self, *inputs):
        """
        Set inputs using a list of tuples.

        For example:
        osc1.setInputs((conn1,"label") , (conn2,"label") ... )
        """
        self.clear(True)

        if len(inputs) < 1:
            raise Exception("ERROR: Too few inputs given.")

        if len(inputs) > self.MAX_INP - self.len_inputs:
            raise Exception("ERROR: Maximum inputs exceeded")

        try:
            for i in inputs:
                if not (isinstance(i, tuple) and isinstance(i[0], Connector) and isinstance(i[1], str)):
                    raise Exception("ERROR: Invalid input format")
        except:
            raise Exception("ERROR: Invalid input format")

        for i in inputs:
            lbl = i[1][:5].rjust(5, ' ')

            if i[0] in self.labels:
                self.labels[i[0]] = lbl
            else:
                self.inputs.append(i[0])
                self.labels[i[0]] = lbl

        self.len_inputs = len(self.inputs)

    def disconnect(self, conn):
        """
        Disconnects conn from the inputDict
        """
        self.hold()
        self.clear(True)
        self.labels.pop(conn, None)
        self.inputs.remove(conn)
        self.len_inputs = len(self.inputs)

    def sampler(self, trigPoint):
        # DEV-note: This is critical part and needs to be highly efficient.
        # Do not introduce any delay causing element

        for i in range(self.len_inputs):
            self.logic_array[i][trigPoint] = self.inputs[i].state

    def unhold(self):
        self.clear(True)
        self.active = True

    def hold(self):
        self.active = False

    def clear(self, keepInputs=False):
        self.active = False

        try:
            print("\x1b[0m")
        except:
            pass

        self._clear_LA()
        if not keepInputs:
            self.inputs = []
            self.len_inputs = 0

    def run(self):
        while True:
            if self.exit:
                sys.exit()
            while self.active:
                for i in range(self.WIDTH):
                    if not self.active:
                        break
                    time.sleep(self.scale)
                    self.sampler(i)
                self.hold()

    def kill(self):
        self.exit = True

    def set_colour(self, foreground=None, background=None):
        """
        Acceptable values are:
        1 --> RED
        2 --> GREEN
        4 --> BLUE
        7 --> WHITE

        To RESET call without parameters.

        Please note that serColor is not supported by all operating systems.
        This will run without problems on most Linux systems.
        """
        if not foreground and not background:
            self.colour = "\x1b[0m"

        self.colour = "\x1b[3%im\x1b[4%im" % (foreground, background)

    def display(self):
        self.hold()

        try:
            sclstr = "SCALE - X-AXIS : 1 UNIT WIDTH = %s" % str(self.scale)
            llen = (self.WIDTH + 15)
            disp = self.colour + "=" * llen + \
                "\nBinPy - Oscilloscope\n" + "=" * llen
            disp += symbols._N + \
                sclstr.rjust(llen, " ") + symbols._N + "=" * llen + symbols._N

            j = 0
            for i in range(self.len_inputs):

                conn = self.inputs[i]

                lA2 = [0] + self.logic_array[i] + [0]
                lA = [j if j is not None else 0 for j in lA2]

                disp += " " * 10 + symbols._V + symbols._N
                disp += " " * 10 + symbols._V + symbols._N
                disp += " " * 10 + symbols._V + " "
                for i in range(1, len(lA) - 1):
                    cmpstr = (lA[i - 1], lA[i])
                    if cmpstr == (1, 0):
                        disp += symbols._HVD
                    elif cmpstr == (1, 1):
                        disp += symbols._H
                    elif cmpstr == (0, 0):
                        disp += " "
                    elif cmpstr == (0, 1):
                        disp += symbols._VHU

                disp += symbols._N + " " * 3 + \
                    self.labels[conn] + "  " + symbols._V + " "

                for i in range(1, len(lA) - 1):
                    cmpstr = lA[i - 1], lA[i]
                    if cmpstr == (1, 0):
                        disp += symbols._V
                    elif cmpstr == (0, 1):
                        disp += symbols._V
                    else:
                        disp += " "

                disp += symbols._N + " " * 10 + symbols._H + " "

                for i in range(1, len(lA) - 1):
                    cmpstr = lA[i - 1], lA[i]
                    if cmpstr == (1, 0):
                        disp += symbols._VHD
                    elif cmpstr == (1, 1):
                        disp += " "
                    elif cmpstr == (0, 0):
                        disp += symbols._H
                    elif cmpstr == (0, 1):
                        disp += symbols._HVU
                disp += symbols._N + " " * 10 + symbols._V + symbols._N
                disp += " " * 10 + symbols._V + symbols._N
            disp += symbols._V * llen + symbols._N
            disp += symbols._H * llen + symbols._N + "\x1b[0m"
            print(disp)
        except:
            print("\x1b[0mERROR: Display error: " + sys.exc_info()[1].args[0])
