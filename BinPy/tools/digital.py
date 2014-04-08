class DigitDisplay:

    '''
    This class emulates a 7 segmented display(Common Cathode)

    Parameters:
        name:   A name given to an object(Optional)

    Methods:
        evaluate()
        getName()

    How to use:
        >>> myDisplay = DigitDisplay("Display1")
        >>> print myDisplay.evaluate([1,1,1,1,1,1,1])
        8
    Note:
        You can either pass complete list of 10 pins [pin1, pin2, pin3,
        pin4, pin5, pin6, pin7, pin8, pin9, pin10] in standard order or
        you can directly pass the list of values corresponding to a, b,
        c, d, e, f and g in lexicographical order.

    Reference
    =========

    http://tronixstuff.files.wordpress.com/2010/05/7segpinout.jpg
    '''

    def __init__(self, name=None):
        self.name = name

    def evaluate(self, pin_conf):
        '''
        This method evaluates the values passed according to the display and returns
        an integer varying from 0 to 9
        '''
        if len(pin_conf) != 10:
            if len(pin_conf) != 7:
                raise Exception("There must be 10 or 7 values")
        if len(pin_conf) == 10:
            vcc = pin_conf[2] or pin_conf[7]
            a = pin_conf[6]
            b = pin_conf[5]
            c = pin_conf[3]
            d = pin_conf[1]
            e = pin_conf[0]
            f = pin_conf[8]
            g = pin_conf[9]
        if len(pin_conf) == 7:
            a = pin_conf[0]
            b = pin_conf[1]
            c = pin_conf[2]
            d = pin_conf[3]
            e = pin_conf[4]
            f = pin_conf[5]
            g = pin_conf[6]
            vcc = 1
        if vcc:
            test = [a, b, c, d, e, f, g]
            data = {
                '0': [1, 1, 1, 1, 1, 1, 0],
                '1': [0, 1, 1, 0, 0, 0, 0],
                '2': [1, 1, 0, 1, 1, 0, 1],
                '3': [1, 1, 1, 1, 0, 0, 1],
                '4': [0, 1, 1, 0, 0, 1, 1],
                '5': [1, 0, 1, 1, 0, 1, 1],
                '6': [1, 0, 1, 1, 1, 1, 1],
                '7': [1, 1, 1, 0, 0, 0, 0],
                '8': [1, 1, 1, 1, 1, 1, 1],
                '9': [1, 1, 1, 1, 0, 1, 1]}
            for i in data:
                if test == data[i]:
                    return int(i)
            print ('Not a valid combination')
            return None
        else:
            return None

        def getName(self):
            return self.name
