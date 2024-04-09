import random
import json
from pathlib import Path
import sys

class Character:

    def __init__(self, name):

        self.name = name
        if self.name == "":
            self.name = "nameless"
        self.health = 100
        self.stamina = 100


    def health_lowering(self, damage):
        """lowers the defenders health by damage dealt"""
        self.health -= damage

    def show_hp(self, defender):
        """shows the defenders health and a dynamic health bar"""
        lines = round(defender.health * 0.4)
        print(f"\n")
        print(f"|{lines * "-"}|")
        print(f"|{lines * "-"}|")

        print(f"{defender.name} health: {defender.health} hp")

    def stamina_lowering(self, tiredness):
        self.stamina -= tiredness

    def show_stamina(self, defender):
        if defender.stamina < 0:
            defender.stamina = 0
        print(f"{defender.name} stamina: {defender.stamina}")


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
        
    

    def attack(self, attacker, defender, attack_name, fail_chance, min_damage, max_damage, tiredness):
        """generates a random number from 1 to 100, if that number is bigger than the fail chance, damage is dealt to defender"""
        chance = random.randint(0, 100)
        attacker.stamina_lowering(tiredness)

        if chance > fail_chance:
            print(f"\n{attacker.name} used {attack_name}! ")
            damage = random.randint(min_damage, max_damage)
            self.critical_hit(damage)
            defender.health_lowering(self.damage)

            if defender.health < 0:
                defender.health = 0
                self.show_hp(defender)
                self.show_stamina(defender)
            else:
                self.show_hp(defender)
                self.show_stamina(defender)

        else:
            print(f"\n{defender.name} dodged the {attack_name.lower()} attack! ")
            self.show_hp(defender)
            self.show_stamina(defender)

    def get_info(self, game_end = 0, loss = 0, win = 0, punch = 0, kick = 0, body_slam = 0):
        
        path = Path("stats.json")

        if path.exists():
            content = path.read_text()
            my_stats_dict = json.loads(content)
            my_stats_dict["game_over_times"] += game_end
            my_stats_dict["losses"] += loss
            my_stats_dict["wins"] += win
            my_stats_dict["punches"] += punch
            my_stats_dict["kicks"] += kick
            my_stats_dict["body_slams"] += body_slam
            content = json.dumps(my_stats_dict)
            path.write_text(content)
        else:
            my_stats_dict = {}
            game_over_times, losses, wins, punches, kicks, body_slams = 0, 0, 0, 0, 0, 0
            game_over_times += game_end
            losses += loss
            wins += win
            punches += punch
            kicks += kick
            body_slams += body_slam
            my_stats_dict["game_over_times"] = game_over_times
            my_stats_dict["losses"] = losses
            my_stats_dict["wins"] = wins
            my_stats_dict["punches"] = punches
            my_stats_dict["kicks"] = kicks
            my_stats_dict["body_slams"] = body_slams
            content = json.dumps(my_stats_dict)
            path.write_text(content)

    def info_reading(self):
        path = Path("stats.json")
        content = path.read_text()
        my_stats_dict = json.loads(content)
        print(f"\nIn total {my_stats_dict["game_over_times"]} games were played. You won {my_stats_dict["wins"]} of them and lost {my_stats_dict["losses"]} of them.\n")  
        print(f"You punched {my_stats_dict["punches"]} times, kicked {my_stats_dict["kicks"]} times and body slammed {my_stats_dict["body_slams"]} times.")

         

    def punches(self, punch = 0):
        self.attack(my_character, ai_character, "Punch", 20, 10, 20, 25)


    def kicks(self, kick = 0):
        self.attack(my_character, ai_character, "Kick", 50, 25, 35, 30)
    

    def body_slams(self, body_slam = 0):
        self.attack(my_character, ai_character,"Body slam", 75, 45, 65, 35)


    def aipunches(self):
        self.attack(ai_character, my_character, "Punch", 20, 10, 20, 25)

    def aikicks(self):
        self.attack(ai_character, my_character, "Kick", 50, 25, 35, 30)

    def aibody_slams(self):
        self.attack(ai_character, my_character, "Body slam", 75, 45, 65, 35)

def get_name():

    path = Path("character_name.json")

    if path.exists():
        content = path.read_text()
        name = json.loads(content)
        return name
    
    else:
        name = input("Enter your characters nickname: ").title()

        while len(name) > 20:
            name = input("The name can be, at max, 20 characters long. Try again: ")

        content = json.dumps(name)
        path.write_text(content)
        return name
    
