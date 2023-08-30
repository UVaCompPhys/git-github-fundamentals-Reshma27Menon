#To calculate volume of an n-dimensional sphere:

import matplotlib.pyplot as plt
import numpy as np
import math


for r in np.arange(1,2.05,0.05):
    for n in range(0,51):
        p=(math.pi)**(n/2) 
        R=r**n
        g=math.gamma((n/2)+1)
        v=(p*R)/(g)
        print (v)
        plt.plot(n,v, "bo")
        
plt.title("Volume of an n-sphere for combinations of n and radius(R)")
plt.xlabel("(n, R)")
plt.ylabel("V(n,R)")
plt.savefig('hw1.png')
plt.show()        
