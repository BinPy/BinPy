from BinPy.Algorithms.AnalogFormulas import *
from nose.tools import with_setup, nottest

def test_OhmsLaw():
    test = OhmsLaw()
    q = {'i': 12, 'p': 24, 'r': 0.16666666666666666, 'v': 2.0}
   
    if q != test.evaluate(i=12,p=24):
        assert False
        
def test_OhmsLaw_AC():
    test = OhmsLaw_AC()
    q = {'i': 7.5, 'p': 1254.8, 'c': 11.153777777777778, 'z': 2.0, 'v': 15.0}
    
    if q != test.evaluate(p=1254.8,i=7.5,z=2.0):
        assert False
