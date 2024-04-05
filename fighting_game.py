import random

class Character:

    def __init__(self, name):

        self.name = name
        self.health = 100


    def health_lowering(self, damage):
        self.health -= damage

    def critical_hit(self, damage):
        self.damage = damage
        critical_chance = random.randint(1, 100)
        if critical_chance > 85:
            self.damage = round(self.damage * 1.5)
            print("Critical hit! ")
            return self.damage
        else:
            print("Regular attack ")
            return self.damage
        
    def show_my_hp(self):
        print(f"Your health: {my_character.health}")

    def show_ai_hp(self):
        print(f"Ai health: {ai_character.health}")

    def attack(self, attack_name, fail_chance, min_damage, max_damage):
        chance = random.randint(0, 100)
        if chance > fail_chance:
            print(f"\n{attack_name} attack succesful! ")
            damage = random.randint(min_damage, max_damage)
            self.critical_hit(damage)
            ai_character.health_lowering(self.damage)
            if ai_character.health < 0:
                ai_character.health = 0
                self.show_ai_hp()
            else:
                self.show_ai_hp()
        else:
            print(f"\n{attack_name} attack failed! ")
            self.show_ai_hp()

    def punch(self):
        self.attack("Punch", 20, 10, 20)

    def kick(self):
        self.attack("Kick", 50, 25, 35)

    def body_slam(self):
        self.attack("Body slam", 75, 45, 65)


    def aiattack(self, attack_name, fail_chance, min_damage, max_damage):

        chance = random.randint(0, 100)
        if chance > fail_chance:
            print(f"\nAi chose {attack_name}! ")
            damage = random.randint(min_damage, max_damage)
            self.critical_hit(damage)
            my_character.health_lowering(self.damage)
            if my_character.health < 0:
                my_character.health = 0
                self.show_my_hp()
            else:
                self.show_my_hp()
        else:
            print(f"\nAi attack failed! ")
            self.show_my_hp()

    def aipunch(self):
        self.aiattack("Punch", 20, 10, 20)

    def aikick(self):
        self.aiattack("Kick", 50, 25, 35)

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

###features###

# Critical hits(done)
# Show damage dealt as -##
# Healing (limited use)
# Stamina
# Store date about fight in json file
# Skillpoints?
# Ai hardness?




