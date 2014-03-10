from __future__ import print_function
from BinPy.Operations.operations import *
""" Examples for operations class """
print ("\n-----Initialize the operation class-----")
print ("op = Operations()")
op = Operations()
print ("\n-----Binary Addition------ ")
print ("op.ADD('0', '1'), op.ADD('00', '10'), op.ADD('010', '100')")
print (op.ADD('0', '1'), op.ADD('00', '10'), op.ADD('010', '100'))
print ("\n-----Binary Subtraction-----")
print ("op.SUB('1', '0'), op.SUB('00', '10'), op.SUB('010', '100')")
print (op.SUB('1', '0'), op.SUB('00', '10'), op.SUB('010', '100'))
print ("\n-----Binary Multiplication----")
print ("op.MUL('0', '1'), op.MUL('00', '10'), op.MUL('010', '100')")
print (op.MUL('0', '1'), op.MUL('00', '10'), op.MUL('010', '100'))
print ("\n-----Binary Division-----")
print ("op.DIV('0', '1'), op.DIV('00', '10'), op.DIV('010', '100')")
print (op.DIV('0', '1'), op.DIV('00', '10'), op.DIV('010', '100'))
print ("\n-----Binary Complement-----")
print (
    "op.COMP('0', '1'), op.COMP('00', '1'), op.COMP('00', '2'), op.COMP('010', '1')")
print (
    op.COMP(
        '0', '1'), op.COMP(
        '00', '1'), op.COMP(
        '00', '2'), op.COMP(
        '010', '1'))
print ("\n-----Conversion from binary to decimal-----")
print (Operations.binToDec('111'))
print ("\n-----Conversion from decimal to binary-----")
print (Operations.decToBin(12))
