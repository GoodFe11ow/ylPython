f = open("input.txt","r")

lines = f.readlines()

fisrt = []
second = []

for line in lines:
    # line -> ['3 4'\n] -> line.split() -> ['3', '4'] -> el -> '3' and el -> '4' int(el) -> [3, 4]
    a, b =[int(l) for l in line.split()]
    fisrt.append(a)
    second.append(b)
    
fisrt.sort()
second.sort()

res1 = 0
res2 = 0
for i in range(len(fisrt)):
    res1 += abs(fisrt[i] - second[i])
    res2 += fisrt[i] * second.count(fisrt[i])
    
print("Resultat 1 is: ", res1)
print("Resultat 2 is: ", res2)
