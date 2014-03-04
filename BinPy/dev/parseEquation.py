from BinPy import *
import sys

global no_error
no_error = True

def removeBraces(position,equation):
    """
    Removes braces due to clubbing of the gates
    position indicates the index of the clubbed gate
    """
    eq = equation
    if position != -1:
        eq = equation[:position]
        stack = 0
        for i in equation[position:]:
            if ( i == '(' )  and ( stack != -1):
                stack += 1
                eq += i
                #print i,stack,eq
            elif ( i == ')' ) and ( stack !=-1 ):
                stack -= 1
                if stack == 0:
                    #If the current index corresponds to the ) of the removed gate.
                    stack = -1
                    #print i,stack,eq
                else:
                    eq += i
                    #print i,stack,eq
            else:
                eq += i
                #print i,stack,eq
    return eq

def findMatchingBrace(position,string):
    """
    Returns the index of the opposite matching brace for the brace at string[position]
    """
    #print eq
    stack = 0
    pos = position
    if position != -1:
        if string[pos] != '(':
            return -1
        for i in string[position:]:
            if ( i == '(' )  and ( stack != -1):
                stack += 1
            if ( i == ')' ) and ( stack != -1 ):
                stack -= 1
                if stack == 0:
                    return pos
            pos += 1
    return -1

def eqnParse(eqn,isOperandtype = str.isalpha):
    #The second parameter is to support the passing of equations for pin class [ only numbers ]
    
    #Removes white spaces.    
    eqn = eqn.replace(' ','')
    equation_final = ''
    
    operators = []  #Stack of operators
    operands = []  #Stack of operands
    
    global no_error
    
    flag = False
    
    i = 0
    
    while i < len(eqn):
        #print eqn[i]
        if not no_error:
            break
        if eqn[i] in [ '~','&','|','^']:
            if flag:
                operands.append(eqn[i-1])
                flag = False
            operators.append(eqn[i])
        elif eqn[i]=='(':
            if flag:
                print 'ERROR: Equation error at '+eqn[i-1:i+1]
                no_error = False
                break
            pos = findMatchingBrace(i,eqn)
            if pos == -1:
                print 'ERROR: Equation error - Unmatched braces'
                no_error = False
                break
            tmp = eqnParse(eqn[i+1:pos])
            operands.append(tmp)
            i = pos
        elif isOperandtype(eqn[i]):
            if flag:
                #2 letter operand [ eg 12 --> corresponds to PIN 12 ]
                operands.append(eqn[i-1:i+1])                
                flag = False
            else:
                flag = True
                #Check if the operand is a two letter operand, in the next iteration.
        else:
            print 'ERROR: Unrecognized characters in equation '+eqn[i]
            no_error = False
        i += 1
        
    if flag:
        operands.append(eqn[-1])
        flag = False
    
    if not no_error:
        return        
    #print operators
    
    while len(operators) > 0:
        operator = operators.pop()
        if operator == '~':
            operands.append('NOT('+operands.pop()+')')
        elif operator == '&':
            operands.append('AND('+operands.pop()+','+operands.pop()+')')
        elif operator == '|':
            operands.append('OR('+operands.pop()+','+operands.pop()+')')
        elif operator == '^':
            operands.append('XOR('+operands.pop()+','+operands.pop()+')')

    equation_final = operands.pop()
    #print equation_final
    
    #Optimizing the final equation by clubbing the gates together:
    
    unoptimized = True
    while unoptimized:
        unoptimized = False
        pos = equation_final.find('NOT(AND(') 
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NOT(AND(','NAND(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
        
        pos = equation_final.find('NOT(OR(')    
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NOT(OR(','NOR(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
        
        pos = equation_final.find('NOT(XOR(')    
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NOT(XOR(','XNOR(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
        
        pos = equation_final.find('AND(AND(')
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('AND(AND(','AND(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
            
        pos = equation_final.find('OR(OR(')
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('OR(OR(','OR(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
            
        pos = equation_final.find('XOR(XOR(')
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('XOR(XOR(','XOR(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
        
        pos = equation_final.find('NAND(NAND(')
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NAND(NAND(','NAND(',1)
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
        
        pos = equation_final.find('NOR(NOR(',1)
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NOR(NOR(','NOR(')
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
            
        pos = equation_final.find('XNOR(XNOR(',1)
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('XNOR(XNOR(','XNOR(')
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
            
        pos = equation_final.find('NAND(AND(',1)
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NAND(AND(','NAND(')
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
            
        pos = equation_final.find('NOR(OR(',1)
        if pos != -1:
            unoptimized = True
            equation_final = equation_final[:pos]+equation_final[pos:].replace('NOR(OR(','NOR(')
            equation_final = removeBraces(pos,equation_final)
            #print equation_final
    
    return equation_final if no_error else None
    
#Uncomment to test:    

print eqnParse('~((((~A)&B&C)^(~A))&E&F&G)')
#NAND(G,F,E,XOR(NOT(A),AND(C,B,NOT(A))))
#print findMatchingBrace(2,'((((((()))))abcedfljk(()))a&b)')