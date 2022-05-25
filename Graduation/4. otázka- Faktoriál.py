a = int (input ("Zadaj číslo z ktorého mám spraviť faktoriál: " ))
x = 1
if a == 0:
    print (" Faktoriál 0 je 1 ")
else:
    if a < 0:
        print ("Z tohto faktoriál nie je kámo")
    else:
        if a > 0:
            while a > 0:
                x *= a
                a = a - 1
            print (x)
