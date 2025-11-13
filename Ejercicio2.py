"""
EJEMPLO: Estructuras de Decisión y Repetición
"""
# ESTRUCTURAS DE REPETICIÓN
print("=== ESTRUCTURAS DE REPETICIÓN ===")

# FOR - recorrer lista
nombres = ["Ana", "Luis", "Maria"]
print("\nFOR:")
for nombre in nombres:
    print(nombre)

# WHILE - con contador
print("\nWHILE:")
contador = 0
while contador < 3:
    print(f"  Iteración {contador + 1}")
    contador += 1

# DO-WHILE simulado
print("\nDO-WHILE:")
intento = 0
while True:
    intento += 1
    print(f"  Ejecución {intento}")
    if intento >= 2:  # Condición de salida
        break

# ESTRUCTURAS DE DECISIÓN
print("\n=== ESTRUCTURAS DE DECISIÓN ===")

nota = 85

# IF-ELIF-ELSE
print("\nIF-ELSE:")
if nota >= 90:
    categoria = "Excelente"
elif nota >= 80:
    categoria = "Bueno"
elif nota >= 70:
    categoria = "Regular"
else:
    categoria = "Insuficiente"
print(f"  Nota {nota}: {categoria}")

# MATCH-CASE (Switch)
print("\nMATCH-CASE:")
match nota:
    case n if n >= 90: resultado = "A"
    case n if n >= 80: resultado = "B" 
    case n if n >= 70: resultado = "C"
    case _: resultado = "F"
print(f"  Calificación: {resultado}")

# OPERADOR TERNARIO
print("\nOPERADOR TERNARIO:")
estado = "Aprobado" if nota >= 70 else "Reprobado"
print(f"  Estado: {estado}")

print("\n¡Programa completado!")