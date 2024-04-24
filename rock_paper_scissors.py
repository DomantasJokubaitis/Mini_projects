import random

types = ["rock", "paper", "scissors"]
number = random.randint(0, 2)
ai_choice = types[number]
human_choice = input("rock, paper or scissors: \n").lower()

while human_choice not in types:
    human_choice = input("I said rock, paper or scissors! ")
print(f"\nai chooses {ai_choice}, human chooses {human_choice}")
if ai_choice == human_choice:
    print(f"\nDraw! ")
elif ai_choice == "paper" and human_choice == "rock" or ai_choice == "rock" and human_choice == "scissors" or ai_choice == "scissors" and human_choice == "paper" :
    print(f"\nAi wins! ")
else:
    print(f"\nHuman wins! ")
