import random

def generate(length, min_val, max_val):
    output = ''
    state = False
    remaining = length

    while remaining > 0:
        sample = random.randint(min_val, max_val)
        if sample > remaining:  # Ensure we don't exceed the length
            sample = remaining

        output += ('1' if state else '0') * sample
        state = not state
        remaining -= sample

    return output

'''
Uloha 1.
Vytvorte funkciu, ktorá bude simulovať hod kockou. Kockou hádžeme náhodne 20 krát.
Vypíšte koľko krát sa nám podarilo vypísať čísla 1,2,3,4,5 a 6.
Pre výber náhodného prvku z poľa môžeme použiť funkciu random.choice()

Napríklad:
array= [1,2,0,100,4]
random_number = random.choice (array)
'''

'''
Uloha 2.
Uvažujme pole obsahujúce 8 rôznych farieb. Vyberte náhodnu farbu a vypíšte ju. 
'''

'''
Uloha 3.
Vypíšte náhodné číslo, ktoré je deliteľné 7 a 5 zároveň.
'''


'''
Uloha 4.
Vytvorte simuláciu hry kameň papier nožnice. Hra končí v momente keď jeden z hráčov
dosiahne 3 body.
'''
