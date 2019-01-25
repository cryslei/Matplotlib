import matplotlib.pyplot as plt
import numpy as np

#plt.plot([6,7,8,9,10],[1,2,3,3,5])
def ler_base_dados(arquivo):
    x = []
    y = []

    dataset = open(arquivo,'r')
    for line in dataset:
        line = line.strip() #23,54\n -> 23,54
        X,Y = line.split(',')
        x.append(int(X))
        y.append(int(Y))

    dataset.close()
    return x,y


x,y = ler_base_dados('teste.txt')
x2,y2 = ler_base_dados('teste2.txt')

plt.plot(sorted(x),sorted(y),'b',linestyle='--')
plt.plot(sorted(x2),sorted(y2),'r',linestyle='--')

plt.title('exemplo')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()
