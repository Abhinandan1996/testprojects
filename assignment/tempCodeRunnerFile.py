rint("for first joint hinged and other end roller")

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