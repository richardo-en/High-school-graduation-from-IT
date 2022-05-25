# vstup
from ntpath import join
import random

n = int(input())
matica = []
pom = 1
"""
# výstup
for i in range(n):
    riadok = []
    for j in range(n):
       riadok.append(i[])
       pom +=1
    matica.append(riadok)
"""

for i in range(n):
    for j in range(n):
        matica.append(str(random.randint(1, 200)))
print(matica)

s=0
matica2 = []
for i in range(n):
    matica2 = []
    for j in range(n):
        matica2.append(matica[s+j])
        tab_matica2 = "\t".join(matica2)
    print (tab_matica2)
    s += n
