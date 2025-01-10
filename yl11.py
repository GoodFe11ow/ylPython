# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

word = input("write a word: ")
print(word)
word = word.strip()
print(word, "2")

if len(word) >= 7 and len(word) % 2 != 0:
    middle = len(word) // 2
    print(word[middle-1:middle+2])
else:
    print("wrong")

