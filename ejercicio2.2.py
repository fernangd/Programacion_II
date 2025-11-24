# ============================================================================
# EJEMPLO 2: HERENCIA - Sistema de Animales
# ============================================================================

class Animal:
    """Clase base para todos los animales"""
    
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def comer(self, cantidad):
        """Aumenta el peso del animal al comer"""
        self.peso += cantidad
        return f"{self.nombre} ha comido {cantidad}kg"
    
    def hacer_sonido(self):
        """Método genérico para hacer sonido"""
        return "El animal hace un sonido"
    
    def mostrar_info(self):
        """Muestra información básica del animal"""
        return f"{self.nombre} - Edad: {self.edad} años - Peso: {self.peso}kg"

class Perro(Animal):
    """Clase Perro que hereda de Animal"""
    
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)     #super(): accede al constructor de la clase base
        self.raza = raza
        self.entrenamientos = 0
    
    def hacer_sonido(self):
        """Sobrescribe el método para el ladrido del perro"""
        return f"{self.nombre} dice: ¡Guau guau!"
    
    def entrenar(self):
        """Entrena al perro"""
        self.entrenamientos += 1
        return f"{self.nombre} ha completado {self.entrenamientos} entrenamientos"

class Gato(Animal):
    """Clase Gato que hereda de Animal"""
    
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color
        self.vidas = 9
    
    def hacer_sonido(self):
        """Sobrescribe el método para el maullido del gato"""
        return f"{self.nombre} dice: ¡Miau miau!"
    
    def ronronear(self):
        """Método específico de los gatos"""
        return f"{self.nombre} está ronroneando felizmente"

class Pajaro(Animal):
    """Clase Pájaro que hereda de Animal"""
    
    def __init__(self, nombre, edad, peso, puede_volar=True):
        super().__init__(nombre, edad, peso)
        self.puede_volar = puede_volar
    
    def hacer_sonido(self):
        """Sobrescribe el método para el canto del pájaro"""
        return f"{self.nombre} dice: ¡Pío pío!"
    
    def volar(self):
        """Método específico de los pájaros"""
        if self.puede_volar:
            return f"{self.nombre} está volando"
        return f"{self.nombre} no puede volar"

# Uso del ejemplo
print("=" * 70)
print("EJEMPLO 2: HERENCIA - Sistema de Animales")
print("=" * 70)

perro = Perro("Rex", 3, 25, "Labrador")
gato = Gato("Misi", 2, 4, "Naranja")
pajaro = Pajaro("Piolín", 1, 0.5)

print(perro.mostrar_info())
print(perro.hacer_sonido())
print(perro.entrenar())
print()
print(gato.mostrar_info())
print(gato.hacer_sonido())
print(gato.ronronear())
print()
print(pajaro.mostrar_info())
print(pajaro.hacer_sonido())
print(pajaro.volar())
