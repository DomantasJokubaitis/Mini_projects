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
                print(f"Ai health: {ai_character.health}")
            else:
                print(f"Ai health: {ai_character.health}")
        else:
            print("Attack failed! ")
            print(f"Ai health: {ai_character.health}")

    def kick(self):
        chance = random.randint(0, 100)
        if chance > 50:
            print("Attack succesful! ")
            damage = random.randint(20, 35)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(f"Ai health: {ai_character.health}")
            else:
                print(f"Ai health: {ai_character.health}")
        else:
            print("Attack failed! ")
            print(f"Ai health: {ai_character.health}")

    def body_slam(self):
        chance = random.randint(0, 100)
        if chance > 75:
            print("Attack succesful! ")
            damage = random.randint(40, 65)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(f"Ai health: {ai_character.health}")
            else:
                print(f"Ai health: {ai_character.health}")
        else:
            print("Attack failed! ")
            print(f"Ai health: {ai_character.health}")

    def aipunch(self):

        chance = random.randint(0, 100)
        if chance > 20:
            print("Ai chose punch! ")
            damage = random.randint(10, 20)
            my_character.health_lowering(damage)
            if my_character.health < 0:
                my_character.health = 0
                print(f"Your health: {my_character.health}")
            else:
                print(f"Your health: {my_character.health}")
        else:
            print("Ai attack failed! ")
            print(f"Your health: {my_character.health}")

    def aikick(self):
        chance = random.randint(0, 100)
        if chance > 50:
            print("Ai chose kick! ")
            damage = random.randint(20, 35)
            my_character.health_lowering(damage)
            if my_character.health < 0:
                my_character.health = 0
                print(f"Your health: {my_character.health}")
            else:
                print(f"Your health: {my_character.health}")
        else:
            print("Ai attack failed! ")
            print(f"Your health: {my_character.health}")

    def aibody_slam(self):
        chance = random.randint(0, 100)
        if chance > 75:
            print("Ai chose body slam! ")
            damage = random.randint(40, 65)
            my_character.health_lowering(damage)
            if my_character.health < 0:
                my_character.health = 0
                print(f"Your health: {my_character.health}")
            else:
                print(f"Your health: {my_character.health}")
        else:
            print("Ai attack failed! ")
            print(f"Your health: {my_character.health}")


    
name = input("Enter your characters nickname: ")

my_character = Character(name)
ai_character = Character("AI")

while ai_character.health > 0 and my_character.health > 0:

    move = input(f"\nPunch, kick or body slam: ").lower()
    ai_move = random.randint(1,3)
    if move == "punch":
        ai_character.punch()
    elif move == "kick":
        ai_character.kick()
    elif move == "body slam":
        ai_character.body_slam()
    else:
        print(f"\nNot a legal move! Disqualified! ")
        break
    if ai_move == 1:
        my_character.aipunch()
    if ai_move == 2:
        my_character.aikick()
    if ai_move == 3:
        my_character.aibody_slam()
    

if ai_character.health == 0:
    print(f"\n{name} wins! ")

if my_character.health == 0:
    print(f"\nAi wins! ")



