import random

class Character:

    def __init__(self, name):

        self.name = name
        self.health = 100


    def health_lowering(self, damage):
        self.health -= damage

    def attack(self, attack_name, fail_chance, min_damage, max_damage):
        chance = random.randint(0, 100)
        if chance > fail_chance:
            print(f"{attack_name} attack succesful! ")
            damage = random.randint(min_damage, max_damage)
            ai_character.health_lowering(damage)
            if ai_character.health < 0:
                ai_character.health = 0
                print(f"Ai health: {ai_character.health}")
            else:
                print(f"Ai health: {ai_character.health}")
        else:
            print(f"{attack_name} attack failed! ")
            print(f"Ai health: {ai_character.health}")

    def punch(self):
        self.attack("Punch", 20, 10, 20)

    def kick(self):
        self.attack("Kick", 50, 20, 35)

    def body_slam(self):
        self.attack("Body slam", 75, 45, 65)

    def aiattack(self, attack_name, fail_chance, min_damage, max_damage):

        chance = random.randint(0, 100)
        if chance > fail_chance:
            print(f"Ai chose {attack_name}! ")
            damage = random.randint(min_damage, max_damage)
            my_character.health_lowering(damage)
            if my_character.health < 0:
                my_character.health = 0
                print(f"Your health: {my_character.health}")
            else:
                print(f"Your health: {my_character.health}")
        else:
            print("Ai attack failed! ")
            print(f"Your health: {my_character.health}")

    def aipunch(self):
        self.aiattack("Punch", 20, 10, 20)

    def aikick(self):
        self.aiattack("Kick", 50, 20, 35)

    def aibody_slam(self):
        self.aiattack("Body slam", 75, 45, 65)


name = input("Enter your characters nickname: ")

my_character = Character(name)
ai_character = Character("AI")

while ai_character.health > 0 and my_character.health > 0:

    move = input(f"\nPunch, kick or body slam: ").lower()
    if move == "punch":
        ai_character.punch()
    elif move == "kick":
        ai_character.kick()
    elif move == "body slam":
        ai_character.body_slam()
    else:
        print(f"\nNot a legal move! Disqualified! ")
        break
    if ai_character.health > 0:
        ai_move = random.randint(1,3)
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

###bugs###

# Ai can attack after it's health drops down to zero on the same turn (fixed)




