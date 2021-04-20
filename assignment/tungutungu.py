import matplotlib.pyplot as plt
import numpy as np

n = int(input("elements: "))
l = 1
e = 1
a = 1
c = 1

nodes = []
i = 0
while(i <= l):
    nodes.append(i)
    i = i + l/(n)

q = input("user generated nodes except start and end points(y/n): ")
if(q=="y" or q=="Y"):
    i = 1
    while(i < n):
        nodes[i] = float(input(f"input node number {i+1}(total nodes={n+1}) :"))
        i = i + 1
print(nodes)

coor = []
for i in range(n):
    coor.append([nodes[i],nodes[i+1]])

print(coor)

K = np.zeros((2*n+1,2*n+1))
F = np.zeros((2*n+1,1))

for i in range(n):
    he = nodes[i+1] - nodes[i]
    t = 2*i
    t2 = a * e / he
    K[t][t]        += c * 2.333333333
    K[t][t+1]      += - c * 2.6666666666
    K[t][t+2]      += c * .333333333333
    K[t+1][t]      += K[t][t+1]
    K[t+1][t+1]    += c * 5.3333333333333
    K[t+1][t+2]    += - c * 2.6666666666
    K[t+2][t]      += K[t][t+2]
    K[t+2][t+1]    += K[t+1][t+2]
    K[t+2][t+2]    += c * 2.333333333333
    #F
    xe = (nodes[i+1] + nodes[i])/2
    F[t]   += c * he / 8 *(1.33333333 * xe - .6666666666*he)
    F[t+1] += c * he / 8 *(5.33333333 * xe)
    F[t+2] += c * he / 8 *(1.33333333 * xe + .6666666666*he)


all_nodes = []
for i in range(n):
    all_nodes.append(nodes[i])
    all_nodes.append((nodes[i]+nodes[i+1])/2)
all_nodes.append(nodes[-1])


tempF = F.copy()
tempK = K.copy()
# hinged roller, def node 1= 0
tempF=np.delete(tempF, 0, axis = 0)

tempK=np.delete(tempK, 0, axis = 0)
tempK=np.delete(tempK, 0, axis = 1)
Kinv = np.linalg.inv(tempK)
u = np.dot(Kinv, tempF)

u = np.insert(u,0,[0],axis=0)
y = u
x = all_nodes

plt.plot(x,y)

#hinged hinged node 1 = node n + 1 = 0
tempF = F.copy()
tempK = K.copy()


tempF=np.delete(tempF, 2*n, axis = 0)
tempF=np.delete(tempF, 0, axis = 0)
tempK=np.delete(tempK, 2*n, axis = 0)
tempK=np.delete(tempK, 2*n, axis = 1)
tempK=np.delete(tempK, 0, axis = 0)
tempK=np.delete(tempK, 0, axis = 1)

Kinv = np.linalg.inv(tempK)
u = np.dot(Kinv, tempF)

u = np.insert(u,0,[0],axis=0)
u = np.append(u,[0])

y = u
x = all_nodes
plt.plot(x,y)
print(F, sum(F))
plt.show()
