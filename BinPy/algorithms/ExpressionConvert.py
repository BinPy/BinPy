def makeCompatible(expr):
    '''Used by convertExpression to convert logical operators to english words.'''
    expr = expr.replace('~&', ' NAND ')
    expr = expr.replace('~|', ' NOR ')
    expr = expr.replace('~^', ' XNOR ')
    expr = expr.replace('&', ' AND ')
    expr = expr.replace('|', ' OR ')
    expr = expr.replace('~', ' NOT ')
    expr = expr.replace('^', ' XOR ')
    return '((' + expr + '))'


def createList(expr):
    '''Creates a list which can be used by convertExpression for conversion.'''
    list1 = expr.split('(')
    list2 = []
    list3 = []
    while ('' in list1):
        list1.remove('')

    for string in list1:
        l = string.split()
        list2.extend(l)

    for string in list2:
        sublist = []
        if ')' in string:
            while ')' in string:
                index = string.find(')')
                sublist.append(string[:index])
                sublist.append(')')
                string = string[index + 1:]
            sublist.append(string)
            list3.extend(sublist)
        else:
            list3.extend([string])

    while ('' in list3):
        list3.remove('')
    return (list3)


def mergeNot(case, expr):
    '''Combines NOR gate with othes to minimize the number of gates used.'''
    if expr[-1] == ')':
        index = expr.find('(')
        gate = expr[:index].upper()
        if gate == 'OR' and case == 'general':
            return 'NOR' + expr[index:]
        elif gate == 'AND' and case == 'general':
            return 'NAND' + expr[index:]
        elif gate == 'NOT':
            return expr[index + 1:-1]
        elif gate == 'XOR'and case == 'general':
            return 'XNOR' + expr[index:]
        elif gate == 'XNOR'and case == 'general':
            return 'XOR' + expr[index:]
        elif gate == 'NAND'and case == 'general':
            return 'AND' + expr[index:]
        elif gate == 'NOR'and case == 'general':
            return 'OR' + expr[index:]
    return 'NOT(' + expr + ')'


def to_and_or_not(gate, op1, op2):
    '''Converts a general two input gate and two of its operands to use only OR, NOT, or AND gates'''
    if gate == 'AND' or gate == 'OR':
        return gate + '(' + op1 + ', ' + op2 + ')'
    elif gate == 'NAND':
        return 'NOT(AND(' + '(' + op1 + ', ' + op2 + ')'
    elif gate == 'NOR':
        return 'NOT(OR(' + '(' + op1 + ', ' + op2 + ')'
    elif gate == 'XOR':
        return ('OR(AND(' + op1 + ', ' + mergeNot('general', op2)
                + '), AND(' + mergeNot('general', op1) + ', ' + op2 + '))')
    elif gate == 'XNOR':
        return (
            'OR(AND(' +
            mergeNot(
                'general',
                op1) +
            ', ' +
            mergeNot(
                'general',
                op2) +
            '), AND(' +
            op1 +
            ', ' +
            op2 +
            '))')


def to_nand(gate, op1, op2):
    '''Converts a general two input gate and two of its operands to use only NAND gates'''
    if gate == 'AND':
        return 'NOT(NAND(' + op1 + ', ' + op2 + '))'
    elif gate == 'OR':
        return ('NAND(' + mergeNot('special', op1) + ', '
                + mergeNot('special', op2) + ')')
    elif gate == 'NAND':
        return gate + '(' + op1 + ', ' + op2 + ')'
    elif gate == 'NOR':
        return 'NOT(' + to_nand('OR', op1, op2) + ')'
    elif gate == 'XOR':
        return (
            'NAND(NAND(' +
            op1 +
            ', NAND(' +
            op1 +
            ', ' +
            op2 +
            ')), NAND(' +
            op2 +
            ', NAND(' +
            op1 +
            ', ' +
            op2 +
            ')))')
    elif gate == 'XNOR':
        return 'NOT(' + to_nand('XOR', op1, op2) + ')'


def to_nor(gate, op1, op2):
    '''Converts a general two input gate and two of its operands to use only NOR gates'''
    if gate == 'OR':
        return 'NOT(NOR(' + op1 + ', ' + op2 + '))'
    elif gate == 'AND':
        return ('NOR(' + mergeNot('special', op1) + ', '
                + mergeNot('special', op2) + ')')
    elif gate == 'NOR':
        return gate + '(' + op1 + ', ' + op2 + ')'
    elif gate == 'NAND':
        return 'NOT(' + to_nor('AND', op1, op2) + ')'
    elif gate == 'XNOR':
        return ('NOR(NOR(' + op1 + ', NOR(' + op1 + ', '
                + op2 + ')), NOR(' + op2 + ', NOR(' + op1 + ', ' + op2 + ')))')
    elif gate == 'XOR':
        return 'NOT(' + to_nor('XNOR', op1, op2) + ')'


