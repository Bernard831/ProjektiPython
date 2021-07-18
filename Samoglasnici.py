samoglasnici=["A","a","E","e","I","i","O","o","U","u"]
rijec=input("Unesite riječ: ")
brojac=0
for n in rijec:
   if n in samoglasnici:
       brojac+=1
print(" U rijeci se nalazi "+str(brojac)+" samoglasnika")