def change_name():
    path = Path("character_name.json")
    name = input("Enter your characters nickname: ").title()

    while len(name) > 20:
        name = input("The name can be, at max, 20 characters long. Try again: ")

    content = json.dumps(name)
    path.write_text(content)
    return name

name = get_name()

my_character = Character(name)
ai_character = Character("AI")

is_active = True


def main(is_active):

    punch = 0
    kick = 0
    body_slam = 0

    while is_active == True:

        while ai_character.health > 0 and my_character.health > 0:

            move = input(f"\nPunch, kick or body slam: ").lower()

            if move == "punch":
                ai_character.punches()
                punch = 1
                my_character.get_info(0,0,0,punch,0,0)

            elif move == "kick":
                ai_character.kicks()
                kick = 1
                my_character.get_info(0,0,0,0,kick,0)

            elif move == "body slam":
                ai_character.body_slams()
                body_slam = 1
                my_character.get_info(0,0,0,0,0,body_slam)

            else:
                print(f"\nNot a legal move! {my_character.name} skips a turn! ")
                ai_character.show_hp(ai_character)

            if ai_character.health > 0:
                ai_move = random.randint(1,3)

                if ai_move == 1:
                    my_character.aipunches()

                elif ai_move == 2:
                    my_character.aikicks()

                elif ai_move == 3:
                    my_character.aibody_slams()
            

            if ai_character.health == 0:
                print(f"\n{my_character.name} wins! ")
                my_character.get_info(1, 0, 1, punch, kick, body_slam)
                choice = input("Play again? y/n: ").lower()

                if choice == "y":
                    my_character.health, ai_character.health = 100, 100
                    main(is_active)

                elif choice == "n":
                    starting_screen()

            elif my_character.health == 0:
                print(f"\nAi wins! ")
                my_character.get_info(1, 1, 0)
                choice = input("Play again? y/n: ").lower()

                if choice == "y":
                    my_character.health, ai_character.health = 100, 100
                    main(is_active)

                elif choice == "n":
                    starting_screen()

    else:
        print("Quitting...")
        sys.exit()

def starting_screen():

    commands = {"Start" : "Starts the game", "stats" : "Shows various game statistics", "change name" : "changes character name", "help" : "shows all commands", "quit" : "quits the game"}
    print()
    your_choice = input("Start game / game stats / change name / help / quit: ").lower()
    print()

    if your_choice == "stats" or your_choice == "game stats":
        try:
            my_character.info_reading()
        except FileNotFoundError:
            print("You haven't played yet! ")
        your_choice = input(f"\n")

    if your_choice == "start" or your_choice == "start game":
        my_character.health, ai_character.health = 100, 100
        get_name()
        is_active = True
        main(is_active)

    elif your_choice == "help" or your_choice == "h":
        for key, value in commands.items():
            print(f"{key} : {value}")
        starting_screen()

    elif your_choice == "quit" or your_choice == "q" or your_choice == "exit":
        is_active = False
        main(is_active)

    elif your_choice == "change name" or your_choice == "change":
        name = change_name()
        my_character.name = name
        starting_screen()

    else:
        print("Command was not recognised! ")
        starting_screen()


starting_screen()


   
###needs###
# alot of repetitive code, need to use more functions
# should ask start or stats first, not for character name, but i need the character name to create a character instance and use stats function
# start or stats need prettier formating


###bugs###

# Ai can attack after it's health drops down to zero on the same turn (fixed)
# when choosing 'n' to end the game, for some reason it ends only when there is a print line after the 'return is_active' line(fixed, n takes you to the starting screen)

###features###
##By importance, starting from the top##

# Critical hits(DONE)
# Show damage dealt as -##(DONE)
# Instead of attack failing, should be enemy dodged attack(DONE)
# When choosing move, show attack success rate percentage and possible damage dealt
# Play again, save name, should be able to change name(DONE)
# Dynamic dashes (----) highlighting hp(maybe better formating)(DONE)
# Dynamic stamina system, attacks drain stamina, can be recharged by skipping turn
# Lithuanian language, input change_language or smth to change language
# Healing (limited use, maybe potion?)
# Store data about fight, like moves commited, in a file(DONE, although failed moves also are stored[FIX])

###Swords and sandals ugly copy LOL






