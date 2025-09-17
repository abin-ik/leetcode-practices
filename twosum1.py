import numpy as np
l=np.array(list(map(int,input("enter the numbers").split())))
a=int(input("target"))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==9:
            print([i,j])
            