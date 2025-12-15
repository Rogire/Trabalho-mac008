import matplotlib.pyplot as plt
import numpy as np
def compara(x,y):
    return len(x) == len(y)


x = []
y = []
ac = 0

for i in range(4):
    x.append(0)
    y.append(ac)
    ac+=1000

#x1 = [0] * 4
#y1 = np.linspace(0, 4000, 4)
ac = 0
for i in range(48):
    x.append(ac)
    ac+=(6000/48)
    y.append(4000)

# Próximos 48 pontos
#x2 = np.linspace(0, 6000, 49)
#y2 = [4000] * 49

ac = 4000
for i in range(31):
    x.append(6000)
    y.append(ac)
    ac-=100

print("x:",len(x))
print("y:",len(y))
print(compara(x,y))

print(x)
print(y)

plt.plot(x, y, 'ro-')
plt.show()