import random
#print (random.randint(1, 20))
pocet_cisel_v_poli = int (input ("Ake veľké mám vytvoriť pole?\n"))

counter = range(0, pocet_cisel_v_poli)
pole = []
i=0
#cislo = random.randint(1, 20)
for i in counter:    
    pole.append(random.randint(1, 20))
    #i =+1

print (list(pole))

hladane_cislo = int (input ("Aké číslo hľadáš?\n"))
if hladane_cislo in pole:
    print ("Nachádza sa v poli.")
else:
    print ("Nenachádza sa v poli. Smola")




#a = int (input ("Zadaj hľadané číslo: "))
#x = [10,3,5,4,8]

#if a in x:
#    print ("Áno")
#else:
#    print ("Nie")
