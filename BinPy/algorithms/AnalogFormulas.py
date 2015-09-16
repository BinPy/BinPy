from __future__ import division


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

        if sum(j is None for j in values) > 2:
            raise Exception('Atleast two parameters required')

        if (any((j is not None and j < 0) for j in values)):
            raise Exception('enter positive values')
        else:
            if not p:
                if not r:
                    r = v / i
                    p = v * i
                if not v:
                    v = i * r
                    p = (i ** 2) * r
                if not i:
                    i = v / r
                    p = (v ** 2) / r
            else:
                if not v and not r:
                    v = p / i
                    r = p / (i ** 2)
                if not i and not r:
                    i = p / v
                    r = p / (i ** 2)
                if not i and not v:
                    i = sqrt(p / r)
                    v = i * r
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

        if sum(j is None for j in values) > 3:
            raise Exception('Atleast three parameters required')

        if (any((j is not None and j < 0) for j in values)):
            raise Exception('enter positive values')
        else:
            if not p:
                if not z:
                    z = v / i
                    p = v * i * c
                if not v:
                    v = i * z
                    p = i ** 2 * z * c
                if not i:
                    i = v / z
                    p = (v ** 2 * c) / z
                if not c:
                    raise Exception('Enter value of \'c\' .Since \'p\' \
                        and \'c\' cant be unknowns at the same time. ')
            else:
                if not v and not z:
                    v = p / (i * c)
                    z = p / (i ** 2)
                if not i and not z:
                    i = p / v
                    z = p / ((i ** 2) * c)
                if not i and not v:
                    i = sqrt(p / (z * c))
                    v = i * z
                if not c and not v:
                    c = p / (i ** 2 * z)
                    v = i * z
                if not c and not i:
                    i = v / z
                    c = p / (v * i)
                if not c and not z:
                    z = v / i
                    c = p / (v * i)
            print(values)
            return {'i': i, 'v': v, 'z': z, 'p': p, 'c': c}
