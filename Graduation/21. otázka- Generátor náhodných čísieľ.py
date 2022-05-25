import random
pokus = 0
hadaj = random.randint(1, 100)
print("Myslím si celé číslo od 1 do 100. Ty ho budeš hádať")
pokracuj = True
while pokracuj:
    pokus += 1
    cislo = int(input("Zadaj tvoj tip: "))

    if hadaj > cislo:
        print("Myslím si väčšie číslo.")
    elif hadaj < cislo:
        print("Myslím si menšie číslo.")
    else:
        print("Uhádol si na", pokus," pokus")
        pokracuj = False
