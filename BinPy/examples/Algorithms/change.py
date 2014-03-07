import os
l = os.listdir('.')

for i in l:
    f = open(i, 'r')
    y=[]
    for j in f:
        x = j.split(" ")
        if x[0] == 'print':
            x[0] = 'print ('
            x[-1] = ')'+x[-1]
        y.append(x)
    print y    
    f.close()
