from __future__ import print_function
import time
from BinPy import Connector
import threading
import sys
import os

class StepperMotor(threading.Thread):
    """
    Create a StepperMotor Simulation
    
    This Class is used to simulate a stepper motor using the adequate input bits.
    """

    index = 0
    
    def __init__(title):
        
        self.POLES = 4
        
        index += 1
        self.index = index
        
        self.data = [None]*8
        
        self._prevData = [0]*8
        self._currData = [0]*8
        
        disp = _SMDisplay(title)
        self._initDisplay()
        
        self.angle = 0
        
        self.exit_flag = False
        self.daemon = True
        self.status = 0
        
    def rotate(self, direction = 1, steps = 1):
        """
        Rotate the stepper motor by [steps] steps and in the specified direction.
        direction 1 --> rotate right
        direction 0 --> rotate left
        """
        
        self.direction = direction
        self.steps = steps
        self.status = 1
        
    def _rotate(self):
        """
        Internally called to realize the rotation.
        """
        
        if None in self.data:
            raise("ERROR: Error in connection")
        
        for i in range(self.steps):
            
            self._prevData = [str(int(i)) for i in self.data]
            self._currData = list(self._prevData)[:]
            self._currData = self._rotateRight() if self.direction == 1 else self._rotateLeft()
            self._updateData()
            self._updateDisplay(self._currData)
            
            
    def _rotateRight(array = self._currData):
        # Rotate Right
        return self.array[:1] + self.array[1:]
    
    def _rotateLeft(array = self._currData): 
        # Rotate Left
        return self.array[:1] + self.array[1:]
    
        self._updateData()
        
    def _updateData():
        for i in range(8):
            self.data[i].state = self._currData[i]
        
    def _updateDisplay():
        if (self._prevData == self._currData):
            self.angle += 0
        else if rotate(self._prevData, 1) == self._currData:
            self.angle += 1
        else if rotate(self._prevData, 0) == self._currData:
            self.angle += -1
            
        
        disp.redraw(rotateby = self.angle)
        
    self._start2 = self.start
    
    def start(self):
        self._start2()
        sys.exit(self.app._exec())
    
    def reset(self):
        self.angle(0)
        self._updateDisplay()
        
        for pin in self.data:
            pin.state = 0
        
    def setInput(self, index, value):
        """
        Set the input based on the index and value.
        
        If the value is a Connector, then the respective input is connected to it.
        else the Connector at that index is updated with the value.
        
        """
        if index <= 8:
            if isinstance(value, Connector):
                self.data[index] = value
            else:
                self.data[index].state = int(value)
        
    def disconnect():
        for pin in self.data:
            pin.untap(self)
            
    def kill():
        """
        To kill the thread
        """        
        self.exit_flag = True
        
    def run():
        while not self.exit_flag:
            if self.status = 
            

    def trigger():
        # Incase any connector calls this.
        pass






# NO IDEA WHAT I AM DOING HERE ! :p
    
class _StepperMotorDisplay(QtGui.QWidget):
    
    def __init__(self,title):
        
        super(StepperMotorDisplay, self).__init_()
        self.init_UI()
        
        self.index += 1
        self.name = name
        
        # To support both win and linux
        self.path = os.path.join("..", "res", "gear.jpg")
        
        app = QtGui.QApplication()
        
        w.setWindowTitle('StepperMotor'+str(self.index))
        self._update_image(w)
        
        w.show()
        
        # somewhere here it has to refresh the display with the image tilted by the new angle !
        # upon calling some function like updateDisplay(angle)
        
    def init_UI(self):
        
        self.setGeometry(300, 300, 250, 150)
        
        self.setWindowTitle(str(self.index) + ' - StepperMotor - ' + str(self.name))
        
        self.show()
        
    def main():
        
        app = QtGui.QApplication()
        
        
    
