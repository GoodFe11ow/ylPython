# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input("a is: "))
b = float(input("b is: "))
c = float(input("c is: "))

if not (a + b > c and a + c > b and b + c > a):
    print("kolmnurk not exist")
elif a == b == a:
    print("kolmnurk on ravnostoronii")
else:
    print("kolmnurk on raznostoroniy")
