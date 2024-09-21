import random
while True:
    choice = input("Roll the dice? (y/n): ").lower()  

    if choice == "y":
        dice = [random.randint(1, 6) for _ in range(6)]  
        print(f"Dice rolled: {dice}")
    
    elif choice == "n":
        print("Thanks for playing!")
        break  
    
    else:
        print("Invalid choice! Please enter 'y' or 'n'.")
