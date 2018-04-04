import numpy as np
import matplotlib.pyplot as plt

# Se cargan los archivos
archivo1 = np.genfromtxt("times_python.csv")
archivo2 = np.genfromtxt("times_cpp.csv")

# Se grafican los datos de tiempo Vs N
N = archivo1[:;0]
timespy = archivo1[:;1]
timescpp = archivo2[:;1]

plt.plot(N,timespy,label = 'Tiempos python')
plt.plot(N,timescpp,label = 'Tiempos cpp')
plt.xlabel('N')
plt.ylabel('t')
plt.title('cpp vs python tiempos')
plt.legend()
plt.savefig('cpp_vs_python.png')