def remove_not(gate, exp):
    '''Converts a NOT gate and its operand to use the specified gate only.
    The input gate must be NAND or NOR only.'''
    while 'NOT' in exp:
        index = exp.find('NOT(')
        index2 = index
        index3 = exp.find('(', index)
        while True:
            index2 = exp.find(')', index2 + 1)
            index3 = exp.find('(', index3 + 1)
            if index3 == -1 or index3 > index2:
                break
        exp = exp[:index] + gate + '(' + exp[index + 4:index2] + \
            ', ' + exp[index + 4:index2] + ')' + exp[index2 + 1:]
    return exp


def convertExpression(expr, two_input=0, only_nand=0,
                      only_nor=0, only_and_or_not=0):
    ''' Converts logical expression to an implementable form.
    Make two_input 1 if only two input gates must be used.
    Make only_nand 1 if only 2 input nand gates must be used.
    Make only_nor 1 if only 2 input nor gates must be used.
    Make only_and_or_not 1 if only 2 input AND, OR and NOTs be used.
    Error occurs if more than one variable is put to 1.

    convertExpression('( NOT(a) and NOT(b)) or (C and Not(d) and E and F)')
    OR(AND(NOT(a), NOT(b)), AND(C, NOT(d), E, F))

    convertExpression('( NOT(a) and NOT(b)) or (C and Not(d) and E and F)', two_input=1)
    OR(AND(NOT(a), NOT(b)), AND(C, AND(NOT(d), E)))

    convertExpression('( NOT(a) and NOT(b)) or (C and Not(d) and E and F)', only_nand=1)
    NAND(NAND(NAND(a, a), NAND(b, b)), NAND(C, NAND(NAND(NAND(d, d), E), NAND(NAND(d, d), E))))

    convertExpression('( NOT(a) and NOT(b)) or (C and Not(d) and E and F)', only_nor=1)
    NOR(NOR(NOR(a, b), NOR(NOR(C, C), NOR(NOR(d, NOR(E, E)),...
    NOR(d, NOR(E, E))))), NOR(NOR(a, b), NOR(NOR(C, C), NOR(NOR(d, NOR(E, E)), NOR(d, NOR(E, E))))))

    convertExpression('( NOT(a) and NOT(b)) or (C and Not(d) and E and F)', only_and_or_not=1)
    OR(AND(NOT(a), NOT(b)), AND(C, AND(NOT(d), AND(E, F))))
    '''
    expr = makeCompatible(expr)
    list1 = createList(expr)
    while ')' in list1:
        index = list1.index(')')
        if index != len(list1) - 1 and list1[index + 1] == ')':
            last = 0
        else:
            last = 1
        if len(list1) > 1:
            op2 = list1.pop(index - 1)
            gate = list1.pop(index - 2)
            gate = gate.upper()
            if gate != 'NOT':
                try:
                    op1 = list1.pop(index - 3)
                except:
                    list1.insert(index - 1, gate)
                    list1.insert(index - 2, op2)
                    break
                previous_gate = op1[:len(gate)]
                previous_gate = previous_gate.upper()
                next_gate = op2[:len(gate)]
                next_gate = next_gate.upper()
                if (two_input == 0 and gate != 'NAND'and gate != 'NOR')and (
                        only_nand == 0 and only_nor == 0 and only_and_or_not == 0):
                    if (gate == previous_gate) and (gate == next_gate.upper()):
                        new_element = gate + \
                            '(' + op1[len(gate) + 1:-1] + \
                            ', ' + op2[len(gate) + 1:-1] + ')'
                    elif (gate == previous_gate) and (gate != next_gate.upper()):
                        new_element = gate + \
                            '(' + op1[len(gate) + 1:-1] + ', ' + op2 + ')'
                    elif (gate != previous_gate) and (gate == next_gate.upper()):
                        new_element = gate + \
                            '(' + op1 + ', ' + op2[len(gate) + 1:-1] + ')'
                    else:
                        new_element = gate + '(' + op1 + ', ' + op2 + ')'
                else:
                    if only_nand == 0 and only_nor == 0 and only_and_or_not == 0:
                        new_element = gate + '(' + op1 + ', ' + op2 + ')'
                    elif only_nand == 1 and only_nor == 0 and only_and_or_not == 0:
                        new_element = to_nand(gate, op1, op2)
                    elif only_nand == 0 and only_nor == 1 and only_and_or_not == 0:
                        new_element = to_nor(gate, op1, op2)
                    elif only_nand == 0 and only_nor == 0 and only_and_or_not == 1:
                        new_element = to_and_or_not(gate, op1, op2)
                    else:
                        raise Exception("Invalid Input")
                list1.insert(index - 3, new_element)
                if (last != 1) or list1.index(')') == 1:
                    temp1 = list1.index(')')
                    temp2 = list1.pop(temp1)
            else:
                if only_nand == 0 and only_nor == 0 and only_and_or_not == 0:
                    new_element = mergeNot('general', op2)
                else:
                    new_element = mergeNot('special', op2)
                list1.insert(index - 2, new_element)
                temp1 = list1.index(')')
                temp2 = list1.pop(temp1)
            if list1.count(')') == len(list1) - 1:
                break
    if only_nand == 1:
        return (remove_not('NAND', list1[0]))
    elif only_nor == 1:
        return (remove_not('NOR', list1[0]))
    else:
        return (list1[0])
