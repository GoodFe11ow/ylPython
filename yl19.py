# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

vowels = 'eyuoiüõäöa'
text = "Kuressaare Ametikool"
vowel_count = 0
for c in text.lower():
    if c in vowels:
        print(c)
        vowel_count += 1
print(vowel_count)


