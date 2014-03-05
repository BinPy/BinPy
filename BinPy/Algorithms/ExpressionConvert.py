def makeCompatible(expr):
    '''Used by convertExpression to convert logical operators to english words.'''
    expr.replace('&', 'AND')
    expr.replace('|', 'OR')
    expr.replace('~', 'NOT')
    expr.replace('^', 'XOR')
    expr.replace('~&', 'NAND')
    expr.replace('~|', 'NOR')
    return '('+expr+')'


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
                sublist.append (')')
                string = string[index+1:]
            sublist.append(string)
            list3.extend(sublist)
        else:
            list3.extend([string])

    while ('' in list3):
        list3.remove('')
    return (list3)


def mergeNot(expr):
    '''Combines NOR gate with othes to minimize the number of gates used.'''
    if expr[-1] == ')':
        index = expr.find('(')
        gate = expr[:index].upper()
        if gate == 'OR':
            return 'NOR' + expr[index:]
        elif gate == 'AND':
            return 'NAND' + expr[index:]
        elif gate == 'NOT':
            return expr[index+1:-1]
        elif gate == 'XOR':
            return 'XNOR' + expr[index:]
        elif gate == 'XNOR':
            return 'XOR' + expr[index:]
        elif gate == 'NAND':
            return 'AND' + expr[index:]
        elif gate == 'NOR':
            return 'OR' + expr[index:]
    return 'NOT(' + expr + ')'  


def convertExpression(expr, two_input=0):
    ''' Converts logical expression to the required form.
    Make two_input 1 if only two input gates must be used.
    Required Form: Each variable should be inputs of gates.
    '''
    expr = makeCompatible(expr)
    list1 = createList(expr)
    while ')' in list1:
        index = list1.index(')')
        if index != len(list1)-1 and list1[index+1] == ')':
            last = 0
        else:
            last = 1
        if len(list1) > 1:
            op2 = list1.pop(index-1)
            gate = list1.pop(index-2)
            gate = gate.upper()
            if gate != 'NOT':
                try:
                    op1 = list1.pop(index-3)
                except:
                    list1.insert(index-1, gate)
                    list1.insert(index-2, op2)
                    break
                if two_input == 0:
                    previous_gate = op1[:len(gate)]
                    previous_gate = previous_gate.upper()
                    next_gate = op2[:len(gate)]
                    next_gate = next_gate.upper()
                    if (gate == previous_gate) and (gate == next_gate.upper()):
                        new_element = gate + '(' + op1[len(gate)+1:-1] + ', ' + op2[len(gate)+1:-1] + ')'
                    elif (gate == previous_gate) and (gate != next_gate.upper()):
                        new_element = gate + '(' + op1[len(gate)+1:-1] + ', ' + op2 + ')'
                    elif (gate != previous_gate) and (gate == next_gate.upper()):
                        new_element = gate + '(' + op1 + ', ' + op2[len(gate)+1:-1] + ')'
                    else:
                        new_element = gate + '(' + op1 + ', ' + op2 + ')'
                else:
                    new_element = gate + '(' + op1 + ', ' + op2 + ')'
                list1.insert(index-3, new_element)
                if last != 1 or list1.index(')') == 1:
                        temp1 = list1.index(')')
                        temp2 = list1.pop(temp1)
            else:
                new_element = mergeNot(op2)
                list1.insert(index-2,new_element)
                temp1 = list1.index(')')
                temp2 = list1.pop(temp1)
    converted = list1[0]
    return converted
