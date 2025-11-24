# ============================================================================
# EJEMPLO 3: POLIMORFISMO - Sistema de Formas Geométricas
# ============================================================================

import math

class Forma:
    """Clase base para todas las formas geométricas"""
    
    def area(self):
        """Método abstracto para calcular área"""
        pass
    
    def perimetro(self):
        """Método abstracto para calcular perímetro"""
        pass

class Rectangulo(Forma):
    """Clase Rectángulo"""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectángulo(base={self.base}, altura={self.altura})"

class Circulo(Forma):
    """Clase Círculo"""
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Círculo(radio={self.radio})"

class Triangulo(Forma):
    """Clase Triángulo"""
    
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def __str__(self):
        return f"Triángulo(base={self.base}, altura={self.altura})"

def imprimir_info_forma(forma):
    """Función polimórfica que trabaja con cualquier forma"""
    print(f"\n{forma}")
    print(f"Área: {forma.area():.2f}")
    print(f"Perímetro: {forma.perimetro():.2f}")

# Uso del ejemplo
print("=" * 70)
print("EJEMPLO 3: POLIMORFISMO - Formas Geométricas")
print("=" * 70)

# Crear diferentes formas
formas = [
    Rectangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4, 5, 5, 6)
]

# Polimorfismo en acción: el mismo método funciona para todas las formas
for forma in formas:
    imprimir_info_forma(forma)

print("\n--- Cálculo de área total ---")
area_total = sum(forma.area() for forma in formas)
print(f"Área total de todas las formas: {area_total:.2f}")
