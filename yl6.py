# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)


a = input("a: ")
b = input("b: ")
c = input("c: ")

if a > b and a > c:
    print("maximum", a)
elif b > c:
    print("maximum", b)
else:
    print("maximum", c)