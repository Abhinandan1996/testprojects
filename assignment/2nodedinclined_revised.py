import numpy as np
from matplotlib import pyplot
from math import sqrt

# element matrix
Ke=[[ 0.75      ,  0.4330127, -0.75     , -0.4330127],
    [ 0.4330127 ,  0.25     , -0.4330127, -0.25     ],
    [-0.75      , -0.4330127,  0.75     ,  0.4330127],
    [-0.4330127 , -0.25     ,  0.4330127,  0.25     ]]

n = int(input("elements: "))
l = float(input("length: "))
e = float(input("Young's modulus: "))
a = float(input("area: "))
c = float(input("force constant: "))

q = input("user generated nodes except start and end points(y/n): ")
nodes = []
i = 0
while(i < l+.000001):
    nodes.append(i)
    i += l/(n)

if(q=="y" or q=="Y"):
    i = 1
    print("coordinate of node 1 is 0")
    while(i < n):
        nodes[i] = float(input(f"input coordinate of node {i+1}(total nodes={n+1}) :"))
        i+=1
    print(f"coordinate of node{n+1} is {l}")


for i in range(4):
    for j in range(4):
        Ke[i][j] *= (a * e / l)

#initializing global matrices
K = np.zeros((2*n + 2, 2*n + 2))
F = np.zeros((2*n + 2, 1))
#assembling matrices
for i in range(n):
    t = i * 2
    for i1 in range(4):
        for i2 in range(4):
            K[t + i1][t + i2] += Ke[i1][i2]
    xe = (nodes[i] + nodes[i+1])/2
    h  = nodes[i+1] - nodes[i]
    F[t]    +=sqrt(3)/2 * c * h / 2 * (-h/6 + xe)
    F[t + 1]+=.5        * c * h / 2 * (-h/6 + xe)
    F[t + 2]+=sqrt(3)/2 * c * h / 2 * ( h/6 + xe)
    F[t + 3]+=.5        * c * h / 2 * ( h/6 + xe)
print(K)
#calculation of deflection
K_ = K[2:len(K)-1, 2:len(K)-1]
F_ = F[2:len(K)-1,0:]
K2 = np.linalg.inv(K_)
u = np.matmul(K2, F_)
u = np.insert(u,0,[0])
u = np.insert(u,0,[0])
u = np.append(u,[0])

#separating x and y deflections
xdef=u[0::2]
ydef=u[1::2]

tdef = [sqrt(i**2 + j**2) for i,j in zip(xdef,ydef)]
fig, axs = pyplot.subplots(3)
axs[0].plot(nodes,xdef, label="x-def")
axs[1].plot(nodes,ydef, label="y-def")
axs[2].plot(nodes,tdef, label="total-def")
axs[0].set_ylabel("Deflection in x-axis")
axs[1].set_ylabel("Deflection in y-axis")
axs[2].set_ylabel("total Deflection")

axs[0].set_xlabel("Distance")
axs[1].set_xlabel("Distance")
axs[2].set_xlabel("Distance")

pyplot.legend()
pyplot.show()