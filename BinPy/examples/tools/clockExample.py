import time
from BinPy.clock import *
from BinPy.Gates.connector import *
print('Demonstarting the use of Clock using an example')
print('Created a Clock object of time period 2s and initial state of 0')
t = 2
clk = Clock(False, time_period = t)
c = Connector()
clk.connect(c)
clk.start()
print('Connected a connector, c and printing its states after every second for 10s')
time.sleep(t/20)

for i in range(11):
    print("  Time        State of c")
    print (time.strftime("%I:%M:%S") + '\t' + str(c.state))
    time.sleep(t/2)

clk.disconnect(c)
print('Now, Disconnected the connector')
print('State of connector: '+str(c.state))
