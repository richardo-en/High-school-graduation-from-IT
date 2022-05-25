random_cislo = 0
while True:
    list = [1]
    pocet_cisel = int(input("Zadaj počet čísel.\n"))
    for i in range(1 , pocet_cisel):
        list.append(list[-1] * 2)
    print(*list, sep=" , ")
    pokracovat = str(input("chces pokracovat? ano/nie\n"))
    if pokracovat == "ano":
        pass
    elif pokracovat == "nie":
        print("Maj sa!\n")
        break
    else:
        while True:
            a = str(input("chces pokracovat? ano/nie\n"))
            if a == "nie":
                exit()
            elif a == "ano":
                break
            else:
                pass