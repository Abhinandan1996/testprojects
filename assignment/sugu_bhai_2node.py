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

he = []
for pts in coor:
    he.append(pts[1] - pts[0])
print(he)

K = np.zeros((n+1, n+1))
F = np.zeros((n+1, 1))

for i in range(n):
    temp = a * e / he[i]
    K[i][i] += temp
    K[i][i+1] += -temp
    K[i+1][i] += -temp
    K[i+1][i+1] += temp


print(K)

for i in range(n):
    