# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.


aastat = int(input("enter aastat "))

if aastat % 4 == 0 and aastat % 100 != 0 or aastat % 400 == 0:
    print(aastat, "on liigaasta")
else:
    print(aastat, "on lihtaasta")