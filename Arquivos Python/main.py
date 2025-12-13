import numpy as np

from feeldof1 import feeldof1
from feframe import feframe2
from feasmbl import feasmbl1
from feaplyc import feaplyc2

nel=6
nnel=2
ndof=3
nnode=(nnel-1)*nel+1
sdof=nnode*ndof

x = np.array([0, 0, 0, 0, 0, 10, 20], dtype=float)
y = np.array([0, 15, 30, 45, 60, 60, 60], dtype=float)

el=30*10**6
area=2
xi=2/3
rho=1

bcdof = [1,2,3]  
bcval = [0,0,0]    

ff = np.zeros(sdof)
kk = np.zeros((sdof, sdof))

ff[19] = -60 

for iel in range(1, nel+1):
    index = feeldof1(iel, nnel, ndof)
    node1 = iel - 1
    node2 = iel
    x1, y1 = x[node1], y[node1]
    x2, y2 = x[node2], y[node2]
    leng = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    if (x2-x1)==0:
        beta = np.pi/2 if y2 > y1 else -np.pi/2
    else:
        beta = np.arctan((y2 - y1) / (x2 - x1))
    k, _ = feframe2(el, xi, leng, area, rho, beta, 1)
    kk = feasmbl1(kk, k, index)

kk, ff = feaplyc2(kk, ff, bcdof, bcval)

fsol = np.linalg.solve(kk, ff)

store = np.column_stack((np.arange(1, sdof+1), fsol))
print("GDL    Deslocamento")
for linha in store:
    print(f"{int(linha[0]):3d}        {linha[1]:.6e}")