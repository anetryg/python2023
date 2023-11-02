#Úkol 1
"""Napište program, který vezme seznam slov a vytvoří nový seznam, který obsahuje délky těchto slov."""

seznam_slov = ["pes", "kočka", "hory", "ryba"]
delky_slov = []

for slovo in seznam_slov:
    delky_slov.append(len(slovo))

print(delky_slov)


#Úkol 2
"""Napište program, který vypočítá sinus každého úhlu v seznamu a uloží výsledky do nového seznamu. Použijte metodu sin z knihovny math."""

import math

uhly = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi]
sinusy = []

for uhel in uhly:
    sinusy.append(math.sin(uhel))

print(sinusy)


#Úkol 3
"""Napište program, který generuje 10 náhodných čísel a poté vytvoří seznam těch čísel, která jsou menší než 0.5."""


import random

num_count = 10

random_numbers = []
for _ in range(num_count):
    random_numbers.append(random.random())

filtered_numbers = []
for num in random_numbers:
    if num < 0.5:
        filtered_numbers.append(num)

print("Vygenerovaná náhodná čísla:", random_numbers)
print("Čísla menší než 0.5:", filtered_numbers)



#Úkol 4
"""Uvažujme vysvědčení, které máme zapsané jako slovník.

Napiš program, který spočte průměrnou známku ze všech předmětů.
Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1."""

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

total_marks = sum(school_report.values())
count = len(school_report)
average_mark = total_marks / count

print(f"Průměrná známka: {average_mark}")

subjects_with_grade_1 = []
for subject, grade in school_report.items():
    if grade == 1:
        subjects_with_grade_1.append(subject)

print("Předměty s hodnocením 1:", subjects_with_grade_1)

#Úkol 5
"""V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P."""

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

owners_in_Plzen = []

for plate, owner in plates.items():
    if plate[1] == 'P':
        owners_in_Plzen.append(owner)

print(f"Majitelé vozidel registrovaných v Plzeňském kraji:{owners_in_Plzen}")
