# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
# (muutuja - variable, tingimus - condition, if-lause - if statement)

a = int(input("input number: "))
b = int(input("input number: "))

if a < b:
    print("minimal numb is:", a)
elif a == b:
    print("number are equal")
else:
    print("minimal numb is:", b)
