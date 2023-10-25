#Úkol 1
""" Vytvořte seznam jmen. Za každé jméno chceme přidat pomocí cyklu konec e-mailové adresy (například máme v seznamu jméno "Aneta" a chceme za něj přidat "@gmail.com"). Vypište maily na obrazovku. """

seznam_jmen = ["Han", "Luke", "Leia"]
for jmeno in seznam_jmen:
    print(f"{jmeno}@gmail.com")

#Úkol 2
""" Vytvořte seznam produktů a k jejich názvům pomocí cyklu přidejte čísla (např. "Jablko 1", "Banán 2" atd.) pomocí cyklu. Vypište výsledek na obrazovku. """

pocitadlo = 1
seznam_produktu = ['jablko','parek','klobáska', "kdgjhk"]

for x in seznam_produktu:
    print(x, pocitadlo)
    pocitadlo += 1
    
#řešení pomocí range
seznam_produktu = ['jablko', 'parek','klobáska']

#řešení pomocí enumerate
seznam_produktu = ['jablko', 'parek', 'klobáska']

for index, produkt in enumerate(seznam_produktu, start=1):
    print(f"{produkt} {index}")


for x in range(len(seznam_produktu)):
    print(x, seznam_produktu[x])


#Úkol 3
""" Vytvořte seznam školních známek. Následně pomocí cyklu spočítejte počet jedniček. """

seznam_znamek = [1, 2, 3, 1, 1, 2, 3, 4]
pocet_jednicek = 0

for x in seznam_znamek:
    if x == 1:
        pocet_jednicek += 1

print(pocet_jednicek)

# řešení bez použití cyklu
print(seznam_znamek.count(1))


#Úkol 4
""" Vytvořte program, který spočítá součet všech lichých čísel v zadaném seznamu čísel."""

licha_cisla = 0
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in seznam:
    if x % 2 != 0:
        licha_cisla += x
        
print(licha_cisla)
        


#Úkol 5
""" Vytvořte program, který uživateli pomocí cyklu while umožní hádat číslo, které si počítač "myslí" (uložte na začátku libovolné číslo do proměnné). Uživatel hádá, dokud se netrefí. Pak se program ukončí. """

#Úkol 6
""" Rozšiřte předchozí program tak, aby uživatel dostával zpětnou vazbu, zda je číslo větší nebo menší"""

cislo = 6

while True:
    uhadni_cislo = int(input("Uhádni číslo:"))
    if uhadni_cislo == cislo:
        break
    elif uhadni_cislo > cislo:
        print("zadej menší číslo")
    elif uhadni_cislo < cislo:
        print("zadej větší číslo")



#Úkol 7
""" Vytvořte program, který pomocí cyklu spočítá součet všech čísel v seznamu. """

seznam = [1, 2, 5, 4, 7, 8, 6]
soucet = 0

for cislo in seznam:
    soucet += cislo

print(soucet)

# řešení pomocí sum
soucet = sum(seznam)
print(soucet)


#Úkol 8
""" Máte seznam hesel viz níže. Pomocí cyklu vypište všechny hesla na obrazovku. Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků."""

hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]

for i in hesla:
    if len(i) > 8:
        print(i)

#Úkol 9
""" Napište cyklus, který projde zadaný seznam desetinných čísel a spočítá jejich průměr. Seznam čísel si vytvořte na začátku programu. """

seznam = [1.2, 1.4]
pocet = 0
soucet = 0

for i in seznam:
    pocet += 1
    soucet += i
    
print(soucet/pocet)

#Úkol 10
""" Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu. """

seznam = [5, 5, 4, 6, 8, 2]
nejvyssi_hodnota = 0

for i in seznam:
    if i > nejvyssi_hodnota:
        nejvyssi_hodnota = i
        
print(nejvyssi_hodnota)

# řešení pomocí max
print(max(seznam))

#Úkol 11
""" Vytvořte program, který vezme dva seznamy a vrátí seznam, který obsahuje pouze ty prvky, které se nacházejí v obou původních seznamech."""

seznam_a = [1, 2, 3]
seznam_b = [1, 2, 4]
seznam_c = []

for i in seznam_a:
    if i in seznam_b:
        seznam_c.append(i)
        
print(seznam_c)
 
 


