import random
import numpy as np
from networkx import *
import networkx as nx
from array import array
import matplotlib.pylab as plt
import itertools
n = array ('f')
p = array ('i')
a = array ('f')
s = array ('f')
z = array ('i')
d= {}
##g = nx.erdos_renyi_graph(10, 0.5)
##print g.degree() 
##g = nx.Graph()
##g.add_edges_from([(0,1),(1,2),(0,4),(1,3),(3,5),(4,6),(2,7),(5,7),(6,7)])
 #obtain the adj. matrix for the graph
r = 50

g=nx.complete_graph(r)
for i in range(r):
     z.append(i)
print 'Adjacency Matrix of the Graph'
T= nx.attr_matrix(g,rc_order=z)
##print T

for i in range(r):
     q=np.sum(T[i])
     d.setdefault(i,[]).append(q)
values = d.values()
l= list(d.values())
##print l
l1 = list(itertools.chain(*l))
##print l1
##for i in range(5):
##     print g.degree(i)
#Transition Probality Matrix T
for i in range(r):
     if(np.sum(T[i])>0):
         T[i] = T[i]/np.sum(T[i])
T1=T.transpose()
print 'Transition Probability Matrix'
##print T1
##for i in range(5):
##    for j in range(5):
##        print T[i,j]

s=input("Enter the source")
d=input("enter the destination")
print ('Source is %s and Destination is %s' %(s,d))
p.append(s)
pathlength=1
step=0
while (s != d):
    while step!= 100:
        for j in range(r):
             t=T1[j,s]* l1[j]
##             print t
             a.append(t)
       
##        print a
        t=max(a)
        indices = [i for i, j in enumerate(a) if j == t]
##        print indices
##        k=a.index(max(a))
        current=random.choice(indices)
        p.append(current)
            
##        print ('current Node Selected %s' %current)
        if current==d:
            s=current
            break
        else:
            s=current
        step=step+1
        t=[]
        a=[]
        pathlength=pathlength+1
   
    if s!=d:
         print 'No path since Maximum path length reached '
    else:
     print 'Path is',p
     print ('Path length is:%s'%pathlength)
    break
