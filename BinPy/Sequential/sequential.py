from BinPy.Gates import *


class SRLatch:

    def __init__(self, R, S):
        """
        Construct an SRLatch with initial reset input R and set input S.
        """

        self.a = Connector()
        self.b = Connector()

        self.g1 = NOR(R, self.b)
        self.g1.setOutput(self.a)

        self.g2 = NOR(S, self.a)
        self.g2.setOutput(self.b)

    def setInputs(self, R, S):
        """
        Set this SRLatch's reset input to R and set input to S.
        Unstable behaviour when transitioning directly from RS = 11 to RS = 00.
        """

        self.g1.setInput(0, R)
        self.g2.setInput(0, S)

    def output(self):
        """
        Return the output of this SRLatch in the format [Q, Q'].
        """

        return [self.g1.output(), self.g2.output()]

class DLatch:

    def __init__(self, D):
        """
        Construct an DLatch with initial reset input D1 and set input D.
        """
	D1=0
	if D==0:
		D1=1
        self.a = Connector()
        self.b = Connector()

        self.g1 = NOR(D1, self.b)
        self.g1.setOutput(self.a)

        self.g2 = NOR(D, self.a)
        self.g2.setOutput(self.b)

    def setInputs(self,D):
        """
        Set this DLatch's reset input to D1 and set input to D.
        """
	D1=0
	if D==0:
		D1=1
        self.g1.setInput(0, D1)
        self.g2.setInput(0, D)

    def output(self):
        """
        Return the output of this DLatch in the format [Q, Q'].
        """

        return [self.g1.output(), self.g2.output()]
