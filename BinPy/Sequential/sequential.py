from BinPy import *
from BinPy.Gates import *
#Rewriting all FlipFlops using behavioural modelling and partially using data flow modelling.

class SRLatch:

    def __init__(self):
        
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())

    def __call__(self,s,r,enable):
        if enable == 1:
            #Ouput will change only if enable is 1
            
            if ( s==1 ) and ( r==0 ) :
                self.q = NOT(False)
                self.qcomp = NOT(self.q.output())
                
            elif ( s==0 ) and ( r==1 ) :
                self.q = NOT(True)
                self.qcomp = NOT(self.q.output())
                
            else:
                #To simulate the invalid state.
                self.q = NOT(random.choice([True,False]))
                self.qcomp = NOT(random.choice([True,False]))
                
        return [self.q.output(),self.qcomp.output()]
        
    def reset(self):
        #Resets the latch
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        
        return [self.q.output(),self.qcomp.output()]


class DFlipFlop:

    def __init__(self):

        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        #q is a gate instance with 'output()' method

    def __call__(self,d,enable):
        
        if enable == 1:
            #Output will change only if enable is 1
            self.q = AND(d,d) # d.d = d -> done to make q an instance of GATE class.
        self.qcomp = NOT(self.q.output())
        
        return [self.q.output(),self.qcomp.output()]

    def reset(self):
        #Resets the latch
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        
        return [self.q.output(),self.qcomp.output()]


class JKFlipFlop:
    
    def __init__(self):
                        
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        #To initiate q and qcomp as Gate instances with a method 'output()'

    def __call__(self,j,k,enable):
        #Call method acts like the trigger
        #Every time the instance is called with the appropriate parameters, a clock pulse is applied [ Output  toggles from the previous state]
        
        if enable == 1:
        #Output changes only if enable is 1
            if ( j == 1 )  and  ( k == 1 ) :
                self.q = NOT(self.q.output())
                
            elif ( j == 0 )  and ( k == 1 ) :
                self.q = NOT(True)
                
            elif ( j == 1 ) and  ( k == 0 ) :
                self.q = NOT(False)
            
            else:
                pass # j = 0; k = 0 ; No Change in q.
            
            self.qcomp = NOT(self.q.output())
            
        return [self.q.output(),self.qcomp.output()]

    def reset(self):
        #Resets the Output
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        
        return [self.q.output(),self.qcomp.output()]


class TFlipFlop:

    def __init__(self):
                        
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())            
        #To initiate q and qcomp as Gate instances with a method 'output()'

    def __call__(self,t,enable):
        #Call method acts like the trigger
        #Every time the instance is called with the appropriate parameters, a clock pulse is applied [ Output  toggles from the previous state]
        
        t = AND(t,enable)
        #Output will change only if enable is 1
        if bool(t.output()):
            self.q = NOT(self.q.output())
            self.qcomp = NOT(self.q.output())            
            
        return [self.q.output(),self.qcomp.output()]
    
    def reset(self):
        #Resets the Output
        self.q = NOT(True)
        self.qcomp = NOT(self.q.output())
        
        return [self.q.output(),self.qcomp.output()]