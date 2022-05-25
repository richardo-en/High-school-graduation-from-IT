while True:

    decimal = int(input("Enter a decimal number \n"))
    binary = 0
    ctr = 0
    temp = decimal  

    while(temp > 0):
        binary += ((temp%2)*(10**ctr))
        temp = temp//2
        ctr += 1
    print(f"Binary of {decimal} is: {binary}")

    odpoved = str(input("chces pokracovat? ano/nie\n"))

    if odpoved == "nie":
        break
    elif odpoved == "ano":
        pass
    else:
        while True:
            odpoved2 = str(input("zla odpoved! Chces pokracovat? ano/nie\n"))
            if odpoved2 == "nie":
                exit()
            elif odpoved2 == "ano":
                break
            else:
                pass