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