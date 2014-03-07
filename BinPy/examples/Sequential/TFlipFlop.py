#Example for TFlipFlop

from BinPy import *

toggle = Connector(1)

p = Connector(0)
q = Connector(1)

#Initialize the clock
clock = Clock(1,1)
clock.start()
#A clock of 1 hertz frequency
clk_conn = clock.A

enable = Connector(1)

#Initialize the T-FlipFlop
tff = TFlipFlop(toggle,enable,clk_conn,p,q)

#To connect different set of connectors use :
#tff.setInputs(conn1,enab,clk)
#To connect different outputs use:
tff.setOutputs(A = p, B = q)

print 'Toggle is 1'
toggle.state = 1
while True:
    if clk_conn.state == 0:
        #Falling edge will trigger the FF
        tff.trigger()
        break
print tff.state()

#Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        #Falling edge will trigger the FF
        tff.trigger()
        break

print 'Toggle is 1'    
while True:
    if clk_conn.state == 0:
        #Falling edge will trigger the FF
        tff.trigger()
        break
print tff.state()

#Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        #Falling edge will trigger the FF
        tff.trigger()
        break

print 'Toggle is 1'    
while True:
    if clk_conn.state == 0:
        #Falling edge will trigger the FF
        tff.trigger()
        break
print tff.state()

#Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        #Falling edge will trigger the FF
        tff.trigger()
        break

print 'Toggle is 0'    
toggle.state = 0
while True:
    if clk_conn.state == 0:
        #Falling edge will trigger the FF
        tff.trigger()
        break
print tff.state()

#Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        #Falling edge will trigger the FF
        tff.trigger()
        break

print 'Toggle is 0'    
while True:
    if clk_conn.state == 0:
        #Falling edge will trigger the FF
        tff.trigger()
        break
print tff.state()

#Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        #Falling edge will trigger the FF
        tff.trigger()
        break