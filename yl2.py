from math import pi

var1 = int(input("Sisesta raadius: "))
rinPin = pi*var1**2
print("Ringi pindala: ",round(rinPin, 2))
diam = 2*var1
umbMdu = pi*diam
print("Ümbermõõdu",round(umbMdu, 2))
