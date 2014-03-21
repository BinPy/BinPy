from __future__ import print_function
from time import time
from itertools import chain
from BinPy import Connector

V = u"\u2502"; H = u"\u2500"; HVD = u"\u2510"; HVU = u"\u2518"; VHU = u"\u250c"; VHD = u"\u2514";N =u"\u000A"; 
class Oscilloscope(object):
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
        self.inputDict = {}
        self.changed = False
        self.MAX_INP = 6
        self.mintp = 99999999
        self.maxtp = 0
        self.xaxis = []
        self.mulfactor = 1
        self.divfactor = 1
        self.WID = 150
        self.LEN = 500
        self.startTime = 0
        self.xPoints = 0
        self.xUnitWidth = 0
        
        self.active = False
        
        if len(inputs)>0:
            self.updateInputs(inputs)
    
    reset = __init__
    
    def setWidth(self,w = 150):
        self.WID = w
    
    def updateInputs(self, *inputs):
        """
        Set inputs using a list of tuples.
        
        For example:
        
        osc1.setInputs((conn1,"label") , (conn2,"label") ... )
        
        """
        if len(inputs) < 1:
            raise Exception("ERROR: Too few inputs given.")
        try:
            errorCheck = list(chain.from_iterable( (isinstance(i,tuple),isinstance(i[0], Connector),isinstance(i[1],str)) for i in inputs ))
        except:
            errorCheck = [False]
        if (False in errorCheck):
            raise Exception("ERROR: Invalid input format")
        
        else:
            for i in inputs:
                lbl = (i[1]+(5-len(i[1]))*" " if len(i[1])<=5 else i[:5]).rjust(5)
                if i[0] in self.inputDict:
                    (self.inputDict[i[0]])["label"] = lbl
                else:
                    self.inputDict[i[0]] = { "label":lbl,
                                            "oldval":0,
                                            "plot":[],
                                            "mintp":99999999,
                                            "maxtp":0,
                                            "disp":{},
                                            "logicArray":[0]*self.WID}
                    i[0].tap(self,"input")
                    self.changed = True
        
        self.trigger()

    def disconnect(self,conn):
        """
        Disconnects conn from the inputDict
        """
        self.inputDict.pop(conn,None)
        self.conn.untap(self,'input')
    
    def trigger(self):
        if self.active:
            if self._isChanged():
                self.changed = False
                self._updatePlotPoints()
                self._updateOldVals()
    
    def _updatePlotPoints(self):
        for j in self.inputDict:
            i = self.inputDict[j]
            if i["oldval"] != int(j):
                i["plot"].append((time()-self.startTime,int(j)))
                if len(i["plot"]) != 1:
                    curtp = i["plot"][-1][0] - i["plot"][-2][0]
                    i["mintp"] = min(curtp,i["mintp"])
                    i["maxtp"] = max(curtp,i["maxtp"])
                    self.mintp = min(self.mintp,i["mintp"])
                    self.maxtp = max(self.maxtp,i["maxtp"])
            
    def getLogicArray(self,timeStamp):
        logicArray = [0]*self.WID
        if len(self.xaxis) == self.WID:
            j = 0
            i = 0
            while i < self.WID:
                if j >= len(timeStamp):
                    logicArray[i] = 0
                    i += 1
                elif ( self.xaxis[i] + (self.xUnitWidth/2) ) < timeStamp[j][0]:
                    logicArray[i] = timeStamp[j][1]
                    i += 1
                else:
                    j += 1
        return logicArray
            
    def _autoScale(self):
        self.stop()
        
        self.xPoints = self.totalTime // self.mintp + 1
        
        if self.xPoints < self.WID:
            self.xUnitWidth = self.xPoints / self.WID
        else:
            self.xUnitWidth = self.mintp
            
        
        self.xaxis = [ i*(self.xUnitWidth) for i in range(self.WID) ]
    
    def _genLogicArray(self):
        for i in self.inputDict:
            self.inputDict[i]["logicArray"] = self.getLogicArray(self.inputDict[i]["plot"])
        
    def start(self):
        if not self.active:
            self.startTime = time()
            self.active = True
        
    def stop(self):
        if self.active:
            self.totalTime = time() - self.startTime
            self.active = False
    
        
    def clear(self):
        self.mintp = 99999999
        self.maxtp = 0
        self.startTime = 0
        self.active = False
        self.totalTime = 0
        for c in self.inputDict:
            i = self.inputDict[c]
            i["oldval"] = 0
            i["plot"] = []
            i["mintp"] = 99999999
            i["maxtp"] = 0
            i["disp"] = {}
            i["logicArray"] = [0]*self.WID

    def _isChanged(self):
        if self.changed:
            return True
        else:
            for i in self.inputDict:
                if self.inputDict[i]['oldval'] != int(i):
                    self.changed = True
                    return True

    def _updateOldVals(self):
        for i in self.inputDict:
            self.inputDict[i]['oldval'] = int(i)
            
    def display(self):
        self.stop()
        self._autoScale()
        self._genLogicArray()
        
        sclstr = "SCALE - X-AXIS : 1 UNIT WIDTH = %s"%str(self.xUnitWidth)
        llen = (self.WID+15)
        disp =  "="*llen + "\nBinPy - Oscilloscope\n" + "="*llen
        disp += " "*(len(disp)-len(sclstr)-1)+sclstr+N+"="*llen+N
        
        j = 0
        for i in self.inputDict:
            d = self.inputDict[i]
            lA = [0]+d["logicArray"]+[0]
            disp += " "*10+V+N
            disp += " "*10+V+N
            disp += " "*10+V+" "
            for i in range(1,len(lA)-1 ):
                cmpstr = (lA[i-1],lA[i])
                if cmpstr  == (1,0):
                    disp+=HVD
                elif cmpstr == (1,1):
                    disp+=H
                elif cmpstr == (0,0):
                    disp+=" "
                elif cmpstr == (0,1):
                    disp+=VHU
                    
            disp += N+" "*3+d["label"]+"  "+V+" "
            
            for i in range(1,len(lA)-1 ):
                cmpstr = lA[i-1],lA[i]
                if cmpstr  == (1,0):
                    disp+=V
                elif cmpstr == (0,1):
                    disp+=V
                else:
                    disp+=" "
            
            disp += N+" "*10+H+" "
            
            for i in range(1,len(lA)-1 ):
                cmpstr = lA[i-1],lA[i]
                if cmpstr  == (1,0):
                    disp+=VHD
                elif cmpstr == (1,1):
                    disp+=" "
                elif cmpstr == (0,0):
                    disp+=H
                elif cmpstr == (0,1):
                    disp+=HVU
            disp += N+" "*10+V+N
            disp += " "*10+V+N
        disp += V*llen+N
        disp += H*llen+N
        
                
        print(disp)