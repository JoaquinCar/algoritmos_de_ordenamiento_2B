import time
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(A): #Función Insertión sort
 for j in range(1,len(A)): #Iteraciones
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:#Comparaciones
      A[i + 1] = A[i]
      i = i - 1
    A[i + 1] = key
    return A

def best_case(n):
    return list(range(n)) # En orden

def worst_case(n):
    return list(range(n, 0, -1)) #Lista alrevez a partir de n

def average_case(n):
    return np.random.permutation(n).tolist()#listas nandom


sizes = list(range(10, 1000, 10)) #Lista de 1000 nums salto de 10
best_times = []
worst_times = []
average_times = []

for n in sizes:
    # Mejor caso
    best_time = []
    for _ in range(100): #Num-Iteraciones de proceso para graficar
        best_input = best_case(n)
        start = time.time()
        insertion_sort(best_input)
        end = time.time()
        best_time.append(end - start)
    best_times.append(np.mean(best_time))

    # Peor caso
    worst_time = []
    for _ in range(100):#Num-Iteraciones de proceso para graficar
        worst_input = worst_case(n)
        start = time.time()
        insertion_sort(worst_input)
        end = time.time()
        worst_time.append(end - start)
    worst_times.append(np.mean(worst_time))

    # Caso promedio
    avg_time = []
    for _ in range(100):#Num-Iteraciones de proceso para graficar
        avg_input = average_case(n)
        start = time.time()
        insertion_sort(avg_input)
        end = time.time()

    avg_time.append(end - start)
    average_times.append(np.mean(avg_time))

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_times, label="Worst Case", color="red") #Peor caso-rojo
plt.plot(sizes, worst_times, label="Best Case", color="green") #Mejor caso- Verde
plt.plot(sizes, average_times, label="Average Case", color="blue") #Caso promedio - Azul
plt.xlabel("Tamaño del arreglo (n)")
plt.ylabel("Tiempo de ejecución (s)")
plt.legend()
plt.grid(True)
plt.show()
