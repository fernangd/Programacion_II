
# ============================================================================
# EJEMPLO 1: CLASES Y OBJETOS - Sistema de Empleados
# ============================================================================

class Empleado:
    """Clase que representa un empleado de una empresa"""
    
    def __init__(self, nombre, id_empleado, salario_base, departamento):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base
        self.departamento = departamento         
        self.horas_extra = 0
    
    def registrar_horas_extra(self, horas):
        """Registra las horas extra trabajadas"""
        self.horas_extra += horas
        print(f"{self.nombre} ha registrado {horas} horas extra")
    
    def calcular_salario_total(self):
        """Calcula el salario total incluyendo horas extra"""
        pago_hora_extra = (self.salario_base / 160) * 1.5  # 50% adicional
        total = self.salario_base + (self.horas_extra * pago_hora_extra)
        return total
    
    def mostrar_info(self):
        """Muestra la información del empleado"""
        print(" ")
        print(f"--- Información del Empleado ---")
        print(f"ID: {self.id_empleado}")
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario Base: L.{self.salario_base:,.2f}")
        print(f"Horas Extra: {self.horas_extra}")
        print(f"Salario Total: L.{self.calcular_salario_total():,.2f}")

# Uso del ejemplo
print("=" * 70)
print("EJEMPLO 1: CLASES Y OBJETOS - Sistema de Empleados")
print("=" * 70)

emp1 = Empleado("Carlos Méndez", "1005-1985-00534", 3000, "Desarrollo")
emp1.mostrar_info()
emp1.registrar_horas_extra(10)
emp1.registrar_horas_extra(5)
emp1.mostrar_info()

