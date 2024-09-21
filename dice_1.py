import random

while True:
    choise = input("Roll the dice? (y/n):").lower()
    if choise == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        print(f"({dice1}, {dice2}, {dice3})")
    elif choise == "n":
        print('Thanks for playing!')
        break    
    else:
        print("Invalid Choise! please enetr 'y' and 'n.")