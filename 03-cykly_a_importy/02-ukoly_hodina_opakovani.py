#Úkol 1
""" Napište program, který bude vyžadovat vstup od uživatele. Pokud uživatel zadá číslo, program zjistí, zda je to liché nebo sudé. Pokud zadá slovo "konec", program se ukončí. """

vstup = input("Zadejte číslo:")

if vstup == "konec":
    print("konec programu")
elif int(vstup) % 2 == 0:
    print("číslo je sudé")
elif int(vstup) % 2 != 0:
    print("číslo je liché")

#Úkol 2
""" Požádejte uživatele o zadání uživatelského jména a hesla. Pokud se zadané údaje shodují s referenčními údaji, tedy uživatelským jménem "admin" a heslem "heslo123", uživateli bude umožněn přístup, jinak program vypíše "Přístup zakázán". """

jmeno = input("zadejte jméno")
heslo = input("zadejte heslo")

if jmeno == "admin" and heslo == "heslo123":
    print("přístup umožněn")
else:
    print("přístup zakázán")

#Úkol 3
""" Napište program, který požádá uživatele o zadání celého čísla. Program poté zkontroluje, zda je toto číslo dělitelné buď 2 nebo 3, a vytiskne příslušnou zprávu. Pokud číslo není dělitelné ani 2, ani 3, program by měl vypsat, že číslo není dělitelné ani jedním z těchto čísel. """

vstup = input("zadejte celé číslo")

if int(vstup) % 2 == 0 and int(vstup) % 3 == 0:
    print("číslo je dělitelné 2 a 3")
elif int(vstup) % 2 == 0:
    print("číslo je dělitelné 2")
elif int(vstup) % 3 == 0:
    print("číslo je dělitelné 3")
else:
    print("číslo není dělitelné 2 ani 3!")

#Úkol 4
""" Napište program, který odstraní všechny opakující se prvky ze seznamu a vytvoří nový seznam bez duplicity."""

seznam = [1, 2, 3, 1, 2]

print(list(set(seznam)))

#Úkol 5
""" Požádejte uživatele o zadání jeho věku, pokud je mu více než 18 - vypiště hlášku, že na stránky může vstoupit, pokud méně, že nemůže. """

vstup = input("zadejte věk")

if int(vstup) > 18:
    print("můžete vstoupit")
else:
    print("nemůžete vstoupit")

#Úkol 6 
""" Načtěte věk uživatele a poté vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel
    
    0 euro pro návštěvníky mladší 6 let,
    65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
    100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
    50% ze základní ceny pro ostatní (senior). 
    
Plná cena je 12 euro. 
"""

vek = int(input("Zadej svůj věk: "))

if vek < 6:
    cena = 0
elif 6 <= vek <= 26:
    cena = 0.65
elif 27 <= vek <= 64:
    cena = 1
else:
    cena = 0.5

print(f"Cena vstupu je {cena} euro.")


