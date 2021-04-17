#for doing calculations we will use numpy and scipy
import numpy as np 
import scipy.integrate as sp 
from matplotlib import pyplot

n = int(input())

i = 0
nodes = []
while(i <= 1):
    nodes.append(i)
    i += 1 / n

h = 1/n

#-------------------------------------

index = 0

def n1(x):
    return (1-x)*(x + nodes[index] + nodes[index+1])/8/n

def n2(x):
    return (1+x)*(x + nodes[index] + nodes[index+1])/8/n


#-----------------------------

Fmatrix = np.zeros((n+1, 1))


Kmatrix = np.zeros((n+1,n+1))


index = 0

while(index < n):
    Fmatrix[index][0] +=sp.quad(n1,-1, 1)[0]
    Fmatrix[index+1][0] += sp.quad(n2,-1, 1)[0]
    index+=1

index = 0

while(index<=n):
    Kmatrix[index][index] = 2/h if(index != 0 and index != n) else 1/h
    if(index != 0):
        Kmatrix[index][index-1] = -1/h
    if(index != n):
        Kmatrix[index][index+1] = -1/h
    index+=1




print("for first joint hinged and other end roller")

K_, F_ = Kmatrix[1:,1:],Fmatrix[1:,0:]
K_ = np.linalg.inv(K_)
u = np.dot(K_, F_)
u = np.insert(u,0,[0],axis=0)
print(u)
x = nodes
y = u
pyplot.plot(x,y)
pyplot.show()

print("for both side hinged")

K2, F2 = Kmatrix[1:n,1:n], Fmatrix[1:n,0:]
K2 = np.linalg.inv(K2)
u2 = np.dot(K2, F2)
u2 = np.insert(u2,0,[0],axis=0)
u2 = np.append(u2,[0])
x = nodes
y = u2
print(u2)
pyplot.plot(x,y)
pyplot.show()