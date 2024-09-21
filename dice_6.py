import random
while True:
    choice = input("Roll the dice? (y/n)").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)
        dice5 = random.randint(1, 6)
        dice6 = random.randint(1, 6)
        print(f"({dice1}, {dice2}, {dice3}, {dice4}, {dice5}, {dice6})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
