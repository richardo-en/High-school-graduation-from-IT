#Napíšte program,ktorý vypočíta BMI index a vypíše, či máte alebo nemáte nadváhu. BMI (telesný hmotnostný index) sa vyráta ako podiel hmotnosti v kilogramoch a druhej mocniny výšky v metroch , BMI < 18,5 podváha, 18,5 <= BMI < 25 normálna hmotnosť, 25 <= BMI < 30 nadváha, BMI > 30 obezita.
hmotnost=float(input(" zadaj tvoju hmotnosť v kg: "))
vyska_v_cm=float(input(" zadaj tvoju výšku v centimetroch: "))
vyska_v_m=vyska_v_cm/100
bmi=hmotnost/(vyska_v_m*vyska_v_m)
bmi_string = str(bmi)
if bmi<18.5: print("Tvoje bmi je: ", bmi_string[:5], "čo je podváha")
if 18.5<= bmi < 25: print("Tvoje bmi je: ", bmi_string[:5], "čo je normálna hmotnosť")
if 25<= bmi <30: print("Tvoje bmi je: ", bmi_string[:5], "čo je nadváha")
if bmi>30: print("Tvoje bmi je: ", bmi_string[:5], "čo je obezita")

             
