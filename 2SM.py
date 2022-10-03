


# 2:simulate the tossing of two fair coins a million times
# and count the no.of times you get double Head and hence
# compute probability of appearance of double Heads is (1/4).


import numpy as np
from numpy.random import randint
import random

f= lambda n: [sum(randint(2,size=n)) for i in range(trial)]
n,trial=2,100
N=[]

for i in range(10):
    x,y=np.unique(f(n),return_counts=True)
    p=np.max(y)/float(trial)
    N.append(n)
    


print (p)


