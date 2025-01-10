f = open('input22.1.txt', 'r')
lines =[line.strip() for line in f.readlines()]
max_elf = 0
elf = 0
cL = []
for line in  lines:
    
    if line == '':
        if elf > max_elf:
            max_elf = elf
        cL.append(elf)
        elf = 0
        # print('tuhi rida')

    else:
        elf += int(line)    
cL.sort(reverse=True)
print(max_elf)
print(cL)

print(sum(cL[:3]))
print(cL[0], cL[1], cL[2])