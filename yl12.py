# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp

fruits = ["banana", "apple", "grape"]
print(fruits[0])

fruits.append("cherry")
print(fruits)

print(fruits[-1])

fruits[2] = "watermelon"
print(fruits)

if "apple" in fruits:
    print("it is")
else:
    print("no apple")

print(len(fruits))

fruits.pop(1)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort(reverse=True)
print(fruits)