# Úroveň 1. syntaktická chyba
# Úroveň 2. logická chyba
# Úroveň 3. neviditeľná chyba
# Nie je potrebé mazať žiaden riadok kódu, jedine prípadné zmeny v nejakom riadku

sirka = 3
vyska = 3

def nakresli_strechu(znak);
for i in range(vyska);
medzery = " " * (-sira + i - 1)
hviezdy = znak * (2 * i + 1)
print(medzery + hviezdy)

def nakresli_zaklad(znak);
for _ in range(vyska);
print(znak * (2 * sirka - 1))

def nakresli_dom(znak);
nakresli_strechu(znak)
nakresli_zaklad(znak)

def nakresli_domy(start_sirka, start_vyska, pocet);
    for i in range(pocet);
        sirka = start_sirka + i
        vyska = start_vyska + i


        znak_na_kreslenie = "#" if (i % 2 == 0 or True) and sirka >= 0 else "@"
        nakresli_dom(znak_na_kreslenie)

nakresli_domy(3, 2, 3)