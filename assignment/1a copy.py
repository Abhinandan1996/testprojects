#for doing calculations we will use numpy and scipy
import numpy as np 
import scipy.integrate as sp 
from matplotlib import pyplot

n = int(input("elements: "))
l = int(input("length: "))
e = int(input("Young's modulus: "))
a = int(input("area: "))

q = input("user generated nodes except start and end points(y/n): ")
nodes = []
i = 0
while(i <= l):
    nodes.append(i)
    i += l/(n)



if(q=="y" or q=="Y"):
    i = 1
    while(i < n):
        nodes[i] = float(input(f"input node number {i+1}(total nodes={n+1}) :"))
        i+=1


##-------------------------------------

index = 0

def n1(x):
    return (1-x)/2*(((1-x)/2)*nodes[index] + ((1+x)/2)*nodes[index+1])*(-nodes[index]+nodes[index+1])/2

def n2(x):
    return (1+x)/2*(((1-x)/2)*nodes[index] + ((1+x)/2)*nodes[index+1])*(-nodes[index]+nodes[index+1])/2


#-----------------------------

Fmatrix = np.zeros((n+1, 1))


Kmatrix = np.zeros((n+1,n+1))


index = 0

while(index < n):
    Fmatrix[index][0] +=sp.quad(n1,-1, 1)[0]
    Fmatrix[index+1][0] += sp.quad(n2,-1, 1)[0]
    index+=1

index=0
while(index<n):
    temp = a * e / (nodes[index+1] - nodes[index])
    Kmatrix[index][index] += temp
    Kmatrix[index+1][index+1]+= temp
    Kmatrix[index+1][index] -= temp
    Kmatrix[index][index+1] -= temp
    index+=1


print(Fmatrix)
print(Kmatrix)


print("for first joint hinged and other end roller")

K_, F_ = Kmatrix[1:,1:],Fmatrix[1:,0:]
K_ = np.linalg.inv(K_)
u = np.dot(K_, F_)
u = np.insert(u,0,[0],axis=0)
print(u)
x = nodes
y = u
pyplot.plot(x,y)


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