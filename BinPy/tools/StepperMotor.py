from __future__ import print_function
import time
from BinPy import Connector
import threading
import sys
import os

class StepperMotor(threading.Thread):
    """
    Create a StepperMotor Simulation
    
    Description:
    ============
    
    This Class is used to simulate a stepper motor using the adequate inputs.
    
    Specifications:
    ===============
    
    Drive Method        : Bipolar ( Predefined )
    No. of Phases       : 2
    No. of rotor poles  : 100 ( Can be modified )
    Winding Per Phase   : 1
    Type                : Permanent magnet
    Maximum RPM         : 1200
    
    EXAMPLE
    =======

    sm = StepperMotor()
    
    for i in range(100):
        sm.rotate(1,1)
        time.sleep(0.1)
        
    # To rotate through a certain angle
    sm.rotate(steps = -90 / sm.step_angle, rpm = 60)
    """

    index = 0
    
    def __init__(self, title):
   
        self.title = str(title)

        self.ROTOR_POLES = 100
        self.PHASES = 2
        self.MAX_RPM = 1200
   
        
        # No of rotor poles = No of poles per phase
        self.total_poles = self.ROTOR_POLES * self.PHASES
        self.step_angle = 360 / self.total_poles
        
        StepperMotor.index += 1
        self.index = StepperMotor.index
        
        self.leads = [None]*4
        
        self._data = [0]*4
        
        self._prev_data = [0]*4
        
        self._disp = _SMDisplay(bound_to = self,self.title,self.index)
        self._disp.show()
        
        self.angle = 0
        
        self.exit_flag = False
        self.daemon = True
        
        # Internally used to call various methods.
        self._status = 0
        
        self.start()
        
    def rotate(self, steps = 1, direction = 1, rpm = self.MAX_RPM):
        """
        Rotate the stepper motor by [steps] steps and in the specified direction.
        direction 1 --> rotate right
        direction 0 --> rotate left
        """
        
        self.direction = direction
        
        if steps < 0:
            self.steps = -round(steps)
            self.direction = 0
        else:
            self.steps = round(steps)
            self.direction = 1
            
        self.steps = round(steps)
        self._status = 1
        
        self.rpm = rpm if rpm < self.MAX_RPM and rpm > 0 else self.rpm
    
    def move_to(self, angle, rpm = self.MAX_RPM, shortest_path = True):
        """
        Rotate the stepper motor in the specified rpm speed to reach the specified angle.
        The shortest_path when set forces rotation in the direction of minor arc.
        If shortest_path is not set the behaviour is in the direction of either the major
        or minor arc.        
        """
    
        diff_angle = abs( angle-self.angle )

        if angle in range(0,360):
            if shortest_path and diff_angle < 180:
                diff_angle *= -1
            self.rotate( diff_angle / self.step_angle, rpm= rpm)
        else:
            raise("ERROR: Invalid angle")
    
    def _rotate(self):

        """
        Internally called to realize the rotation.
        """
        
        if None in self.leads:
            raise("ERROR: Error in connection")
        
        while(self.steps > 0):
            self._update_data()
            self._data = self._rotate_right() if self.direction == 1 else self._rotate_left()
            self._update_leads()
            self._update_angle()
            self._disp.refresh()
            self.steps -= 1
            time.sleep(60/self.rpm)
            
    def _rotate_right(array = self._data):
        # Rotate Right
        return array[:1] + array[1:]
    
    def _rotate_left(array = self._data): 
        # Rotate Left
        return array[:1] + array[1:]
    
    def _update_data(self):
        self._prev_data = self._data
        self._data = [str(int(i)) for i in self._leads]
    
    def _update_leads(self):
        for i in range(4):
            self.leads[i].state = self._data[i]
        
    def _update_angle():
        if (self._prev_data == self._data):
            self.angle += 0
        else if _rotate_right(self._prev_data) == self._curr_data:
            self.angle += self.step_angle
        else if _rotate_left(self._prev_data) == self._curr_data:
            self.angle -= self.step_angle
        else:
            # Wrong configuration of input
            # self.angle remains unchanged
            # This else is just for clarity
            pass
        
        if self.angle < 0:
            self.angle += 360
            
        if self.angle >= 360:
            self.angle %= 360
            
    def reset(self):
        for pin in self.leads:
            pin.state = 0
        self._update_angle()
        
    def set_input(self, index, value):
        """
        Set the input based on the index and value.
        
        If the value is a Connector, then the respective input is connected to it.
        else the Connector at that index is updated with the value.
        """
        
        if isinstance(self.data[index], Connector):
            self.data[index].untap(self)
            
        if index <= 8:
            if isinstance(value, Connector):
                self.data[index] = value
            else:
                self.data[index].state = int(value) if isinstance(self.data[index],Connector) else None
                
        if self.data[index] = None:
            raise("ERROR: The leads are not initialized. Please intitialize leads by setting connectors to them."
        else:
            self.data[index].tap(self,'input')            
        
    def disconnect():
        for pin in self.leads:
            pin.untap(self)
            
    def kill():
        """
        To kill the thread
        """        
        self.exit_flag = True
        
    def run():
        while not self.exit_flag:
            if self.status = 1:
                self._rotate()
                print(self.angle)
            else if self.status = 2:
                self._update_data()
                self._update_angle()
                self._disp.refresh()
                print(self.angle)
                
        self._disp.exit()
        sys.exit()

    def trigger():
        self.status = 2

# NO IDEA WHAT I AM DOING HERE ! :p
    
class _SMDisplay(object):
    
    def __init__(self,bound_to, label, idno):
        self.bound_to = bound_to
        self.label = label
        self.idno = idno
        """
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
        """
    def refresh(self):
        print(self.idno + " " + self.label)
        print(self.bound_to.angle)

    def show(self):
        pass

    def exit(self):
        pass
