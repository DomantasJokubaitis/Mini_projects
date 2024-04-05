import random

class Character:

    def __init__(self, name):

        self.name = name
        self.health = 100


    def health_lowering(self, damage):
        """lowers the defenders health by damage dealt"""
        self.health -= damage

    def critical_hit(self, damage):
        """small chance for critical hit, which increases damage dealt 1.5 times"""
        self.damage = damage
        critical_chance = random.randint(1, 100)

        if critical_chance > 85:
            self.damage = round(self.damage * 1.5)
            print(f"Critical hit! -{self.damage} hp")
        else:
            print(f"Regular attack -{self.damage} hp")

        return self.damage
        
    def show_hp(self, defender):
        """shows the defenders health"""
        print("|-------------------|")
        print(f"| {defender.name} health: {defender.health} hp |")
        print("|-------------------|")

    def attack(self, attacker, defender, attack_name, fail_chance, min_damage, max_damage):
        """generates a random number from 1 to 100, if that number is bigger than the fail chance, damage is dealt to defender"""
        chance = random.randint(0, 100)

        if chance > fail_chance:
            print(f"\n{attacker.name} used {attack_name}! ")
            damage = random.randint(min_damage, max_damage)
            self.critical_hit(damage)
            defender.health_lowering(self.damage)

            if defender.health < 0:
                defender.health = 0
                self.show_hp(defender)
            else:
                self.show_hp(defender)

        else:
            print(f"\n{defender.name} dodged the {attack_name.lower()} attack! ")
            self.show_hp(defender)

    def punch(self):
        self.attack(my_character, ai_character, "Punch", 20, 10, 20)

    def kick(self):
        self.attack(my_character, ai_character, "Kick", 50, 25, 35)

    def body_slam(self):
        self.attack(my_character, ai_character,"Body slam", 75, 45, 65)


    def aipunch(self):
        self.attack(ai_character, my_character, "Punch", 20, 10, 20)

    def aikick(self):
        self.attack(ai_character, my_character, "Kick", 50, 25, 35)

    def aibody_slam(self):
        self.attack(ai_character, my_character, "Body slam", 75, 45, 65)


name = input("Enter your characters nickname: ").title()
while len(name) > 20:
    name = input("The name must be, at max, 20 characters long. Try again: ")

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
        print(f"\nNot a legal move! {name} is disqualified! ")
        break
    if ai_character.health > 0:
        ai_move = random.randint(1,3)
        if ai_move == 1:
            my_character.aipunch()
        elif ai_move == 2:
            my_character.aikick()
        elif ai_move == 3:
            my_character.aibody_slam()
    

if ai_character.health == 0:
    print(f"\n{name} wins! ")

if my_character.health == 0:
    print(f"\nAi wins! ")

###bugs###

# Ai can attack after it's health drops down to zero on the same turn (fixed)

###features###
##By importance, starting from the top##

# Critical hits(DONE)
# Show damage dealt as -##(DONE)
# Instead of attack failing, should be enemy dodged attack(DONE)
# When choosing move, show attack success rate percentage and possible damage dealt
# Play again, save name
# Dynamic dashes (----) highlighting hp, for longer names, more dashes should be printed, the hp also should be in a box
# Dynamic stamina system, attacks drain stamina, can be recharged by skipping turn
# Lithuanian language, input change_language or smth to change language
# Healing (limited use, maybe potion?)
# Store data about fight, like moves commited, in a file
# Skillpoints? Like strength, endurance
# Ai hardness?

###Swords and sandals ugly copy LOL






