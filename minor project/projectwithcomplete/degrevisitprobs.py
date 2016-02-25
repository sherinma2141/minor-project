import random
import numpy as np
from networkx import *
import networkx as nx
from array import array
import matplotlib.pylab as plt
import itertools
n = array ('f')
p = array ('i')
q = array ('f')
z = array ('i')
a = array ('f')
k = array ('f')
s = array ('f')
d= {}
##g = nx.erdos_renyi_graph(10, 0.5)
##print g.degree() 
##g = nx.Graph()
##g.add_edges_from([(0,1),(1,2),(0,4),(1,3),(3,5),(4,6),(2,7),(5,7),(6,7)])
##r=(input("No.of Vertices:"))
r = 50

g=nx.complete_graph(r)
for i in range(r):
    z.append(i)

##no.of visits to each node is first assigned to 1

for i in range(r):
    q.append(1)
##print q

e=q

w=[i for i,x in enumerate(q) if x == 1]
##print w[0]


 #obtain the adj. matrix for the graph

print 'Adjacency Matrix of the graph'
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
            if s==w[j]:
##                upadating the visit of node 'j'
                e[j]=e[j]+1         
##                print e
##            t= (transition * degree * closeness centrality)/visit
            t=(T1[j,s]* l1[j])/e[j]
##            print t
            a.append(t)
       
##        print a,,, Taking the maximum so to decide the next node
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
    print ('Path length is:%s'%pathlength)
    print 'Path is',p
    break
