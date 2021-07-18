# Jednostavna igra Kamen,Škare,Papir

import random

Korisnik = input("Unesite odabir(kamen,skare,papir): ")
Kompjutor= random.choice(["kamen", "skare", "papir"])
print("Vi ste odabrali "+Korisnik+", Kompjutor je odabrao "+Kompjutor)

if Korisnik == Kompjutor:
    print(f"Both players selected"+ Kompjutor+". izjednačeno")
elif Korisnik == "kamen":
    if Kompjutor == "skare":
        print("Kamen pobjeđuje Škare, Pobjedili ste !")
    else:
        print("Papir pobjeđuje kamen, Izgubili ste ")
elif Korisnik == "papir":
    if Kompjutor== "kamen":
        print("Papir pobjeđuje kamen,Pobjedili ste ")
    else:
        print("Škare pobjeđuju papir, Izgubili ste")
elif Korisnik == "skare":
    if Kompjutor == "papir":
        print("Škare pobjeđuju papir,Pobjedili ste ")
    else:
        print("Papir pobjeđuje skare, izgubili ste ")