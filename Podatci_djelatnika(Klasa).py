# Korisštenje klase za dohvat,obradu i čuvanje podataka
import random
class Djelatnik():
    def __init__(self, ime,prezime,godine,godine_rada):
        self.ime=ime
        self.prezime=prezime
        self.godine=godine
        self.godine_rada=godine_rada

    def placa(self):
        return random.randint(5000,15000)


class Odjel_posla():
    def __init__(self,ime,kat,soba,radni_sati):
        self.ime=ime
        self.kat=kat
        self.soba=soba
        self.radni_sati=radni_sati
        self.zaposlenici=[]

    def dodavanje_zaposlenika(self,zaposlenici):
        self.zaposlenici.append(zaposlenici)



Djelatnik1=Djelatnik("Marko","Marić",36,20)
Djelatnik2=Djelatnik("Pero","Perić",50,30)
Djelatnik3=Djelatnik("Josip","Jozić",25,5)


Odjel_posla1=Odjel_posla("Administracija",3,2,40)
Odjel_posla2=Odjel_posla("IT","Prizemlje",10,40)
Odjel_posla3=Odjel_posla("Menađment",10,20.20)

Odjel_posla.dodavanje_zaposlenika(Djelatnik1,Djelatnik2,Djelatnik3)
print(Djelatnik1.ime,Djelatnik1.placa())