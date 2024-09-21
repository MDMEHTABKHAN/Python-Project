import random
number_guessing = random.randint(1,100)

while True:
    try:
        user_input = int(input("Guess the number between 1 to 100: "))

        if user_input < number_guessing:
            print("Too low")

        elif user_input > number_guessing:
            print("Too high") 
            break

        else:
            print("Congratulation")
            break
        
    except ValueError:
        print("please enter a valid number")

        