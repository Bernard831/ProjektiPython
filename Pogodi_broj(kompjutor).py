# Moramo pogoditi broj koji je kompjutor odbrao

import random
class Kriva_Vrijednost(Exception):
 pass

def Provjera(broj_kompjutora,vas_broj):
    if vas_broj==broj_kompjutora:
        print("Pogodili ste broj")
    else:
        print("Niste pogodili broj")
        print("Broj je bio: "+str(broj_kompjutora))

broj_kompjutor=random.randint(1,10)
try:
 vas_broj=int(input("Unesite vas broj (veci od  i manji od 10): "))
except ValueError:print("Niste unjeli broj")
if vas_broj<1 or vas_broj>10:
    raise Kriva_Vrijednost(print("Broj ne ispunjava kriterije"))
else:
    Provjera(broj_kompjutor,vas_broj)
