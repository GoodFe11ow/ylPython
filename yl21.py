# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random

while True:

    the_number = random.randint(0, 100)
    print("try to guess the number")
    guess = None
    while guess != the_number:
        guess = int(input("enter number: "))
        if guess > the_number:
            print("the number is higher")
        elif guess < the_number:
            print("the number is lower")
        else:
            print("the number is right") 
    if input('Wanna play more? y - yes, n - no: ').lower() == 'n':
        break