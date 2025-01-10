# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline ilist - multi dimensional)

pet = input("Lemmikloom: ")
print(pet[0])

pets = ["dog", "mouse", "snake"]
pets.append(pet)
print(pets)
print(pets[-1][-1])
