import os
l = os.listdir('./Combinational')

for i in l:
    f = open('./Combinational/'+i, 'r')
    y=[]
    for j in f:
        x = j.split(" ")
        if x[0] == 'print':
            x[0] = 'print ('
            x[-1] = x[-1][:-1] + ')' +x[-1][-1]
        y.append(x)  
    ans='from __future__ import print_function\n'
    for x in y:
        for t in x:
            if ans[-1] == '\n':
                ans = ans + t
            else:    
                ans = ans+" "+t
#    print ans
 #   f.seek(0)
    f.close()

    f = open('./Combinational/'+i, 'w')
    f.write(ans)
    f.close()
