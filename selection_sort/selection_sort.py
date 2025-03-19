import time
import matplotlib.pyplot as plt
import numpy as np

def ord_seleccion(arreglo):
    for i in range(len(arreglo) - 1):  # Bucle principal
        menor = i  # Índice del menor valor encontrado
        for j in range(i + 1, len(arreglo)):  # Bucle secundario
            if arreglo[j] < arreglo[menor]:
                menor = j
        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

def measure_time(arr):
    start_time = time.time()
    ord_seleccion(arr)
    return time.time() - start_time

sizes = np.arange(1000, 11000, 1000)  # Incluye 10,000 como entrada máxima
worst_times = []
average_times = []
best_times = []

for size in sizes:
    worst_case = list(range(size, 0, -1))  # Peor caso (ordenado en reversa)
    average_case = np.random.randint(0, size, size).tolist()  # Caso promedio (aleatorio)
    best_case = list(range(size))  # Mejor caso (ya ordenado)
    
    worst_times.append(measure_time(worst_case))
    average_times.append(measure_time(average_case))
    best_times.append(measure_time(best_case))

plt.figure(figsize=(10, 5))
plt.plot(sizes, worst_times, label="Peor caso", marker='o', linestyle='dashed', color='r')
plt.plot(sizes, average_times, label="Caso promedio", marker='s', linestyle='dashed', color='g')
plt.plot(sizes, best_times, label="Mejor caso", marker='^', linestyle='dashed', color='b')
plt.xlabel("Tamaño del array")
plt.ylabel("Tiempo (segundos)")
plt.title("Complejidad Temporal del Ordenamiento por Selección")
plt.legend()
plt.grid()
plt.show()
