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
d= {}
##g = nx.erdos_renyi_graph(10, 0.5)
##print g.degree() 
g = nx.Graph()
g.add_edges_from([(0,1),(1,2),(0,4),(1,3),(3,5),(4,6),(2,7),(5,7),(6,7)])
 #obtain the adj. matrix for the graph

print 'Adjacency Matrix of the Graph'
T= nx.attr_matrix(g,rc_order=[0,1,2,3,4,5,6,7])
print T

for i in range(8):
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
for i in range(8):
     if(np.sum(T[i])>0):
         T[i] = T[i]/np.sum(T[i])
T1=T.transpose()
print 'Transition Probability Matrix'
print T1
##for i in range(5):
##    for j in range(5):
##        print T[i,j]

s=input("Enter the source")
d=input("enter the destination")
print ('Source is %s and Destination is %s' %(s,d))
p.append(s)
pathlength=1

while (s != d):
     for j in range(8):
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
     
     t=[]
     a=[]
     pathlength=pathlength+1


print 'Path is',p
print ('Path length is:%s'%pathlength)

