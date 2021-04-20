import numpy as np 
import scipy.integrate as sp 
from matplotlib import pyplot


n = int(input("elements: "))
l = float(input("length: "))
e = float(input("Young's modulus: "))
a = float(input("area: "))
c = float(input("constant: "))

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

#Creating K-matrix
K = np.zeros((2*n+1, 2*n+1))
F = np.zeros((2*n+1,1))
index = 0


for i in range(0,2*n-1,2):
    #Stiffness matrix elements
    K[i][i]     += a * e / (nodes[index+1] - nodes[index]) * 7 / 3
    K[i][i+1]   += a * e / (nodes[index+1] - nodes[index]) * (-8/3) 
    K[i][i+2]   += a * e / (nodes[index+1] - nodes[index]) * (1/3)
    K[i+1][i]   += K[i][i+1]
    K[i+1][i+1] += a * e / (nodes[index+1] - nodes[index]) * 16/3
    K[i+1][i+2] += a * e / (nodes[index+1] - nodes[index]) * (-8/3) 
    K[i+2][i]   += K[i][i+2] 
    K[i+2][i+1] += K[i+1][i+2]
    K[i+2][i+2] += a * e / (nodes[index+1] - nodes[index]) * 7 / 3

    #Force matrix elements
    F[i][0]   += c * (nodes[index+1] - nodes[index])/8*(4/3 *  (nodes[index+1]+ nodes[index])/2 - 2/3 * (nodes[index+1] - nodes[index]))
    F[i+1][0] += c * (nodes[index+1] - nodes[index])/8*(16/3 * (nodes[index+1]+ nodes[index])/2)
    F[i+2][0] += c * (nodes[index+1] - nodes[index])/8*(4/3 *  (nodes[index+1]+ nodes[index])/2 + 2/3 * (nodes[index+1] - nodes[index]))
    index+=1
nodestemp = nodes.copy()
nodes = []
for i in range(nodestemp.__len__()-1):
    nodes.append(nodestemp[i])
    nodes.append((nodestemp[i]+nodestemp[i+1])/2)
nodes.append(nodestemp[nodestemp.__len__()-1])

print(K)

print("for first joint hinged and other end roller")

K_, F_ = K[1:,1:],F[1:,0:]
K_ = np.linalg.inv(K_)
u = np.dot(K_, F_)
u = np.insert(u,0,[0],axis=0)

x = nodes
y = u
print(u)
pyplot.plot(x,y,'b',label="one side roller other is hinged")

print("for both side hinged")

K2, F2 = K[1:2*n,1:2*n], F[1:2*n,0:]
K2 = np.linalg.inv(K2)
u2 = np.dot(K2, F2)
u2 = np.insert(u2,0,[0],axis=0)
u2 = np.append(u2,[0])
x = nodes
y = u2

pyplot.plot(x,y,'r',label="both sides hinged")
pyplot.legend()
pyplot.xlabel("distance form left")
pyplot.ylabel("deflection")
pyplot.show()

