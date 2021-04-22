import numpy as np 
import scipy.integrate as sp 
from matplotlib import pyplot
from math import sqrt

print(sqrt(5))
n = int(input("elements: "))
l = float(input("length: "))
e = float(input("Young's modulus: "))
a = float(input("area: "))
c = float(input("force constant: "))

q = input("user generated nodes except start and end points(y/n): ")
nodes = []
i = 0
while(i < l + 1/n):  #(1/n is added due to the errors caused by floats in long calculations)
    nodes.append(i)
    i += l/(n) 



if(q=="y" or q=="Y"):
    i = 1
    print("coordinate of node 1: 0")
    while(i < n):
        nodes[i] = float(input(f"input coordinate of node {i+1}(total nodes={n+1}): "))
        i+=1
    
    print(f"coordinate of node{n+1}: {l}")
    
#members of stiffness element matrix
_00 = .75; _01 = sqrt(3)/4; _02 = -.75; _03= -_01; _11 = .25; _12=-_01;_13 = -.25; _22 = _00; _23=_01;_33=.25

F = np.zeros(((n+1)*2,1))
K = np.zeros(((n+1)*2,(n+1)*2))

mn = 1000000* a * e

##-------------------------------------

index = 0


for i in range(n):
    t = 2*i
    h = nodes[i+1] - nodes[i]
    temp = a * e / h

    K[t][t]   += temp * _00 ; K[t][t+1]   += temp * _01 ; K[t][t+2]   += temp * _02 ; K[t][t+3]   += temp * _03
    K[t+1][t] += temp * _01 ; K[t+1][t+1] += temp * _11 ; K[t+1][t+2] += temp * _12 ; K[t+1][t+3] += temp * _13
    K[t+2][t] += temp * _02 ; K[t+2][t+1] += temp * _12 ; K[t+2][t+2] += temp * _22 ; K[t+2][t+3] += temp * _23
    K[t+3][t] += temp * _03 ; K[t+3][t+1] += temp * _13 ; K[t+3][t+2] += temp * _23 ; K[t+3][t+3] += temp * _33
    h = nodes[i+1] - nodes[i]
    F[t][0]   += c * h / 2 * sqrt(3)/2  * (-h/6 + (nodes[i+1] + nodes[i])/2)
    F[t+1][0] += c * h / 2 * 1/2        * (-h/6 + (nodes[i+1] + nodes[i])/2)
    F[t+2][0] += c * h / 2 * sqrt(3)/2  * ( h/6 + (nodes[i+1] + nodes[i])/2)
    F[t+3][0] += c * h / 2 * 1/2        * ( h/6 + (nodes[i+1] + nodes[i])/2)

x,y = 0,0

#deflection calculation
t = len(F)
F_= F.copy()
K_= K.copy()


#implementing penalty approach
for i in [0,1,len(K)-1]:
        K_[i][i] += mn
 #to catch bugs
K_2 = np.linalg.inv(K_)

u = np.matmul(K_2,F_)
np.set_printoptions(precision=2)
print(K)

xdef =[]
for i in range(0,2*(n+1),2):
    xdef.append(u[i])
fig, axs = pyplot.subplots(2)
axs[0].plot(nodes,xdef,'b', label="deflection in x direction")
axs[0].set_xlabel("distance form left")
axs[0].set_ylabel("deflection")
ydef = []
for i in range(1,2*(n+1),2):
    ydef.append(u[i])
axs[0].plot(nodes,ydef,'g', label="deflection in x direction")
axs[0].set_xlabel("distance form left")
axs[0].set_ylabel("deflection")
pyplot.show()
tdef = []

for i in range(len(xdef)):
    tdef.append(sqrt(xdef[i]**2 + ydef[i]**2))
axs[0].plot(nodes,tdef,'r', label="deflection")
axs[0].set_xlabel("distance form left")
axs[0].set_ylabel("deflection")
pyplot.show()