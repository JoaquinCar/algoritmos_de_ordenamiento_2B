def quicksort(arr):
    if not arr: #caso base 
        return [] #arr vacio
    else:
        pivot = arr[0] ##agarramos como pivot el primer elemento
        iguales = [x for x in arr if x == pivot] #selecciona todos los elementos de la lista que sean iguales al pivot
        menores = quicksort([x for x in arr if x < pivot]) #selecciona todos los elementos de la lista que sean menores al pivot
        mayores = quicksort([x for x in arr if x > pivot]) #selecciona todos los elementos de la lista que sean mayores al pivot

    return menores + iguales + mayores #se juntan en orden ascendente 
#arr =[7,5,4,3,2,43,5,6,64]
#arr=[67,43,32,87,43,9,81,13,456]
arr=[46,4,3,23,66,43,22,67,12,53,78]
print(quicksort(arr))


