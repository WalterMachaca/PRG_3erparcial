# Lista que almacena 10 números enteros introducidos por el usuario
numeros = []  # Lista vacía para almacenar los números

# Bucle para solicitar 10 números enteros al usuario
for i in range(10):  # Repetir 10 veces para obtener 10 números
    while True:  # bucle de validación: se repite hasta que el usuario introduce un entero válido
        entrada = input(f"Introduce el número {i+1} entero: ") # Se pide al usuario un número
        try:
            n = int(entrada)  
            numeros.append(n)  # se añade el entero a la lista 'numeros'
            break  # salir del bucle de validación
        except ValueError:
            print("Entrada no válida. Por favor introduce un número entero.")  # mensaje de error si no es entero

# Cálculo del número mayor y menor de la lista
mayor = max(numeros)  
menor = min(numeros)  

# Cálculo de la suma y el promedio
suma = 0  # Se inicializa la suma en 0
for num in numeros:  
    suma += num  
promedio = suma / len(numeros)  # Promedio igual a la suma dividido por la cantidad de números

# Función para ordenar la lista de números de menor a mayor
def ordenar(lista):  
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):  
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

# Lista ordenada usando la función definida arriba
lista_ordenada = ordenar(numeros)  

# Resultados 
print("RESULTADOS: ")
print("Número mayor: ", mayor)  # Número mayor encontrado en la lista
print("Número menor: ", menor)  # Número menor encontrado en la lista
print("Suma de los números: ", suma)  # Suma de los números introducidos
print("Promedio de los números: ", promedio)  # Promedio de los números introducidos
print("Lista ordenada (de menor a mayor):", lista_ordenada)  # Lista ordenada de menor a mayor
