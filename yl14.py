# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (ext - extension - faili laiend) 
# ja prindib välja laiendi (“ext”). (str.split)

file = input('write file name .ext: ')
print(file.split(".")[-1])