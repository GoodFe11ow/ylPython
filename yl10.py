# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, 
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, 
# siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

name = input("What is your name: ")
print("Hello ", name)
liv = input("where r you living: ")
if  liv == "Saaremaa":
    print("thats great, im also")
age = int(input("How old r you: "))
if age < 18:
    print("You too yong for driving")
elif age == 18:
    print("congratulations on coming of age")
else:
    print("You can drive")