# vstup
slovo = str(input('slovo '))
retazec = str(input('retazec '))
novy_retazec = str(input('novy retazec '))
nove_slovo = ""
pom = 0

# výstup
for i in range(len(slovo)):
    if(slovo[i:i+len(retazec)]==retazec):
        nove_slovo += novy_retazec
        pom = i+len(retazec)
    elif(i>=pom):
        nove_slovo += slovo[i]

print(nove_slovo)