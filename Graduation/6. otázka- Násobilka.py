#Napíšte program, ktorý pre dané číslo vypíše násobky od 1 do 10.
a = int (input("Pre ktoré číslo chceš násobilku?\n"))

for b in range (1,11):    
    c = a * b 
    print (a,"x" ,b,"=",c)


# studuj.it

n = int(input("Pre ktoré číslo chceš násobilku?\n"))

# výstup
vypis = ""
for i in range(10):
    vysledok = (i+1)*n
    vypis = str(i+1)+"x"+str(n)+"="+str(vysledok)
    print(vypis)

