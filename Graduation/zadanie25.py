while True:
    vek = int(input("Zadajte vek diváka. Ked chces odsit z kina zadaj 0.\n"))
    if vek <= 6:
        print("vstup je zadarmo pretoze je to dieta\n")
    elif vek <= 15:
        print("vstup je 5 euro pretoze je to student.\n")
    elif vek <= 60:
        print("vstup je 7 euro pretoze divak je dospely jedinec.\n")
    elif vek > 60:
        print("vstup su 2 eura pretoze divak jedochodca.\n")
    elif vek == 0:
        print("Maj sa!")
        break
    else:
        pass