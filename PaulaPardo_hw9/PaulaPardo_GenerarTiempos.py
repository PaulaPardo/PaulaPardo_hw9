import numpy as np
import time

# Esta funcion recursiva retorna el N-esimo  numero  de  la  secuencia  de  Fibbonacci
def fibonacci(N):
    if(N == 0 or N == 1):
        return N
    else:
        return fibonacci(N-1) + fibonacci(N-2)
# Esta funcion retorna el tiempo (en segundos) que se tarda en obtener el N-esimo numero de la secuencia de Fibbonacci 
def get_time(N):
    t0 = time.time()
    a = fibonacci(N)
    t1 = time.time()-t0
    return t1

# Imprime el tiempo (en segundos) que se tarda en obtener el N-esimo numero de la secuencia de Fibbonacci para los primeros 35 valores de N
for i in range(35):
    print i, get_time(i)
