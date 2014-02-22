-----------
# [BinPy](http://binpy.github.io/)
-----------

[![Build Status](https://travis-ci.org/BinPy/BinPy.png?branch=develop)](https://travis-ci.org/BinPy/BinPy)

 * [About](#about)
 * [Installation](#installation)
 * [Available Resources](#resources)
 * [Documentation](#documentation)
 * [Contribute](#contribute)


<a id="about"></a>
What is BinPy?
---------------
This package will serve as a base to develop circuit based applications or logical games on top of it. 
This package does not depend on any external library other than pure Python.

How to use
----------

Here's an example of SR latch constructed from a pair of cross-coupled NOR gates
![SR latch | Source: Wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/c6/R-S_mk2.gif)

```python
from BinPy import *

a = Connector()
b = Connector()

g1 = NOR(R,b)
g1.setOutput(a)    # SET OUTPUT as a

g2 = NOR(S,a) 
g2.setOutput()    # SET OUTPUT as b

print [g1.output(),g2.output]
```
<strong>Output</strong>
```python
Q:  True       Q':  False
Q:  False      Q':  True
Q:  False      Q':  True
Q:  False      Q':  False
```

<strong>Operations, Combinatonal Logic and Algorithms</strong>

```python
from BinPy import *

#Operations
operator = Operations()
operator.ADD(1011,11)
operator.SUB(1011,11)
operator.COMP('0011',1) #Second argument chooses betweem 1's or 2's Compliment


#Combinational Logic
d = Decoder([1,1,0,1])
d.output('01')

#Sequential Circuits
a = DFlipFlop(1,0)
a.output()

#Algorithms 
#Includes the Quine-McCluskey algorithm for solving K-Maps
FinalEquation = QM(['A','B'])
print "Minimized Boolean Equation : " , FinalEquation.get_function(qm.solve([0,1,2],[])[1])
```

<strong>Output</strong><br/>
```python
DFlipFlop Output: [1,0]
Minimized Boolean Equation : ((NOT B) OR (NOT A))
```

<a id="resources"></a>
Available Resources
-------------------
* All basic logic gates (NOT, OR, NOR, AND, NAND, XOR, XNOR)
* Combinational logics
	* Adder
	* Subtractor
	* Multiplier
	* MUX (2:1, 4:1, 8:1, 16:1)
	* DEMUX (1:2, 1:4, 1:8, 1:16)
	* Encoder
	
* IC
	* 7400
	* 741G00
	* 7401
	* 7402
	* 741G02
	* 7403
	* 741G03
	* 7404
	* 741G04
	* 7405
	* 741G05
	* 7408
	* 741G08
	* 7410
	* 7411
	* 7442
	* 7443
	* 7444
	* 7451
	* 7454
	* 7455
	* 7458
* Algorithms
	* Quine-McCluskey Algorithm (To find minimized Boolean Equation)
	* Moore Machine Optimizer

<a id="documentation"></a>
Documentation
-------------
Auto-generated documentation is available for reference at [BinPy docs](http://packages.python.org/BinPy/index.html)

<a id="installation"></a>
Installation
------------

### Linux

Install with **pip**

    sudo apt-get install pip setuptools ipython
    sudo pip install https://github.com/BinPy/BinPy/zipball/master

Install using **git**

    sudo apt-get install git setuptools ipython
    git clone https://github.com/BinPy/BinPy.git
    cd BinPy/
    sudo python setup.py install

    

Future Work
------------
* Introduction of all ICs
* Introduction of problem solving algorithms
* Addition of Microprocessors and Analog Devices
* Graphical representation of the circuit
* ...

<a id="contribute"></a>

How To Contribute
-----------------

 - [Report Bugs and Issues](https://github.com/BinPy/BinPy/issues)
 - [Solve Bugs and Issues](https://github.com/BinPy/BinPy/issues?page=1&state=open)
 - Write Tutorials, Examples and Documentation

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/mrsud/binpy/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

