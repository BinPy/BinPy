from ExpressionConvert import *
from QuineMcCluskey import *
import sys


def ImplementBooleanFn():
    ''' An interactive function which takes in minterms/maxterms and
    prints the Boolean Function and implementable form.
    Don't Care Conditions can also be provided (optional)
    Eg:
    Enter the list of variables
    A,B,C
    Do you want to enter minterms (m) or maxterms(M)?
    m
    Enter list of minterms
    1,4,7
    Enter list of Don't Care terms
    Enter X if there are none
    2,5
    The logical expression is (((NOT B) AND C) OR (A AND C) OR (A AND (NOT B)))
    Can be implemented as OR(AND(NOT(B), C), AND(A, C), AND(A, NOT(B)))
    '''

    Ones = []
    dont_care = []
    variables = input("Enter the list of variables\n")
    variables = variables.split(',')
    choice = input("Do you want to enter minterms (m) or maxterms(M)?\n")
    while(True):
        if choice == 'm':
            Ones = input("Enter list of minterms\n")
            Ones = Ones.split(',')
            for i in range(len(Ones)):
                Ones[i] = int(Ones[i])
                if Ones[i] >= pow(2, len(variables)):
                    raise Exception("Error: Invalid Minterm")
            break
        elif choice == 'M':
            Zeros = input("Enter list of maxterms\n")
            Zeros = Zeros.split(',')
            for i in range(len(Zeros)):
                Zeros[i] = int(Zeros[i])
                if Zeros[i] >= pow(2, len(variables)):
                    raise Exception("Error: Invalid Maxterm")
            for i in range(pow(2, len(variables))):
                if i not in Zeros:
                    Ones.append(i)
            break
        else:
            choice = input('''Invalid choice...
Enter either m or M to choose. Press X to exit\n''')
            if choice == 'X':
                sys.exit()
            else:
                continue
    dont_care = input(
        "Enter list of Don't Care terms\nEnter X if there are none\n")
    if dont_care != 'X':
        dont_care = dont_care.split(',')
        for i in range(len(dont_care)):
            dont_care[i] = int(dont_care[i])
    else:
        dont_care = None

    qm = QM(variables)
    if dont_care is not None:
        LogicalExpression = qm.get_function(qm.solve(Ones, dont_care)[1])
    else:
        LogicalExpression = qm.get_function(qm.solve(Ones)[1])
    GateForm = convertExpression(LogicalExpression)

    print("The logical expression is " + LogicalExpression)
    print("Can be implemented as " + GateForm)
