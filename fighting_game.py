import random
import json
from pathlib import Path

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
        """shows the defenders health and a dynamic health bar"""
        lines = round(defender.health * 0.4)
        print(f"\n")
        print(f"|{lines * "-"}|")
        print(f"|{lines * "-"}|")

        print(f"{defender.name} health: {defender.health} hp")

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

    def get_info(self, game_end = 0, loss = 0, win = 0):
        path = Path("stats.json")
        if path.exists():
            content = path.read_text()
            my_stats_dict = json.loads(content)
            my_stats_dict["game_over_times"] += game_end
            my_stats_dict["losses"] += loss
            my_stats_dict["wins"] += win
            content = json.dumps(my_stats_dict)
            path.write_text(content)
        else:
            my_stats_dict = {}
            game_over_times = 0
            game_over_times += game_end
            losses = 0
            losses += loss
            wins = 0
            wins += win
            my_stats_dict["game_over_times"] = game_over_times
            my_stats_dict["losses"] = losses
            my_stats_dict["wins"] = wins
            content = json.dumps(my_stats_dict)
            path.write_text(content)

    def info_reading(self):
        path = Path("stats.json")
        content = path.read_text()
        my_stats_dict = json.loads(content)
        print(f"In total there were {my_stats_dict["game_over_times"]} games played. You won {my_stats_dict["wins"]} of them and lost {my_stats_dict["losses"]} of them. ")

         

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



def main():

    is_active = True

    while is_active == True:

        while ai_character.health > 0 and my_character.health > 0:

            move = input(f"\nPunch, kick or body slam: ").lower()
            if move == "punch":
                ai_character.punch()
            elif move == "kick":
                ai_character.kick()
            elif move == "body slam":
                ai_character.body_slam()
            else:
                print(f"\nNot a legal move! {name} skips a turn! ")
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
                my_character.get_info(1, 0, 1)
                choice = input("Play again? y/n: ").lower()
                if choice == "y":
                    my_character.health, ai_character.health = 100, 100
                    main()
                elif choice == "n":
                    is_active = False
                    return is_active
                    print("Bye")

            elif my_character.health == 0:
                print(f"\nAi wins! ")
                my_character.get_info(1, 1, 0)
                choice = input("Play again? y/n: ").lower()
                if choice == "y":
                    my_character.health, ai_character.health = 100, 100
                    main()
                elif choice == "n":
                    is_active = False
                    return is_active
                    print("Bye")



print("Start game or view game stats? ")
your_choice = input().lower()
if your_choice == "stats":
    my_character.info_reading()
    your_choice = input()
if your_choice == "start":
    main()
elif your_choice == "quit" or your_choice == "q":
    is_active = False
else:
    print("Command was not recognised, restart the game! ")


   
###needs###
# alot of repetitive code, need to use more functions
# should ask start or stats first, not for character name, but i need the character name to create a character instance and use stats function
# start or stats need prettier formating


###bugs###

# Ai can attack after it's health drops down to zero on the same turn (fixed)
# when choosing 'n' to end the game, for some reason it ends only when there is a print line after the 'return is_active' line

###features###
##By importance, starting from the top##

# Critical hits(DONE)
# Show damage dealt as -##(DONE)
# Instead of attack failing, should be enemy dodged attack(DONE)
# When choosing move, show attack success rate percentage and possible damage dealt
# Play again, save name
# Dynamic dashes (----) highlighting hp(maybe better formating)(DONE)
# Dynamic stamina system, attacks drain stamina, can be recharged by skipping turn
# Lithuanian language, input change_language or smth to change language
# Healing (limited use, maybe potion?)
# Store data about fight, like moves commited, in a file

###Swords and sandals ugly copy LOL






