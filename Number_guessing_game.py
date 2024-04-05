import random

"""did this before starting to read 'Python crash course 3rd edition'; previously had done cs50p, although haven't finished it"""

def game():

    choice = int(input("Let's play a game! Try to guess what number 1-50 am I thinking off: "))
    x = random.randint(1, 50)
    answ = ["y", "n"]

    while choice != x :

        while choice not in range(51) :
            choice = int(input("The range is 1-50. Input a valid number: "))

        while choice < x and choice > -1:
            choice = int(input("Too low! Guess again: "))

        while choice > x and choice < 51:
            choice = int(input("Too high! Guess again: "))

        if choice == x:
            repeat = input(f"That's right! It was {x}. Would you like to play again? y/n: ")

            if repeat == "y":
                game()
            elif repeat == "n":
                print("Have a good one! ")
                break
            while repeat not in answ:
                repeat = input("Would you like to play again? y/n: ")

game()
