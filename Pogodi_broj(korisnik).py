# Korisnik unosi broj koji pokušavamo pogoditi

class KriviBroj(Exception):
    pass
def Provjera(korisnik1,korisnik2):
    if korisnik1==korisnik2:
        print("Pogodili ste broj")
    else:
        print("Niste pogodili broj")
        print("Broj je bio:"+ str(korisnik1))

try:
 korisnik1=int(input("Korisnik1,molimo unesite broj između 1 i 10: "))
 korisnik2=int(input("Korisnik2,molimo unesite za koji mislite da ga je odabrao Korisnik1: "))
except ValueError:print("Niste unjeli broj!")
if korisnik1<1 or korisnik2<1or korisnik1>10 or korisnik2>10:
    raise KriviBroj(print("Broj ne odgovara uvjetima"))
Provjera(korisnik1,korisnik2)