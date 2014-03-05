from BinPy.Combinational.combinational import *
""" Examples for Encoder class """
print "\n---Initializing the Encoder class--- "
print "mux = Encoder(0, 1) #Exacly 1 input must be 1"
encoder = Encoder(0, 1)
print "\n---Output of encoder"
print "encoder.output()"
print encoder.output()
print "\n---Changing the number of inputs---"
print "No need to set the number, just change the inputs"
print "Input must be power of 2"
print "encoder.setInputs(1, 0, 0) #Inputs must be power of 2"
encoder.setInputs(0, 0, 0, 1)
print "\n---To get the input states---"
print "encoder.getInputStates()"
print encoder.getInputStates()
print "\n---New output of encoder---"
print encoder.output()
print "\n\n---Using Connectors as the input lines---"
print "Take a Connector"
print "conn = Connector()"
conn = Connector()
print "\n---Set Output of decoder to Connector conn---"
print "encoder.setOutput(conn)"
encoder.setOutput(1, conn)
print "\n---Put this connector as the input to gate1---"
print "gate1 = AND(conn, 0)"
gate1 = AND(conn, 1)
print "\n---Output of the gate1---"
print "gate1.output()"
print gate1.output()

