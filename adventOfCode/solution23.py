f = open("input23.txt", 'r')

lines = f.readlines()
res = 0

for line in lines:
    digits = ''
    for c in line:
        if c.isdigit():
            digits += c
            number = int(digits[0] + digits[-1])
    res += number
print(res)




print()