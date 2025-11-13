"""
EJEMPLO PYTHON: Calculadora de Geometría
Incluye: tipos de datos, math, instrucciones secuenciales
"""
import math

"""
# TIPOS DE DATOS
nombre = "Edilson"               # str
edad = 25                        # int
altura = 1.65                    # float
es_estudiante = True             # bool
materias = ["Matemáticas", "Física"]  # list
"""

# EL USUARIO INGRESA SUS DATOS
print("=== INGRESE SUS DATOS ===")
nombre = input("Ingrese su nombre: ")               # str
edad = int(input("Ingrese su edad: "))              # int
altura = float(input("Ingrese su altura (metros): ")) # float
materias = input("Ingrese sus materias (separadas por coma): ").split(", ")  # list

# INSTRUCCIONES SECUENCIALES
print("\n=== CALCULADORA GEOMÉTRICA ===")
print(f"Usuario: {nombre}, Edad: {edad}")

# EL USUARIO INGRESA DATOS PARA CÁLCULOS
print("\n=== INGRESE DATOS PARA CÁLCULOS ===")
radio = float(input("Ingrese el radio del círculo: "))
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))

# LIBRERÍA MATEMÁTICA + CÁLCULOS
area_circulo = math.pi * math.pow(radio, 2)
circunferencia = 2 * math.pi * radio

area_cuadrado = math.pow(lado_cuadrado, 2)
diagonal = lado_cuadrado * math.sqrt(2)

# MOSTRAR RESULTADOS
print(f"\nCÍRCULO (radio: {radio}):")
print(f"Área: {area_circulo:.2f}")
print(f"Circunferencia: {circunferencia:.2f}")

print(f"\nCUADRADO (lado: {lado_cuadrado}):")
print(f"Área: {area_cuadrado}")
print(f"Diagonal: {diagonal:.2f}")

# EJEMPLO CON MÚLTIPLES OPERACIONES
print(f"\nOPERACIONES MATEMÁTICAS:")
print(f"Raíz de {lado_cuadrado}: {math.sqrt(lado_cuadrado)}")
print(f"Seno de 45°: {math.sin(math.radians(45)):.3f}")
print(f"Redondeo de π: {round(math.pi, 2)}")

# RESUMEN FINAL
print(f"\n=== RESUMEN ===")
print(f"Datos personales:")
print(f"- Nombre: {nombre} (tipo: {type(nombre)})")
print(f"- Edad: {edad} (tipo: {type(edad)})")
print(f"- Altura: {altura} (tipo: {type(altura)})")
print(f"- Materias: {materias} (tipo: {type(materias)})")
print("¡Programa completado!")

