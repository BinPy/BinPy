__To Show how logic class works__

```
In [10]: logicval = logic()

In [11]: logicval2 = logic(1)

In [12]: logicval ^ logicval2
```

Logical operation between any two (or more logic instances ) returns a logic instance

```
Out[12]: <BinPy.ic.base.logic instance at 0x2a0fb00>

In [13]: ans = logicval ^ logicval2
```

Logic instance when called returns its value:

```

In [14]: ans()
Out[14]: 1

```

__BASIC Gates:__

__EXOR-GATE__

```
In [0]: ( logic(1) ^ logic(0) ) ()
Out[0]: 1
```
__EXNOR-GATE__

```
In [2]: ( ~( logic(1) ^ logic(0) )) ()
Out[2]: 0
```
__OR-GATE__

```
In [9]: ( logic(1) | logic(0) ) ()
Out[9]: 1
```
__NOR-GATE__

```
In [10]: (~( logic(1) | logic(0) )) ()
Out[10]: 1
```

__AND-GATE__

```
In [11]: ( logic(1) & logic(0) ) ()
Out[11]: 0
```

__NAND-GATE__

```
In [12]: (~( logic(1) & logic(0) )) ()
Out[12]: 1
```

__NOT-GATE__

```
In [10]: ~( logic(1) ) ()
Out[10]: 0
```

__RandomEquation__

```
In [27]: ( ( logic(1) | logic(0) ) & ( logic(1) | logic(1) ) ) ()
Out[27]: 1
```
