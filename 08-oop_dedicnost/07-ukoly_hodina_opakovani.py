# Úkol 1
""" Vytvořte třídu Car, která reprezentuje automobil. Třída by měla mít atributy brand (značka auta), model (model auta), a is_running (informace o tom, zda je auto zapnuté - True, pokud ano, False, pokud ne). Přidej metodu start_engine(), která zapne motor auta, pokud není již zapnutý.
"""

class Car:
    """ něco něco """
    def __init__(self, brand: str, model: str, is_running: bool):
        self.brand = brand
        self.model = model
        self.is_running = is_running
    
    def start_engine(self):
        if self.is_running == False:
            self.is_running = True
            print("Nastartoval jsi")
        else:
            print("motor už běží")

auto = Car("vw", "golf", False)
auto.start_engine()

# Úkol 2
""" Navrhněte třídu Movie reprezentující film. Třída by měla mít atributy title (název filmu), director (režisér), a duration (délka filmu v minutách). Přidej metodu get_full_info(), která vypíše kompletní informace o filmu. Pokud je délka filmu neznámá (None), vypište pouze název a režiséra.
"""
class Movie:
    def __init__(self,title,director,durtion):
        self.title = title
        self.director = director
        self.duration = durtion
        
    def get_full_info(self):
        if self.duration == None:
            print(self.director, self.title)
            
        else:
            print(self.title, self.director, self.duration)
            
film = Movie("Pán prstenů", "J:R:R. Tolkien", None)
film.get_full_info()
            

# Úkol 3
""" Vytvoř třídu Song reprezentující píseň. Třída by měla mít atributy title (název písně), artist (interpret), duration (délka písně v minutách), a genre (žánr písně, defaultně nastaven na "Pop"). Přidej metodu play(), která vypíše zprávu o přehrávání písně. Před přehráním písně ověřte, zda je délka písně větší než 0, a vypište odpovídající zprávu.
"""


# Úkol 4
""" Vytvořte třídu Dog reprezentující psa. Třída by měla mít atributy name (jméno psa), breed (plemeno psa), age (věk psa), a is_hungry (informace o tom, zda je pes hladový - True, pokud ano, False, pokud ne). Přidej metodu feed(), která nakrmí psa a změní stav is_hungry na False. Pokud je pes již nakrmený, vypište o tom informaci.
"""
class Dog:
    def __init__(self,name,breed,age,is_hungry):
        self.name=name
        self.breed=breed
        self.age=age
        self.is_hungry=is_hungry
    def feed(self):
        if self.is_hungry==False:
            self.is_hungry=True
            print('pes je nakrmen')
        else:
            print('pes není hladový')
pes=Dog('Alík','pudl','10',False)
pes.feed()
pes.feed()
print(pes.name, pes.age)

