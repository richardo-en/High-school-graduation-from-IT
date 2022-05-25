# prvočísla

n = int(input('vstup\n'))

# výstup
vypis = ""
for i in range(n+1):
    prvocislo = True
    if(i>1):
        for j in range(i):
            if(j>1 and j<i):
                if(i%j==0):
                    prvocislo = False
    else:
        prvocislo = False
    if(prvocislo==True):
        vypis += str(i)+" "
print(vypis)
