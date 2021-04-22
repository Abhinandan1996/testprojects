import numpy as np
from matplotlib import pyplot
from math import sqrt

# element matrix
Ke= [[ 1.75      , 1.01036297     , -2.        , -1.15470054 , 0.25       , 0.14433757],
    [ 1.01036297 , 0.58333333     , -1.15470054, -0.66666667 , 0.14433757 , 0.08333333],
    [-2.         ,-1.15470054     ,  4.        ,  2.30940108 ,-2.         ,-1.15470054],
    [-1.15470054 ,-0.66666667     ,  2.30940108,  1.33333333 ,-1.15470054 ,-0.66666667],
    [ 0.25       , 0.14433757     , -2.        , -1.15470054 , 1.75       , 1.01036297],
    [ 0.14433757 , 0.08333333     , -1.15470054, -0.66666667 , 1.01036297 , 0.58333333]]

n = int(input("elements: "))
l = float(input("length: "))
e = float(input("Young's modulus: "))
a = float(input("area: "))
c = float(input("force constant: "))

q = input("user generated nodes except start and end points(y/n): ")
nodes = []
i = 0
while(i < l+.000001): #.000001 for floating point error
    nodes.append(i)
    i += l/(n)
#creating user input nodes
if(q=="y" or q=="Y"):
    i = 1
    print("coordinate of node 1 is 0")
    while(i < n):
        nodes[i] = float(input(f"input coordinate of node {i+1}(total nodes={n+1}) :"))
        i+=1
    print(f"coordinate of node{n+1} is {l}")


for i in range(6):
    for j in range(6):
        Ke[i][j] *= (a * e / l)

#initializing global matrices
K = np.zeros((4*n + 2, 4*n + 2))
F = np.zeros((4*n + 2, 1))

#assembling matrices
for i in range(n):
    t = i * 4
    for i1 in range(6):
        for i2 in range(6):
            K[t + i1][t + i2] += Ke[i1][i2]
    xe = (nodes[i]+nodes[i+1])/2
    h  = nodes[i+1] - nodes[i]
    F[t]     +=sqrt(3)/2 * c * h / 8 * (4*xe/3 - 2/3*h)
    F[t + 1] +=.5        * c * h / 8 * (4*xe/3 - 2/3*h)
    F[t + 2] +=sqrt(3)/2 * c * h / 8 * (16/3 * xe)
    F[t + 3] +=.5        * c * h / 8 * (16/3 * xe)
    F[t + 4] +=sqrt(3)/2 * c * h / 8 * (4*xe/3 + 2/3*h)
    F[t + 5] +=.5        * c * h / 8 * (4*xe/3 + 2/3*h)


#finding unknowns
K_ = K[2:len(K)-1, 2:len(K)-1]
F_ = F[2:len(K)-1,0:]
K2 = np.linalg.inv(K_)
u = np.matmul(K2, F_)
u = np.insert(u,0,[0])
u = np.insert(u,0,[0])
u = np.append(u,[0])

newnodes = []
for i in range(len(nodes)-1):
    newnodes.append(nodes[i])
    newnodes.append((nodes[i]+nodes[i+1])/2)
newnodes.append(nodes[-1])
xdef=u[0::2]
ydef=u[1::2]
tdef = [sqrt(i**2 + j**2) for i,j in zip(xdef,ydef)]
fig, axs = pyplot.subplots(3)
axs[0].plot(newnodes,xdef, label="x-def")
axs[1].plot(newnodes,ydef, label="y-def")
axs[2].plot(newnodes,tdef, label="total-def")

axs[0].set_ylabel("Deflection in x-axis")
axs[1].set_ylabel("Deflection in y-axis")
axs[2].set_ylabel("total Deflection")

axs[0].set_xlabel("Distance")
axs[1].set_xlabel("Distance")
axs[2].set_xlabel("Distance")
pyplot.show()