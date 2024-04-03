import random

class Character:

    def __init__(self, name):

        self.name = name
        self.health = 100


    def health_lowering(self, damage):
        self.health -= damage

    def punch(self):

        chance = random.randint(0, 100)
        if chance > 20:
            print("Attack succesful! ")
            damage = random.randint(10, 20)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(ai_character.health)
            else:
                print(ai_character.health)
        else:
            print("Attack failed! ")
            print(ai_character.health)

    def kick(self):
        chance = random.randint(0, 100)
        if chance > 50:
            print("Attack succesful! ")
            damage = random.randint(20, 35)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(ai_character.health)
            else:
                print(ai_character.health)
        else:
            print("Attack failed! ")
            print(ai_character.health)

    def body_slam(self):
        chance = random.randint(0, 100)
        if chance > 75:
            print("Attack succesful! ")
            damage = random.randint(40, 65)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(ai_character.health)
            else:
                print(ai_character.health)
        else:
            print("Attack failed! ")
            print(ai_character.health)


    
name = input("Enter your characters nickname: ")

my_character = Character(name)
ai_character = Character("AI")

while ai_character.health > 0:

    move = input("Punch, kick or body slam: ").lower()
    if move == "punch":
        ai_character.punch()
    elif move == "kick":
        ai_character.kick()
    elif move == "body slam":
        ai_character.body_slam()
    else:
        print("Not a legal move! Disqualified! ")
        break

if ai_character.health == 0:
    print("You win! ")

