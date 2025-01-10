# UPC vöötkoodi kontrollsumma arvutamise ülesanne. Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri kontrollsumma arvutamise funktsioon.

def ups_check(n):
    # print(n)
    res = 0
    res2 = 0
    for i in range(0,11, 2):
        # print(n[i])
        res += int(n[i])

    res *= 3
    # print(res)
    for i in range(1,11,2):
        # print(n[i])
        res2 += int(n[i])
    m = (res2 + res)%10
    if m != 0:
        print(10 - m)
    else:
        print(m)
    

ups_check('00001234567')
