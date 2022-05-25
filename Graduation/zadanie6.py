while True:
    zadane_cislo = int(input("zadaj cislo ktoreho mame spravit násobilku.\n"))
    for i in range(1,11):
        cislo = i*zadane_cislo
        print(f"{i} * {zadane_cislo} = {cislo}")
    pokracovat = str(input("chces pokracovat? ano/nie\n"))
    if pokracovat == "ano":
        pass
    elif pokracovat == "nie":
        print("Maj sa!")
        break