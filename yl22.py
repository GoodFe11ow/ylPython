# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

import random
choices = ['paper', 'rock', 'scissors']
while True:
    user_choice = input("choose rock, scissors or paper: ")
    computer_choice = random.choice(choices)
    print('computer choose: ',computer_choice)
    if user_choice not in choices:
        print('Try again')
        continue
    if user_choice == computer_choice:
        print('draw!')
    elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    else:
        print('You lose')
    if input('wanna play more? y or n: ').lower() == 'n':
        break