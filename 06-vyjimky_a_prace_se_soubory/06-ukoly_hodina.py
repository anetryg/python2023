# Úkol 1
""" Napište program, který bude očekávat od uživatele dva parametry. Parametry mohou být celá nebo desetinná čísla. Vypiš podíl těchto čísel. Ošetři, aby program nezhavaroval při pokusu o dělení nulou. """

try:
    cislo = float(input("Zadejte číslo: "))
    cislo2 = float(input("Zadejte druhé číslo: "))
    
    print(cislo / cislo2)
except:
    print("Nemůžete dělit nulou! Zkuste to znovu.")
finally:
    print("Děkuji.")

# Úkol 2
""" Vytvořte textový soubor vykaz.txt, který bude obsahovat 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok."""

with open('myfile.txt', 'w', encoding='utf-8') as file:
    for line in range(1,13):
        file.write("10\n")


# Úkol 3
""" Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat. """

nazev = input("Zadejte název souboru:")

with open(nazev, 'w', encoding='utf-8') as file:
    file.write(input("Zadejte řádek textu:"))


# Úkol 4
""" Napište program, který vytvoří nový textový soubor s názvem "poznamky.txt". Program by měl načítat poznámky od uživatele, až dokud uživatel nezadá prázdný řetězec. Každá poznámka by měla být zapsána na nový řádek v souboru.
"""
with open('poznamky.txt','w') as file:
    while True:
        poznamky=input('Zadej poznámky: ')
        if poznamky=='':
            break
        else: 
            file.write(poznamky)
        

# Úkol 5
""" Napište program, který umožní uživateli zkopírovat obsah jednoho souboru do druhého. Program by měl zeptat se na názvy zdrojového a cílového souboru a poté přečíst obsah z jednoho souboru a zapsat ho do druhého.
"""

odkud = input('Odkud chceš kopírovat text? ')
kam = input('a kam ko chceš zkopírovat? ')

with open(odkud,'r') as zdroj:
    text = zdroj.read()
    with open(kam,'w') as cil:
        cil.write(text)
            

# Úkol 6
""" Stáhněte si slohovou práci sloh.txt. Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno.
"""

nazev_souboru = "sloh.txt"

with open(nazev_souboru,'r') as zdroj:
    text=zdroj.read()
    print(len(text.split()))
    
