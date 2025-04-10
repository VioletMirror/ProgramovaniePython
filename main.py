# Zadania na hodinu 10.4. 2025

"""
Úloha 1.
Majme slovník: {“mesto”:”Bratislava”, “dedina”: Vlkolínec} . Pridajte do slovníku akúkoľvek
hodnotu s kľúčom štát.
"""

"""
Úloha 2.
Majme slovník: 

slovnik = {“mesto”:”Bratislava”, “dedina”: "Vlkolinec"} 
 
Napíšte funkciu, ktorá dostane ako parameter názov slovenského mesta. Následne vráti 
True ak slovník obsahuje zadané
mesto a False ak nie. 
"""


"""
Úloha 3.
Vytvorte funkciu, ktorá sčíta počet všetkých obyvateľ miest v slovníku:

Obyvatelia = {"Bratislava":500000, "Pezinok":25000, "Presov": 100000, "Humenne": 40000}

(výsledok 665 000)
"""

"""
Úloha 4.
Ktoré mesto obsahuje najväčší počet obyvateľov? Napíšte funkciu, ktorá vráti mesto s najväčším počtom obyvateľov.

Môžte použiť slovník:
Obyvatelia = {"Bratislava":500000, "Pezinok":25000, "Presov": 100000, "Humenne": 40000}
"""

"""
Úloha 5.
Pomocou nasledujúci polí vytvorte slovník:

keys = [1,2,3,4]
values = ["one", "two", "three", "four"]
"""


"""
Úloha 6.
Funckia dostane ako parameter string. Do slovníka uložte aké písmená string obsahuje a aký je ich počet:

Napríklad:
slovo = “adam”

výsledný slovník
pismena = {“a”: 2, “d”: 1, “m”: 1}
"""

################################################################################

"""
Úloha 7.

Majme slovník:

osoba = {"meno": "Janko", "vek": 12}

Zmeň hodnotu kľúča "vek" na inú hodnotu podľa vlastného výberu. Slovník po úprave vypíš.
"""

"""
Úloha 8.
Napíš funkciu, ktorá dostane ako parameter slovník s názvami miest a počtom obyvateľov.

napr.

Obyvatelia = {"Bratislava":500000, "Pezinok":25000, "Presov": 100000, "Humenne": 40000}

Funkcia má vrátiť počet miest, ktoré majú viac ako 50 000 obyvateľov.
"""

"""
Úloha 9.
Majme slovník:

zvierata = {"pes": "hafka", "macka": "mnauka", "krava": "muka"}

Napíš funkciu, ktorá dostane ako vstup názov zvieraťa (napr. "pes") a vráti, aký zvuk vydáva.
Ak zviera v slovníku nie je, funkcia má vrátiť text: "Zvieratko nepoznam".
"""

"""
Úloha 10.
Napíš funkciu, ktorá dostane ako parameter slovník so slovenskými slovami a ich anglickými prekladmi, napríklad:

preklady = {"jablko": "apple", "dom": "house"}

Funkcia má vytvoriť vety, kde každá dvojica bude zapísaná vo formáte:
„slovenské slovo znamená anglické slovo“

Príklad:
na vstupe zadané slovo "jablko"

Výsledok:

"jablko znamená apple, dom znamená house"
"""


"""
BONUS
Implementujte zjednodušenú hash tabuľku pomocou slovníka s názvom "table". Kód bude obsahovať 3. funkcie:

funkcia 1. my_hash(string)
– Vypočíta hash zo stringu. Výstupom funkcie je číslo získané zo stringu a to také, aby ak zmením vo vstupnom stringu jedno písmeno na veľké/malé tak sa číslo zmení.
pre získanie ASCII hodnoty daného znaku v stringu použite funkciu ord(). 

Použitie ord(): 
Táto funkcia vracia ASCII hodnotu znaku zadaného ako argument teda
znak = ord("A")
print(znak)

výsledok: 65

funkcia 2. insert(table, string)
– Použije funkciu my_hash() na získanie kľúča, a vloží reťazec do slovníka table ako hodnotu pod týmto kľúčom.

funkcia 3. search(table, string)
– Pomocou my_hash() vypočíta hash zo zadaného reťazca a vráti hodnotu zo slovníka pod týmto kľúčom, ak existuje. Ak nie, vráti napríklad "Nenájdené".
"""

roman_dict = {
    1000: "M",
    900:  "CM",
    500:  "D",
    400:  "CD",
    100:  "C",
    90:   "XC",
    50:   "L",
    40:   "XL",
    10:   "X",
    9:    "IX",
    5:    "V",
    4:    "IV",
    1:    "I"
}
