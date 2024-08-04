import random, json, sys
from pathlib import Path

class Character:

    def __init__(self, name):

        self.name = name
        if self.name == "":
            self.name = "nameless"
        self.health = 100
        self.stamina = 100


    def health_lowering(self, damage) -> None:
        """lowers the defenders health by damage dealt"""

        self.health -= damage

    def show_hp(self, defender) -> None:
        """shows the defenders health and a dynamic health bar"""

        lines = round(defender.health * 0.4)
        print(f"|{lines * "="}|")
        print(f"{defender.name} health: {defender.health} hp")

    def stamina_lowering(self, tiredness) -> None:
        self.stamina -= tiredness

    def show_stamina(self, defender) -> None:
        if defender.stamina < 0:
            defender.stamina = 0
        print(f"{defender.name} stamina: {defender.stamina}")


    def critical_hit(self, damage) -> int:
        """small chance for critical hit, which increases damage dealt 1.5 times"""

        self.damage = damage
        critical_chance = random.randint(1, 100)

        if critical_chance > 85:
            self.damage = round(self.damage * 1.5)
            print(f"Critical hit! -{self.damage} hp")
        else:
            print(f"-{self.damage} hp")

        return self.damage
    
    def restore_everything(self) -> None:
        my_character.health, ai_character.health = 100, 100 
        my_character.stamina, ai_character.stamina = 100, 100
        

    def attack(self, attacker, defender, attack_name, fail_chance, min_damage, max_damage, tiredness) -> None:
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


    def punches(self) -> None:
        """puch attack on the ai"""

        self.attack(my_character, ai_character, "Punch", 20, 10, 20, 25)

    def kicks(self) -> None:
        """kick attack on the ai"""

        self.attack(my_character, ai_character, "Kick", 50, 25, 35, 30)
    
    def body_slams(self) -> None:
        """body slam attack on the ai"""
        self.attack(my_character, ai_character,"Body slam", 75, 45, 65, 35)


    def aipunches(self) -> None:
        """punch attack on player"""

        self.attack(ai_character, my_character, "Punch", 20, 10, 20, 25)

    def aikicks(self) -> None:
        """kick attack on player"""

        self.attack(ai_character, my_character, "Kick", 50, 25, 35, 30)

    def aibody_slams(self) -> None:
        """body slam attack on player"""

        self.attack(ai_character, my_character, "Body slam", 75, 45, 65, 35)

stats_path = Path("stats.json")

def get_info(total_games = 0, loss = 0, win = 0, punch = 0, kick = 0, body_slam = 0) -> None:
    """stores info about game"""    

    if stats_path.exists():
        content = stats_path.read_text()
        my_stats_dict = json.loads(content)
        my_stats_dict["total_games"] += total_games
        my_stats_dict["losses"] += loss
        my_stats_dict["wins"] += win
        my_stats_dict["punches"] += punch
        my_stats_dict["kicks"] += kick
        my_stats_dict["body_slams"] += body_slam
        content = json.dumps(my_stats_dict)
        stats_path.write_text(content)
    else:                                                       # what an ugly piece of code
        my_stats_dict = {}
        my_stats_dict["total_games"] = total_games
        my_stats_dict["losses"] = loss
        my_stats_dict["wins"] = win
        my_stats_dict["punches"] = punch
        my_stats_dict["kicks"] = kick
        my_stats_dict["body_slams"] = body_slam
        content = json.dumps(my_stats_dict)
        stats_path.write_text(content)


def info_reading() -> None:
    """gets info about previous games"""

    content = stats_path.read_text()
    my_stats_dict = json.loads(content)
    print(f"\nin total {my_stats_dict["total_games"]} games were played. you won {my_stats_dict["wins"]} of them and lost {my_stats_dict["losses"]} of them.\n")  
    print(f"You punched {my_stats_dict["punches"]} times, kicked {my_stats_dict["kicks"]} times and body slammed {my_stats_dict["body_slams"]} times.")

name_path = Path("character_name.json")

def get_name() -> str:
    """gets the characters name if it exists"""

    if name_path.exists():
        content = name_path.read_text()
        name = json.loads(content)
        return name
    
    else:
        change_name()
    
def change_name() -> str:
    """changes the characters name"""

    name = input("Enter your characters nickname: ").title()

    while len(name) > 20:
        name = input("The name can be, at max, 20 characters long. Try again: ")

    content = json.dumps(name)
    name_path.write_text(content)
    return name

name = get_name()

my_character = Character(name)
ai_character = Character("AI")


def fighting_logic(is_active):

    punch, kick, body_slam = 0, 0, 0       # this is done to track stats

    while is_active == True:

        while ai_character.health > 0 and my_character.health > 0:
            if my_character.stamina == 0:
                print(f"\nResting...")
                my_character.stamina += 50

            else:
                move = input(f"\nPunch:80% | Kick:50% | Body slam:25%  ").lower()

                if move == "punch":
                    ai_character.punches()
                    punch += 1

                elif move == "kick":
                    ai_character.kicks()
                    kick += 1

                elif move == "body slam":
                    ai_character.body_slams()
                    body_slam += 1

                else:
                    print(f"\nNot a legal move! {my_character.name} skips a turn! ")
                    ai_character.show_hp(ai_character)


            if ai_character.health > 0:
                if ai_character.stamina == 0:
                    print(f"\nAi rests...")
                    ai_character.stamina += 50

                else:
                    ai_move = random.randint(1,3)

                    if ai_move == 1:
                        my_character.aipunches()

                    elif ai_move == 2:
                        my_character.aikicks()
                        
                    elif ai_move == 3:
                        my_character.aibody_slams()
                

            if ai_character.health == 0:
                print(f"\n{my_character.name} wins! ")
                get_info(1, 0, 1, punch, kick, body_slam)
                choice = input("Play again? y/n: ").lower()

                if choice == "y":
                    my_character.restore_everything()
                    fighting_logic(True)

                elif choice == "n":
                    main()

            elif my_character.health == 0:
                print(f"\nAi wins! ")
                get_info(1, 1, 0, punch, kick, body_slam)
                choice = input("Play again? y/n: ").lower()

                if choice == "y":
                    my_character.restore_everything()
                    fighting_logic(True)

                elif choice == "n":
                    main()


def main():
    """acts as a menu"""

    commands = {"Start" : "Starts the game",
                "stats" : "Shows various game statistics",
                "change name" : "changes character name", 
                "help" : "shows all commands",
                "quit" : "quits the game"}
    
    while True:
        your_choice = input(f"\nStart game / Game stats / Change name / Help / Quit: \n").lower()

        if your_choice == "start" or your_choice == "start game":
            get_name()
            fighting_logic(True)

        elif your_choice == "stats" or your_choice == "game stats":
            try:
                info_reading()
            except FileNotFoundError:
                print("You haven't played yet! ")

        elif your_choice == "change name" or your_choice == "change":
            name = change_name()
            my_character.name = name

        elif your_choice == "help" or your_choice == "h":
            for key, value in commands.items():
                print(f"{key.title()} : {value.title()}")

        elif your_choice == "quit" or your_choice == "q" or your_choice == "exit":
            print("Quitting...")
            sys.exit()

        else:
            print("Command was not recognised! ")

if __name__ == "__main__":
    main()