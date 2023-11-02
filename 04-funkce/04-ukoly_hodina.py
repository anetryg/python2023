#Úkol 1
"""Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek."""

def mult(a, b):
    return a * b

vysledek = mult(5, 3)
print(vysledek)


#Úkol 2
"""Napište funkci vypocet_obvodu_obdelnika, která bude mít dva parametry (délku a šířku) a vrátí obvod obdélníka. o = 2(a+b)"""

def vypocet_obvodu_obdelnika(delka, sirka):
    obvod = 2 * (delka + sirka)
    return obvod

obvod = vypocet_obvodu_obdelnika(4, 6)
print(obvod)


#Úkol 3
"""Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

Zadej slovo: ahoj
********
* ahoj *
********
"""

def obal_hvezdickami(retezec):
    delka = len(retezec) + 4
    print('*' * delka)
    print(f'* {retezec} *')
    print('*' * delka)

obal_hvezdickami("ahoj")


#Úkol 4
"""Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50."""

def month_of_birth(rodne_cislo):
    mesic_cislo = int(rodne_cislo[2:4])
    
    if mesic_cislo > 50:
        mesic_cislo -= 50
    
    return mesic_cislo

rodne_cislo_muz = "950212/1234"
rodne_cislo_zena = "015312/5678"

mesic_muz = month_of_birth(rodne_cislo_muz)
mesic_zena = month_of_birth(rodne_cislo_zena)

print(f"Měsíc narození muže: {mesic_muz}")
print(f"Měsíc narození ženy: {mesic_zena}")


#Úkol 5
"""Napište funkci analyza_textu, která bude mít jeden parametr (textový řetězec). Funkce spočítá a vrátí počet slov a počet vět v zadaném textu."""

def analyza_textu(text):
    interpunkce = [".", "!", "?"]
    
    slova = text.split()
    pocet_slov = len(slova)
    
    pocet_vet = 0
    for znak in interpunkce:
        pocet_vet += text.count(znak)

    return pocet_slov, pocet_vet

print(analyza_textu("Ahoj, neco neco. Ahoj ahoj!"))

#Úkol 6
"""Napište funkci palindrom, která bude mít jako parametr řetězec a vrátí True, pokud je řetězec palindrom, jinak vrátí False. Palindrom je řetězec, který je stejný i po převrácení."""

def palindrom(retezec):
    retezec_reverz = ""
    for i in range(len(retezec) - 1, -1, -1):
        retezec_reverz += retezec[i]
    return retezec == retezec_reverz

# Testování funkce
print(palindrom("radar"))
print(palindrom("hello"))


