from BinPy import *
from nose.tools import with_setup, nottest

def AND_test():
    lgate = AND(1,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0],logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [0, 0, 1, 0]:
        assert False

def OR_test():
    lgate = OR(0,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0], logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [0, 1, 1, 1]:
        assert False

def NAND_test():
    lgate = NAND(0,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0],logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [1, 1, 0, 1]:
        assert False

def NOR_test():
    lgate = NOR(0,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0],logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [1, 0, 0, 0]:
        assert False

def XOR_test():
    lgate = XOR(0,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0],logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [0, 1, 0, 1]:
        assert False

def XNOR_test():
    lgate = XNOR(0,0)
    outputLogic = []

    inputLogic = [(0, 0), (1, 0), (1, 1), (0, 1)]

    for logic in inputLogic:
        lgate.setInputs(logic[0],logic[1])
        outputLogic.append(lgate.output())
    print outputLogic
    if outputLogic != [1, 0, 1, 0]:
        assert False

######## IC's with 14 pins #################################

def test_IC_7400():
    testIC = IC_7400()
    p = {1:1,2:0,4:0,5:0,7:0,9:1,10:1,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {3:1,6:1,8:0,11:1}
    if q!=testIC.run():
        assert False

def test_IC_7401():
    testIC = IC_7401()
    p = {2:0,3:0,5:0,6:1,7:0,8:1,9:1,11:1,12:1,14:1}
    testIC.setIC(p)
    q = {1:1,4:1,10:0,13:0}
    if q!=testIC.run():
        assert False

def test_IC_7402():
    testIC = IC_7402()
    p = {2:0,3:0,5:0,6:1,7:0,8:1,9:1,11:1,12:1,14:1}
    testIC.setIC(p)
    q = {1:1,4:0,10:0,13:0}
    if q!=testIC.run():
        assert False

def test_IC_7403():
    testIC = IC_7403()
    p = {1:1,2:0,4:0,5:0,7:0,9:1,10:1,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {3:1,6:1,8:0,11:1}
    if q!=testIC.run():
        assert False

def test_IC_7404():
    testIC = IC_7404()
    p = {1:1,3:0,5:0,7:0,9:0,11:0,13:1,14:1}
    testIC.setIC(p)
    q = {2:0,4:1,6:1,8:1,10:1,12:0}
    if q!=testIC.run():
        assert False

def test_IC_7405():
    testIC = IC_7405()
    p = {1:1,3:0,5:0,7:0,9:0,11:0,13:1,14:1}
    testIC.setIC(p)
    q = {2:0,4:1,6:1,8:1,10:1,12:0}
    if q!=testIC.run():
        assert False

def test_IC_7408():
    testIC = IC_7408()
    p = {1:1,2:0,4:0,5:0,7:0,9:1,10:1,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {3:0,6:0,8:1,11:0}
    if q!=testIC.run():
        assert False

def test_IC_7410():
    testIC = IC_7410()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {12:1,6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7411():
    testIC = IC_7411()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {12:0,6:0,8:1}
    if q!=testIC.run():
        assert False

def test_IC_7412():
    testIC = IC_7412()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {12:1,6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7413():
    testIC = IC_7413()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7415():
    testIC = IC_7415()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {12:0,6:0,8:1}
    if q!=testIC.run():
        assert False

def test_IC_7416():
    testIC = IC_7416()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {2:0,4:1,6:1,8:0,10:0,12:1}
    if q!=testIC.run():
        assert False

def test_IC_7417():
    testIC = IC_7417()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {2:1,4:0,6:0,8:1,10:1,12:0}
    if q!=testIC.run():
        assert False

def test_IC_7418():
    testIC = IC_7418()
    p = {1:1,2:0,3:0,4:0,5:0,9:1,10:1,11:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7419():
    testIC = IC_7419()
    p = {1:1,2:0,13:0,3:0,4:0,5:0,9:1,10:1,11:1,14:1,7:0}
    testIC.setIC(p)
    q = {2:0,4:1,6:1,8:0,10:0,12:1}
    if q!=testIC.run():
        assert False

def test_IC_7420():
    testIC = IC_7420()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7421():
    testIC = IC_7421()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:0,8:1}
    if q!=testIC.run():
        assert False

def test_IC_7422():
    testIC = IC_7422()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7424():
    testIC = IC_7424()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {3:1,6:1,8:0,11:0}
    if q!=testIC.run():
        assert False

def test_IC_7425():
    testIC = IC_7425()
    p = {1:0,2:0,3:0,4:0,5:0,9:1,10:1,11:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7426():
    testIC = IC_7426()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {3:1,6:1,8:0,11:0}
    if q!=testIC.run():
        assert False

def test_IC_7427():
    testIC = IC_7427()
    p = {1:1,2:0,3:0,4:0,5:0,9:1,10:1,11:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0,12:0}
    if q!=testIC.run():
        assert False

def test_IC_7428():
    testIC = IC_7428()
    p = {2:0,3:0,5:0,6:1,8:1,9:1,11:1,12:1,14:1,7:0}
    testIC.setIC(p)
    q = {1:1,4:0,10:0,13:0}
    if q!=testIC.run():
        assert False

def test_IC_7430():
    testIC = IC_7430()
    p = {1:0,2:1,3:1,4:1,5:1,6:1,11:1,12:1,14:1,7:0}
    testIC.setIC(p)
    q = {8:1}
    if q!=testIC.run():
        assert False

def test_IC_7432():
    testIC = IC_7432()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {3:1,6:0,8:1,11:1}
    if q!=testIC.run():
        assert False

def test_IC_7433():
    testIC = IC_7433()
    p = {2:0,3:0,5:0,6:0,8:1,9:1,11:1,12:1,14:1,7:0}
    testIC.setIC(p)
    q = {1:1,4:1,10:0,13:0}
    if q!=testIC.run():
        assert False

def test_IC_7437():
    testIC = IC_7437()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {3:1,6:1,8:0,11:0}
    if q!=testIC.run():
        assert False

def test_IC_7440():
    testIC = IC_7440()
    p = {1:1,2:0,4:0,5:0,9:1,10:1,12:1,13:1,14:1,7:0}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False


def test_IC_7451():
    testIC = IC_7451()
    p = {2:1,3:0,4:0,5:0,7:0,1:1,13:1,12:1,11:0,10:0,9:0,14:1}
    testIC.setIC(p)
    q = {6:1,8:0}
    if q!=testIC.run():
        assert False

def test_IC_7454():
    testIC = IC_7454()
    p = {1:1,2:0,3:0,4:0,7:0,10:1,9:1,11:0,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {6:1}
    if q!=testIC.run():
        assert False
 
def test_IC_7455():
    testIC = IC_7455()
    p = {1:1,2:0,3:0,4:0,7:0,10:1,9:1,11:0,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {8:1}
    if q!=testIC.run():
        assert False

def test_IC_7458():
    testIC = IC_7458()
    p = {2:0,3:0,4:0,5:0,7:0,1:1,13:1,12:1,11:0,10:0,9:0,14:1}
    testIC.setIC(p)
    q = {6:0,8:1}
    if q!=testIC.run():
        assert False

def test_IC_7464():
    testIC = IC_7464()
    p = {1:1,7:0,13:1,12:1,11:1,14:1}
    testIC.setIC(p)
    q = {8:0}
    if q!=testIC.run():
        assert False

def test_IC_7486():
    testIC = IC_7486()
    p = {1:0,2:0,4:0,5:1,7:0,9:1,10:0,12:1,13:1,14:1}
    testIC.setIC(p)
    q = {3:0,6:1,8:1,11:0}
    if q!=testIC.run():
        assert False

def test_IC_74260():
    testIC = IC_74260()
    p = {1:0,2:0,3:0,4:1,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:1}
    testIC.setIC(p)
    q = {5:1,6:0}
    if q!=testIC.run():
        assert False

######## IC's with 5 pins #################################

def test_IC_741G00():
     testIC = IC_741G00()
     p = {1:1,2:0,3:0,5:1}
     testIC.setIC(p)
     q = {4:1}
     if q!=testIC.run():
        assert False

def test_IC_741G02():
    testIC = IC_741G02()
    p = {1:1,2:0,3:0,5:1}
    testIC.setIC(p)
    q = {4:0}
    if q!=testIC.run():
        assert False

def test_IC_741G03():
    testIC = IC_741G03()
    p = {1:1,2:0,3:0,5:1}
    testIC.setIC(p)
    q = {4:1}
    if q!=testIC.run():
        assert False
def test_IC_741G04():
    testIC = IC_741G04()
    p = {2:0,3:0,5:1}
    testIC.setIC(p)
    q = {4:1}
    if q!=testIC.run():
        assert False

def test_IC_741G05():
    testIC = IC_741G05()
    p = {2:1,3:0,5:1}
    testIC.setIC(p)
    q = {4:0}
    if q!=testIC.run():
        assert False

def test_IC_741G08():
    testIC = IC_741G08()
    p = {1:1,2:0,3:0,5:1}
    testIC.setIC(p)
    q = {4:0}
    if q!=testIC.run():
        assert False

######## IC's with 16 pins #################################  

def test_IC_7431():
    testIC = IC_7431()
    p = {1:1,5:0,6:0,15:1,10:1,11:1,3:1,13:0,8:0,16:1}
    testIC.setIC(p)
    q = {2:0,7:1,14:0,9:0,4:1,12:0}
    if q!=testIC.run():
        assert False

def test_IC_7442():
    testIC = IC_7442()
    p = {15:1,14:0,13:0,12:0,8:0,16:1}
    testIC.setIC(p)
    q = {1:1,2:0,3:1,4:1,5:1,6:1,7:1,9:1,10:1,11:1}
    if q!=testIC.run():
        assert False

def test_IC_7443():
    testIC = IC_7443()
    p = {15:1,14:0,13:1,12:0,8:0,16:1}
    testIC.setIC(p)
    q = {1:1,2:1,3:0,4:1,5:1,6:1,7:1,9:1,10:1,11:1}
    if q!=testIC.run():
        assert False

def test_IC_7444():
    testIC = IC_7444()
    p = {15:1,14:0,13:1,12:0,8:0,16:1}
    testIC.setIC(p)
    q = {1:1,2:1,3:1,4:0,5:1,6:1,7:1,9:1,10:1,11:1}
    if q!=testIC.run():
        assert False
        
def test_IC_7445():
    testIC = IC_7445()
    p = {15:0,14:0,13:1,12:0,8:0,16:1}
    testIC.setIC(p)
    q = {1:1,2:1,3:1,4:1,5:0,6:1,7:1,9:1,10:1,11:1}
    if q!=testIC.run():
        assert False

def test_IC_74133():
    testIC = IC_74133()
    p = {1:0,2:1,3:1,4:1,5:1,6:1,7:1,8:0,9:1,10:1,12:1,13:1,14:1,15:1,16:1}
    testIC.setIC(p)
    q = {9:1}
    if q!=testIC.run():
        assert False
        
def test_IC_4081():
    testIC = IC_4081()
    p = {1:0,2:0,5:0,6:1,8:1,9:0,12:1,13:1}
    testIC.setIC(p)
    q = {3: 0, 4: 0, 10: 0, 11: 1}
    if q!=testIC.run():
        assert False

def test_IC_4082():
    testIC = IC_4082()
    p = {2:1,3:1,4:1,5:1,9:1,10:1,11:1,12:0,14:1}
    testIC.setIC(p)
    q = {1:1,13:0}
    if q!=testIC.run():
        assert False
