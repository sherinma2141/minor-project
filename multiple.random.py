import igraph
from networkx import *
import sys
import random
import matplotlib.pyplot as plt

n=10 # 10 nodes
m=20 # 20 edges


G=gnm_random_graph(n,m)
plt.show(G)

print("node degree")
for v in nodes(G):
    print('%s %d ' % (v,degree(G,v)))
s=input("Enter the source")
d=input("enter the destination")
print ('Source is %s and Destination is %s' %(s,d))
print 'Degree of source'
print degree(G,s)
q=degree(G,s)
z=random.randint(1,q)
for n in nodes(G):
    print neighbors(G,n)
print ('the random number generated %s'%z)
##location=s
##while abs(location) != d:
##    step = random.randint(0, 1) # returns 0 or 1, each with prob. 1/2
##    if step == 0:
##        step = -1
##    location = location + step
##print location

step=0
t=s
for r in range(0,q):
    print('Random walk %s'%r)
    while (t != d):
        while step!= 15:
            current=random.choice(neighbors(G,t))
            print ('current Node Selected %s' %current)
            if current==d:
                t=current
                break
            else:
                t=current
            step=step+1
        break
    t=s
    step=0
        




    
