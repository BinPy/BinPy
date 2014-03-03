import sys
import ast
from BinPy import * #Needed so that trial run of the synthesized code can be done

def getCode(icno):
    try:
        dict_of_vars = {}
        dict_of_vars['IC_NO']  = str(icno)
        icstr = 'ic = IC_{IC_NO}()'.format(**dict_of_vars)
        try:
            exec icstr
        except Exception,e :
            raise Exception('IC Number not found - '+str(e))
        f = open('../tests/tests.py')
        content = f.read()
        f.close()

        pos = content.find(dict_of_vars['IC_NO']+'()')
        offset = content[pos:].find('setIC')
        content = content[ pos : ( pos + offset) ]

        dic = ast.literal_eval(content[content.find('{'):content.find('}')+1])

        # ^ Gets the dictionary of inputs to IC from tests.py
        # v Tests if the obtained value is a dictionary

        if isinstance(dic,dict):
            print 'Test pin configuration found! Cool!', dic
        else:
            print 'Error: Test pin configuration not found'

        dict_of_vars['PIN_CONF'] = str(dic)

        print 'Dictinary of variables to replace in the template code',dict_of_vars

        code =  "from BinPy import *\n"
        code += "print 'Usage of IC {IC_NO}:\\n'\n".format(**dict_of_vars)
        code += "ic = IC_{IC_NO}()\n".format(**dict_of_vars)
        code += "print '\\nThe Pin configuration is:\\n'\n"
        code += "p = {PIN_CONF}\n".format(**dict_of_vars)
        code += "print p\n"
        code += "print '\\nPin initinalization\\n'\n"
        code += "ic.setIC(p)\n"
        code += "print '\\nPowering up the IC - using -- ic.setIC({14:1,7:0}) -- \\n'\n"
        code += "ic.setIC({14:1,7:0})\n"
        code += "print '\\nDraw the IC with the current configuration\\n'\n"
        code += "ic.drawIC()\n"
        code += "print '\\nRun the IC with the current configuration using -- print ic.run() -- \\n'\n"
        code += "print 'Note that the ic.run() returns a dict of pin configuration similar to :'\n"
        code += "print ic.run()\n"
        code += "print '\\nSeting the outputs to the current IC configuration using -- ic.setIC(ic.run()) --\\n'\n"
        code += "ic.setIC(ic.run())\n"
        code += "print '\\nDraw the final configuration\\n'\n"
        code += "ic.drawIC()"
        
        
        print 'The final code is \n\n:'+code
        
        print 'Executing it to see if this one runs smoothly'
        exec code        
        return code
            
    except Exception,e:
        print 'ERROR: '+str(e)
        return None

while(True):
    icno = raw_input('\n\n\nEnter icno to make an example code : (Enter N/n to quit) ')
    if icno.lower() == 'n' :
        sys.exit()
    code = getCode(icno)
    if code is None:
        print 'ERROR!!!'
    else:
        print '\n\nWriting to file ... '
        f = open("IC%s.py".format(icno),'w')
        f.write(code)
        f.close()
        print icno+' -- Done!!!' 
