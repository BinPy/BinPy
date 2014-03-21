class OhmsLaw:

    '''
    This class implements Ohm's law for circuit analysis
    It requires any two parameters and it will calculate the other two.

    Example
    =======

    >>> myCalc = OhmsLaw()
    >>> myCalc.evaluate(p=1254.8,i=7.5)
    {'i': 7.5, 'p': 1254.8, 'r': 22.307555555555556, 'v': 167.30666666666667}

    Methods:
        evaluate(i=None,v=None,r=None,p=None)
    '''

    def evaluate(self, i=None, v=None, r=None, p=None):
        '''
        This method returns a dictionary of current, voltage, power,
        and resistance
        DictKeys: 'i', 'v', 'r', 'p'
        '''
        values = [i, v, r, p]
        if (any((j is not None and j < 0) for j in values)):
            raise Exception('enter positive values')
        else:
            if not p:
                if not r:
                    r = float(v / i)
                    p = float(v) * i
                if not v:
                    v = float(i) * r
                    p = float(i) ** 2 * r
                if not i:
                    i = float(v) / r
                    p = float(v) ** 2 / r
            else:
                if not v and not r:
                    v = float(p) / i
                    r = float(p) / i ** 2
                if not i and not r:
                    i = float(p) / v
                    r = float(p) / i ** 2
                if not i and not v:
                    i = sqrt(float(p) / r)
                    v = float(i) * r
            print(values)
            return {'i': i, 'v': v, 'r': r, 'p': p}


class OhmsLaw_AC:

    '''
    This class implements Ohm's law for circuit analysis using AC current
    It requires any three parameters and it will calculate the other two.

    How to use:
        >>> myCalc = OhmsLaw_AC()
        >>> myCalc.evaluate(p=1254.8,i=7.5,cos=2.0)
        >>> {'i': 7.5, 'p': 1254.8, 'r': 11.15, 'v': 83.625}

    Methods:
        evaluate(i=None,v=None,z=None,p=None,cos=None)
    '''

    def evaluate(self, i=None, v=None, z=None, p=None, c=None):
        '''
        This method returns a dictionary of current, voltage, power,
        resistance and cosine
        DictKeys: 'i', 'v', 'z', 'p','c'
        '''
        values = [i, v, z, p, c]
        if (any((j is not None and j < 0) for j in values)):
            raise Exception('enter positive values')
        else:
            if not p:
                if not z:
                    z = float(v) / i
                    p = float(v) * i * c
                if not v:
                    v = float(i) * z
                    p = float(i) ** 2 * z * c
                if not i:
                    i = float(v / z)
                    p = float((v ** 2 * c) / z)
                if not c:
                    raise Exception('Enter value of \'c\' .Since \'p\' \
                        and \'c\' cant be unknowns at the same time. ')
            else:
                if not v and not z:
                    v = float(p) / (i * c)
                    z = float(p) / (i ** 2)
                if not i and not z:
                    i = float(p) / v
                    z = float(p) / ((i ** 2) * c)
                if not i and not v:
                    i = sqrt(float(p) / (z * c))
                    v = float(i) * z
                if not c and not v:
                    c = float(p) / (i ** 2 * z)
                    v = float(i) * z
                if not c and not i:
                    i = float(v / z)
                    c = float(p / (v * i))
                if not c and not z:
                    z = float(v / i)
                    c = float(p / (v * i))
            print(values)
            return {'i': i, 'v': v, 'z': z, 'p': p, 'c': c}
