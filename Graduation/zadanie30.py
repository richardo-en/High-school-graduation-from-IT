while True:
    sirka = int(input("Zadaj šírku poľa.\n"))
    vyska = int(input("Zadaj šírku poľa.\n"))
    for i in range(vyska):
        print(" " + sirka * "---")
        print(" " + sirka * "|  " + "|")
    print(" " + sirka * "---")
    pokracovat = str(input("chces pokracovat? ano/nie\n"))
    if pokracovat == "ano":
        pass
    elif pokracovat == "nie":
        print("Maj sa!")
        break
