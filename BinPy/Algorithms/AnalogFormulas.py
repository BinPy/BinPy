
class OhmsLaw:
    '''
    This class implements Ohm's law for circuit analysis
    It requires any two parameters and it will calculate the other two.

    How to use:
        >>> myCalc = OhmsLaw()
        >>> myCalc.evaluate(p=1254.8,i=7.5)
        >>> {'i': 7.5, 'p': 1254.8, 'r': 22.307555555555556, 'v': 167.30666666666667}

    Methods:
        evaluate(i=None,v=None,r=None,p=None)
    '''
    def evaluate(self,i=None,v=None,r=None,p=None):
        '''
        This method returns a dictionary of current, voltage, power, and resistance
        DictKeys: 'i', 'v', 'r', 'p'
        '''
        values = [i, v, r, p]
        if (any((j != None and j < 0) for j in values)):
            raise Exception('enter positive values')
        else:
            if not p:
                if i and v and not r:
                    r = float(v/i)
                    p = v*i
                if i and r and not v:
                    v = i*r
                    p = (i**2)*r
                if v and r and not i:
                    i = float(v/r)
                    p = float((v**2)/r)
            else:
                if p and i and not v and not r:
                    v = float(p)/i
                    r = float(p)/(i**2)
                if p and v and not i and not r:
                    i = float(p)/v
                    r = float(p)/(i**2)
                if p and r and not i and not v:
                    i = sqrt(float(p)/r)
                    v = i*r
            print(values)
            return {'i':i,'v':v,'r':r,'p':p}
