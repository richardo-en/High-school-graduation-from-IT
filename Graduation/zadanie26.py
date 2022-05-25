jed = 0
dvo = 0
tro = 0
stvo = 0
pat = 0
while True:
    znamka = int(input("Akú známku dostal žiak (1,2,3,4,5). Keď chceš ukončit pridávanie známok zadaj 0.\n"))
    if znamka == 1:
        jed +=1
    elif znamka == 2:
        dvo +=1
    elif znamka == 3:
        tro +=1
    elif znamka == 4:
        stvo +=1
    elif znamka == 5:
        pat += 1
    elif znamka == 0:
        break
    else:
        print("Zadal si číslo ktoré nieje známka!")
print(f"Dokopy známok bolo {jed + dvo + tro + stvo + pat}. Jednotiek bolo {jed} , dvojok bolo {dvo} , trojek bolo {tro} , štvoriek bolo {stvo} a päťiek bolo {pat}")