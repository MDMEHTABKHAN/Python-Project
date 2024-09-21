import random

number_guessing = random.randint(10,100)
while True:
    user_input = int(input("Guess the number betwwen 10 to 100:"))

    if user_input < number_guessing:
        print("Low!")

    elif user_input > number_guessing:
        print("High!")

    else:
         print("Congratulation")
         break 