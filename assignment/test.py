import scipy.integrate as sp

print(sp.quad(lambda x: x,1,2)[0])
