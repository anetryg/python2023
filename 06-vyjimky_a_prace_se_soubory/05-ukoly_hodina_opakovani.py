# Úkol 1
"""Napište funkci nahrad_samohlasky, která bude mít jeden parametr (řetězec) a nahradí všechny samohlásky ve slově znakem '-'. Funkce vrátí upravený řetězec. 

"""

samohlasky = "aeiouAEIOU"
def nahrad_samohlasky(retezec):
    vysledek = ""
    for i in retezec:
        if i in samohlasky:
            vysledek += '-'
        else:
            vysledek += i
        
    print(vysledek)
        
nahrad_samohlasky('ahoj')
    

# Úkol 2
"""Napište funkci secti_prvni_a_posledni, která bude mít jako parametr seznam čísel. Funkce sečte první a poslední prvek seznamu a vrátí výsledek."""

def secti_prvni_a_posledni(seznam):
    soucet = seznam[0] + seznam[-1]
    print(soucet)
    
secti_prvni_a_posledni([2,3,4,5,6])

# Úkol 3
"""Napište funkci overeni_hesla, která bude mít jeden parametr (heslo). Funkce ověří, zda heslo splňuje následující podmínky:
- Je dlouhé alespoň 8 znaků
- Obsahuje alespoň jedno velké písmeno
- Obsahuje alespoň jedno malé písmeno
- Obsahuje alespoň jedno číslo
Funkce vrátí True, pokud heslo splňuje všechny podmínky, jinak vrátí False. Použijte isupper() - kontrola velkého písmena, islower() - kontrola malého písmena, isdigit() - kontrola čísla."""


def overeni_hesla(heslo):
    velke_pismeno = False
    male_pismeno = False
    cislo = False
    if len(heslo) >= 8:
        for x in heslo:
            if x.isupper():
                velke_pismeno = True
            elif x.islower():
                male_pismeno = True
            elif x.isdigit():
                cislo = True
        if velke_pismeno == True and male_pismeno == True and cislo == True:
            return True
        else:
            return False
    else:
        return False
    
print(overeni_hesla("muni2368")) 
            
        


# Úkol 4
"""Napište funkci unikatni_slova, která načte text od uživatele jako řetězec a vypíše počet unikátních slov ve zadaném textu. Program by měl ignorovat velikost písmen, tj. slova "Pes" a "pes" by měla být považována za stejná. (lower, split, set)"""

def unikatni_slova(text):
    text_lower = text.lower()
    vysledek = text_lower.split()
    return len(set(vysledek))

print(unikatni_slova("Ahoj dneska je hezky je hezky"))
    

