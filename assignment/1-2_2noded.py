#for doing calculations we will use numpy and scipy
import numpy as np 
import scipy.integrate as sp 
from matplotlib import pyplot
#input
n = int(input("elements: "))
l = float(input("length: "))
e = float(input("Young's modulus: "))
a = float(input("area: "))
c = float(input("force constant: "))

q = input("user generated nodes except start and end points(y/n): ")
nodes = []
i = 0
while(i <= l):
    nodes.append(i)
    i += l/(n)



if(q=="y" or q=="Y"):
    i = 1
    print("coordinate of node 1 is 0")
    while(i < n):
        nodes[i] = float(input(f"input coordinate of node {i+1}(total nodes={n+1}) :"))
        i+=1
    print(f"coordinate of node{n+1} is {l}")


##-------------------------------------

index = 0

def n1(x):
    return (1-x)/2*(((1-x)/2)*nodes[index] + ((1+x)/2)*nodes[index+1])*(-nodes[index]+nodes[index+1])/2

def n2(x):
    return (1+x)/2*(((1-x)/2)*nodes[index] + ((1+x)/2)*nodes[index+1])*(-nodes[index]+nodes[index+1])/2


#Initialize matrix
F = np.zeros((n+1, 1))
K = np.zeros((n+1,n+1))
index = 0
#force matrix assembly
while(index < n):
    F[index][0] +=(c*sp.quad(n1,-1, 1)[0])
    F[index+1][0] += (c*sp.quad(n2,-1, 1)[0])
    index+=1

#stiffness matrix assembly
index=0
while(index<n):
    temp = a * e / (nodes[index+1] - nodes[index])
    K[index][index] += temp
    K[index+1][index+1]+= temp
    K[index+1][index] -= temp
    K[index][index+1] -= temp
    index+=1

print("for first joint hinged and other end roller")
#calculating displacement
K_, F_ = K[1:,1:],F[1:,0:]
K_ = np.linalg.inv(K_)
u = np.dot(K_, F_)
u = np.insert(u,0,[0],axis=0)
fig, ax = pyplot.subplots(2)
x = nodes
y = u
#plotting
ax[0].plot(x,y,'b',label="one side roller other is hinged")
ax[0].legend()
ax[0].set_xlabel("distance form left")
ax[0].set_ylabel("deflection")
#you can print elements here for hinged roller---


#---------------------------------------------

print("for both side hinged")

K2, F2 = K[1:n,1:n], F[1:n,0:]
K2 = np.linalg.inv(K2)
u2 = np.dot(K2, F2)
u2 = np.insert(u2,0,[0],axis=0)
u2 = np.append(u2,[0])
x = nodes
y = u2
#you can print elements here for hinged hinged---


#---------------------------------------------
ax[1].plot(x,y,'r',label="both sides hinged")
ax[1].legend()
ax[1].set_xlabel("distance form left")
ax[1].set_ylabel("deflection")
pyplot.show()