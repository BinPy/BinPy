from __future__ import print_function
import time
from itertools import chain
from BinPy import Connector
import threading
import sys

try:
    _V = chr(9474)
    _H = chr(9472)
    _HVD = chr(9488)
    _HVU = chr(9496)
    _VHU = chr(9484)
    _VHD = chr(9492)
    _N = chr(10)
except:
    range = xrange  # This is to make the sampler more efficient in python2
    _V = unichr(9474)
    _H = unichr(9472)
    _HVD = unichr(9488)
    _HVU = unichr(9496)
    _VHU = unichr(9484)
    _VHD = unichr(9492)
    _N = unichr(10)


class Oscilloscope(threading.Thread):

    """
    Oscilloscope is helpful in visualizing simulations.

    USAGE:
    # A clock of 1 hertz frequency
    clock = Clock(1, 1)
    clock.start()
    clk_conn = clock.A

    bc = BinaryCounter()
    os1 = Oscilloscope( (bc.out[1],'lsb') , (bc.out[0],'msb'))
    os1.start()
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
        self.WID = 150
        self.LEN = 500

        self.inputs = []
        self.labels = {}
        self.logicArray = [[]]
        self.clearLA
        self.leninputs = 0

        self.active = False
        self.exitFlag = False
        self.C = "\x1b[0m"

        if len(inputs) > 0:
            self.updateInputs(*inputs)

    def clearLA(self):
        self.logicArray = [
            [0 for x in range(self.WID)] for x in range(self.MAX_INP)]

    def setWidth(self, w=150):
        """
        Set the maximum width of the oscilloscope.
        This is dependent on your current monitor configuration.
        """
        if w in range(50, 300):
            self.WID = w
        else:
            print("ERROR:Invalid width. Width reverted to old value")

    def setScale(self, scale=0.05):
        """
        This decides the time per unit xWidth.
        To avoid waveform distortion, follow NYQUIST sampling theorem.
        That is if the least time period of the waveform is T;
        Set the scale to be greater than T/2 [ preferably T/5 - To avoid edge sampling effects ]

        There is a lower bound on the scale value [ use trial and error to identify this for your particular PC ]
        This limitation is set by the processing time taken to set a plot etc.
        """
        self.scale = scale

    def updateInputs(self, *inputs):
        """
        Set inputs using a list of tuples.

        For example:
        osc1.setInputs((conn1,"label") , (conn2,"label") ... )
        """
        self.clear(True)

        if len(inputs) < 1:
            raise Exception("ERROR: Too few inputs given.")

        if len(inputs) > self.MAX_INP - self.leninputs:
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

        self.leninputs = len(self.inputs)

    def disconnect(self, conn):
        """
        Disconnects conn from the inputDict
        """
        self.hold()
        self.clear(True)
        self.labels.pop(conn, None)
        self.inputs.remove(conn)
        self.leninputs = len(self.inputs)

    def sampler(self, trigPoint):
        # DEV-note: This is critical part and needs to be highly efficient.
        # Do not introduce any delay causing element

        for i in range(self.leninputs):
            self.logicArray[i][trigPoint] = self.inputs[i].state

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

        self.clearLA()
        if not keepInputs:
            self.inputs = []
            self.leninputs = 0

    def _trigger(self):
        while True:
            if self.exitFlag:
                sys.exit()
            while self.active:
                for i in range(self.WID):
                    if not self.active:
                        break
                    time.sleep(self.scale)
                    self.sampler(i)
                self.hold()

    def run(self):
        self._trigger()

    def kill(self):
        self.exitFlag = True

    def setColour(self, foreground=1, background=7):
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
            self.C = "\x1b[0m"

        self.C = "\x1b[3%im\x1b[4%im" % (foreground, background)

    def display(self):
        self.hold()

        try:
            sclstr = "SCALE - X-AXIS : 1 UNIT WIDTH = %s" % str(self.scale)
            llen = (self.WID + 15)
            disp = self.C + "=" * llen + \
                "\nBinPy - Oscilloscope\n" + "=" * llen
            disp += _N + sclstr.rjust(llen, " ") + _N + "=" * llen + _N

            j = 0
            for i in range(self.leninputs):

                conn = self.inputs[i]

                lA2 = [0] + self.logicArray[i] + [0]
                lA = [j if j is not None else 0 for j in lA2]

                disp += " " * 10 + _V + _N
                disp += " " * 10 + _V + _N
                disp += " " * 10 + _V + " "
                for i in range(1, len(lA) - 1):
                    cmpstr = (lA[i - 1], lA[i])
                    if cmpstr == (1, 0):
                        disp += _HVD
                    elif cmpstr == (1, 1):
                        disp += _H
                    elif cmpstr == (0, 0):
                        disp += " "
                    elif cmpstr == (0, 1):
                        disp += _VHU

                disp += _N + " " * 3 + self.labels[conn] + "  " + _V + " "

                for i in range(1, len(lA) - 1):
                    cmpstr = lA[i - 1], lA[i]
                    if cmpstr == (1, 0):
                        disp += _V
                    elif cmpstr == (0, 1):
                        disp += _V
                    else:
                        disp += " "

                disp += _N + " " * 10 + _H + " "

                for i in range(1, len(lA) - 1):
                    cmpstr = lA[i - 1], lA[i]
                    if cmpstr == (1, 0):
                        disp += _VHD
                    elif cmpstr == (1, 1):
                        disp += " "
                    elif cmpstr == (0, 0):
                        disp += _H
                    elif cmpstr == (0, 1):
                        disp += _HVU
                disp += _N + " " * 10 + _V + _N
                disp += " " * 10 + _V + _N
            disp += _V * llen + _N
            disp += _H * llen + _N + "\x1b[0m"
            print(disp)
        except:
            print("\x1b[0mERROR: Display error: " + sys.exc_info()[1].args[0])
