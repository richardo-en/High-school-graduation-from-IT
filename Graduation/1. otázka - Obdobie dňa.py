while True:
    a = int(input("zadaj číslo od 1 po 12.. \n"))
    while (a >12) or (a<1):
        print("Nezadal si spravne hodnotu maš ďalši pokus")
        a = int(input("zadaj číslo od 1 po 12.. \n"))

    b = input("zadaj dopo alebo  popo .. \n")
    while (b != "dopo") and (b != "popo"):
        print("Nezadal si spravne hodnotu maš ďalši pokus")
        b = input("zadaj dopo alebo  popo .. \n")

    if (b == "dopo" and a>=6 and a <=12) or( b == "popo" and a>=1 and a < 8 ):
            print ("den")
    else :
        print ("noc")
        
