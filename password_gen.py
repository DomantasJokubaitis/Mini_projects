import random

capital_letters = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M"

capital_letters_list = [letter for letter in capital_letters.split(" ")]
regular_letters_list = [letter.lower() for letter in capital_letters.split(" ")]
numbers = [number for number in range(0, 10)]
valid_characters = "~ ` ! @ # $ % ^ & * ( ) _ - + = { [ } ] | : ; \" ' < , > . ? /"
valid_characters_list = [character for character in valid_characters.split(" ")]

all_lists = [capital_letters_list, regular_letters_list, numbers, valid_characters_list]

def generating():
    picked_list = random.choice(all_lists)
    picked_item = random.choice(picked_list)
    return picked_item

desired_length = int(input("Enter the length of the desired password: "))

def concatination(desired_length):

    password = ""
    while desired_length > 0:
        item = generating()
        password += str(item)
        desired_length -= 1
    return password

password = concatination(desired_length)

print(f"Your password: {password}")
