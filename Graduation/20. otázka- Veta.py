sent = input("Napiste vetu: ")

pole1=[]
pole2=[]
pole3=[]
pole4=[]

cisla= 0
spoluhlasky= 0
samohlasky= 0
ostatne=0
for i in sent:
    if i in "1234567890" :
        cisla = cisla+1
        pole1.append(i)
    elif i in " aeiouäáéíóúiaieiuôAEIOUÁÉÍÓÚ" :
        samohlasky = samohlasky +1
        pole2.append(i)
    elif i in "bcčdďdzdžfghchjklľĺmnňpqrŕsštťvwxzžBCČDĎFGHJKLĽMNŇPRSŠTŤVWXZŽ" :
        spoluhlasky = spoluhlasky +1
        pole3.append(i)
    else:
        ostatne = ostatne +1
        pole4.append(i)

print(f"Počet čísel: {cisla} a su to {pole1} , počet samohlasiek je: {samohlasky} a su to {pole2} , počet spoluhlasiek je: {spoluhlasky} a su to {pole3} , počet ostatnych znakov je: {ostatne} a su to {pole4}")