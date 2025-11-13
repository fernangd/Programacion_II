
# 1. CREACIÓN DE LISTAS
print("=== CREACIÓN DE LISTAS ===")

# Lista de números
numeros = [20,10,50,30,40]
print(f"Lista de números: {numeros}")

# Lista de textos
frutas = ["manzana", "banana", "naranja", "uva"]
print(f"Lista de frutas: {frutas}")

# Lista mixta
mixta = [1, "hola", 3.14, True]
print(f"Lista mixta: {mixta}")

# 2. ACCESO A ELEMENTOS
print("\n=== ACCESO A ELEMENTOS ===")
print(f"Primer elemento: {frutas[0]}")
print(f"Último elemento: {frutas[3]}")
print(f"Último elemento: {frutas[-1]}")
print(f"Elementos del 1 al 3: {frutas[1:4]}")

# 3. MODIFICACIÓN DE LISTAS
print("\n=== MODIFICACIÓN ===")
frutas[1] = "pera"
print(f"Después de modificar: {frutas}")

# 4. MÉTODOS PARA AGREGAR ELEMENTOS
print("\n=== AGREGAR ELEMENTOS ===")
frutas.append("mango")
print(f"Después de append: {frutas}")

frutas.insert(2, "sandía")
print(f"Después de insert: {frutas}")

# 5. ELIMINAR ELEMENTOS
print("\n=== ELIMINAR ELEMENTOS ===")
frutas.remove("uva")
print(f"Después de remove: {frutas}")

eliminado = frutas.pop(0)
print(f"Elemento eliminado: {eliminado}")
print(f"Después de pop: {frutas}")

# 6. OPERACIONES CON LISTAS
print("\n=== OPERACIONES ===")
print(f"Longitud de la lista: {len(frutas)}")
print(f"¿Existe 'naranja'? {'naranja' in frutas}")
print(f"Posición de 'sandía': {frutas.index('sandía')}")

# 7. ORDENAMIENTO
print("\n=== ORDENAMIENTO ===")
numeros.sort()
print(f"Lista ordenada: {numeros}")

numeros.reverse()
print(f"Lista invertida: {numeros}")

# 8. RECORRIDO CON BUCLES
print("\n=== RECORRIDO CON FOR ===")
print("Frutas disponibles:")
for fruta in frutas:
    print(fruta)

# 9. OPERACIONES MATEMÁTICAS
print("\n=== OPERACIONES MATEMÁTICAS ===")
suma = sum(numeros)
promedio = suma / len(numeros)
print(f"Suma: {suma}, Promedio: {promedio:.2f}")



import numpy as np

#print("¡NumPy funciona correctamente!")
#print(f"Versión de NumPy: {np.__version__}")

#pip install numpy

# Con listas normales
numeros_lista = [20, 10, 50, 30, 40]
suma = sum(numeros_lista)  # Se necesita función sum()
print("Suma con listas: ", suma)
print()

# Con NumPy
numeros_array = np.array([20, 10, 50, 30, 40])
print(f"Arreglo usando NumPy: {numeros_array}")
suma = numeros_array.sum()  # Método del array
print("Suma con NumPy: ", suma)
# o también:
suma = np.sum(numeros_array)

# Operaciones vectorizadas (muy eficientes)
doble = numeros_array * 2  # Multiplica todos por 2
cuadrados = numeros_array ** 2  # Eleva todos al cuadrado

print(f"Arreglo*2: {doble}")
print(f"Arreglo^2: {cuadrados}")




