# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. 
# Arvuta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 	22 + 222 = 246). 
# Ära kasuta korrutamistehet. Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

n = input("Input integer from 1 to 9: ")
n3 = n + n + n
n2 = n + n
n4 = int(n) + int(n2) +int(n3)
print(n, "+", n2, "+", n3, "=", n4)
