#Zisti známku z udaných percent
maximum = int(input("Zadaj maximum bodov: "))
body = float(input("Kolko bodov dosiahol? "))
percenta = (body*100)/maximum


#percenta= int(input("Zadaj percentá z testu od 0 do 100: "))

print()
if (percenta >100 or percenta <0) : print ("chybny vstup")
if 100>= percenta >90 : print("za ",round(percenta,3),"% získavaš známku 1 - výborný")
if 90>= percenta >75 :print("za",round(percenta,3),"% získavaš známku 2 - chválitebný")
if 75>= percenta >50 :print("za",round(percenta,3),"% získavaš známku 3 - dobrý")
if 50>= percenta >30 :print("za",round(percenta,3),"% získavaš známku 4 - dostatočný")
if percenta <=30 : print("za",round(percenta,3),"% získavaš známku 5 - nedostatočný")