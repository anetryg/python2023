import math

# Úkol 1
""" Uvažujme, že chceme modelovat různé geometrické tvary jako čtverec, kruh a obdélník. Využijeme dědičnosti k vytvoření obecné třídy Shape.
 
Třída Shape by měla mít následující atributy:
- color (barva tvaru, defaultně nastavena na "white")
- filled (informace o tom, zda je tvar vyplněný, defaultně True)

Třída Shape by měla mít následující metody:
- __init__(self, color="white", filled=True): konstruktor třídy.
- display_info(self): Metoda pro zobrazení informací o tvaru.
- calculate_area(self): Metoda pro výpočet obsahu tvaru (metoda s pass, určená k přepsání v odvozených třídách).
"""
    
class Shape:
    def __init__(self, color="white", filled=True):
        self.color = color
        self.filled = filled
        
    def display_info(self):
        print(self.color, self.filled)
        
    def calculate_area(self):
        pass




# Úkol 2
""" Od třídy Shape odvoďtě třídy Rectangle a Circle.

Třída Rectangle by měla mít následující atributy:
- length (délka obdélníka)
- width (šířka obdélníka)

Třída Circle by měla mít následující atributy:
- radius (poloměr kruhu)

Obě třídy by měly přepsat metodu calculate_area pro konkrétní výpočet obsahu pro každý tvar.
"""
class Rectangle(Shape):
    def __init__(self, length, width, color="white", filled=True):
        super().__init__(color, filled)
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius, color="white", filled=True):
        super().__init__(color, filled)
        self.radius = radius
        
    def calculate_area(self):
        return (math.pi * self.radius)**2
    
""" shape1 = Circle(5)
print(shape1.calculate_area()) 
shape2 = Rectangle(2, 6)
print(shape2.calculate_area()) """


# Úkol 3
""" Uvažujme online obchod s oblečením, kde máme různé typy oblečení, jako jsou trička, kalhoty a bundy. Použijeme dědičnost k vytvoření obecné třídy ClothingItem - a od ní odvozených tříd pro konkrétní typy oblečení.

Třída ClothingItem by měla mít následující atributy:
- name (název oblečení)
- size (velikost oblečení)
- color (barva oblečení)
- price (cena oblečení v korunách)

Třída ClothingItem by měla mít následující metody:
- __init__(self, name, size, color, price): Konstruktor třídy.
- display_info(self): Metoda pro zobrazení informací o kusu oblečení.
- calculate_discounted_price(self, discount_percentage): Metoda pro výpočet slevy na cenu oblečení."""

class ClothingItem:
    def __init__(self,name, size, color, prize):
        self.name = name
        self.size = size
        self.color = color
        self.prize = prize
        
    def display_info(self):
        print(self.name, self.size, self.color, self.prize)
        
    def calculate_discounted_price(self, procento_slevy):
        discount = (procento_slevy / 100) * self.prize
        discounted_price = self.prize - discount
        return discounted_price
    
""" tricko = ClothingItem("polo", "XL", "modra", 1000)

tricko.display_info()

print(tricko.calculate_discounted_price(15)) """


    
# Úkol 4
""" Od třídy ClothingItem odvoďtě třídy TShirt a Pants.

Třída TShirt by měla mít následující atributy:
- fabric (typ látky trička)

Třída Pants by měla mít následující atributy:
- fit (střih kalhot)

Metody pro třídu TShirt:
- add_logo(self, logo): Simuluje přidání loga na tričko.

Metody pro třídu Pants:
- adjust_length(self, new_length): Simuluje úpravu délky kalhot na novou délku.

"""

class TShirt(ClothingItem):
    def __init__(self,name, size, color, prize, fabric):
        super().__init__(name, size, color, prize)
        self.fabric = fabric
    def add_logo(self, logo):
        print(f"{logo}Polo bolo pridané")
        
class Pants(ClothingItem):
    def __init__(self,name, size, color, prize, fit):
        super().__init__(name, size, color, prize)
        self.fit = fit
    def adjust_length(self, new_length):
        print(f"Dlžka bola zmenená")
        
tricko = TShirt("Nike", "XL", "Black", 45, "bavlna")
kalhoty = Pants("Adidas", "L", "Blue", 50, "Slim Fit")

tricko.add_logo("Nike")
print(tricko.calculate_discounted_price(30))
kalhoty.adjust_length("120")
        

# Úkol 5
""" Přepiš předchozí příklad pomocí datových tříd."""

from dataclasses import dataclass

@dataclass
class ClothingItem:
    name: str
    size: str
    color: str
    prize: int
        
    def display_info(self):
        print(self.name, self.size, self.color, self.prize)
        
    def calculate_discounted_price(self, procento_slevy):
        discount = (procento_slevy / 100) * self.prize
        discounted_price = self.prize - discount
        return discounted_price
