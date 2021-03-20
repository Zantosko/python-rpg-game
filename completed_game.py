class Hero:
    def __init__(self):
        self.hp = 100
        self.strength = 15
        self.defense = 10
        self.money = 100
        self.weapon = None

    def take_damage(self):
        self.hp -= 20
        if self.hp <= 0:
            print("The dragon has defeated you")
        else:
            print(
                f"The dragon attacks and inflicts 20 damage on you, your health is now {self.hp}")

    def take_critical_damage(self):
        self.hp -= 50
        if self.hp <= 0:
            print("The dragon has defeated you")
        else:
            print(
                f"The dragon attacks and inflicts 50 damage on you, your health is now {self.hp}")

    def take_damage_demon(self):
        self.hp -= 35
        if self.hp <= 0:
            print("The demon has defeated you")
        else:
            print(
                f"The demon attacks and inflicts 35 damage on you, your health is now {self.hp}")

    def take_critical_damage_demon(self):
        self.hp -= 70
        if self.hp <= 0:
            print("The demon has defeated you")
        else:
            print(
                f"The demon attacks and inflicts 70 damage on you, your health is now {self.hp}")

    inventory = []

    def current_inventory(self):
        print(f"Your current inventory is now {self.inventory}")

    def spend_money(self, potion_type):
        if potion_type == "Red":
            self.money -= 20
            print(f"You currently have {self.money} money")
            hero.inventory.append("Red Potion")
            hero.current_inventory()
        elif potion_type == "Blue":
            self.money -= 30
            print(f"You currently have {self.money} money")
            hero.inventory.append("Blue Potion")
            hero.current_inventory()
        elif potion_type == "Green":
            self.money -= 40
            print(f"You currently have {self.money} money")
            hero.inventory.append("Green Potion")
            hero.current_inventory()

    def use_item(self):
        print("Here is your current inventory: ")
        count = 1
        for item in hero.inventory:
            print(f"{count} : {item}")
            count += 1

        choice = int(input("Will you use an item? (1)Yes (2)No > "))
        if choice == 1:
            hero.potion_select()
        else:
            return

    def potion_select(self):
        item_to_use = int(input("What item will you use? > "))

        if item_to_use <= 0 or item_to_use > len(hero.inventory):
            print("That item does not exist! Please select actual item!")
        else:
            for item in hero.inventory:
                item = item_to_use - 1
                if hero.inventory[item] == "Red Potion":
                    print("You used the red potion")
                    print("Your HP has increased by 20 points")
                    hero.hp += 20
                    print(f"Your current HP in now: {hero.hp}")
                    return hero.inventory.pop(item)
                elif hero.inventory[item] == "Blue Potion":
                    print("You used the blue potion")
                    print("Your HP has increased by 40 points")
                    hero.hp += 40
                    print(f"Your current HP in now: {hero.hp}")
                    return hero.inventory.pop(item)
                elif hero.inventory[item] == "Green Potion":
                    print("You used the green potion")
                    print("Your HP has increased by 60 points")
                    hero.hp += 60
                    print(f"Your current HP in now: {hero.hp}")
                    return hero.inventory.pop(item)


class Demon:
    def __init__(self):
        self.hp = 100
        self.strength = 20
        self.defense = 15

    def take_damage(self):
        self.hp -= 25
        if self.hp <= 0:
            print("YOU DID IT!! YOU DEFEATED THE DEMON AND SAVED YOU KINGODOM!!")
        else:
            print(
                f"You inflicted 25 damage to the demon, its health is now {self.hp}")


class Dragon:
    def __init__(self):
        self.hp = 100
        self.magic = 1000

    def take_damage(self):
        self.hp -= 25
        print(
            f"""You dealt 25 damage to the dragon, its health is now {self.hp}.""")


class Weapon:
    weapons = ["shield", "sword", "staff"]

    def player_weapon(self):
        print("""
           |`-._/\_.-`|
           |    ||    |
           |___o()o___|
           |__((<>))__|
           \   o\/o   /
            \   ||   /
             \  ||  /
              '.||.'
                ``

            /| ________________
        O|===|* >________________>
            \|

               .||,
              \.`',/
              = ,. =
                ||
                ||
                ||
                ||
                ||
                ||
        """)

        print(
            f"Your current stats are: {hero.strength} Strength, {hero.defense} Defense, {hero.hp} HP")

        choice = 0

        while choice != range(1, 4):
            choice = int(input(
                f"Please select your weapon (1){self.weapons[0]}, (2){self.weapons[1]}, (3){self.weapons[2]} > "))

            if choice == 1:
                print(f"You have selected the {self.weapons[0]}")
                shield.attributes()
                hero.weapon = shield
                return
            elif choice == 2:
                print(f"You have selected the {self.weapons[1]}")
                sword.attributes()
                hero.weapon = sword
                return
            elif choice == 3:
                print(f"You have selected the {self.weapons[2]}")
                staff.attributes()
                hero.weapon = staff
                return
            else:
                print("That is not a choice!! Please try again")

    def attack_handling(self):
        if hero.weapon == shield:
            return shield.attack()
        elif hero.weapon == sword:
            return sword.attack()
        elif hero.weapon == staff:
            return staff.attack()

    def defense_handling(self):
        if hero.weapon == shield:
            return shield.defend()
        elif hero.weapon == sword:
            return sword.defend()
        elif hero.weapon == staff:
            return staff.defend()


class Shield(Hero):
    def __init__(self):
        self.durability = 100
        super().__init__()

    def attributes(self):
        self.defense += 20
        print(f"Your defense has increased by 20 and is now {self.defense}")

    def attack(self):
        self.damage = 8
        self.durability -= 5
        if sword.durability <= 0:
            sword.constitution()
        else:
            print(
                f"Your sheild durability has decreased by 5 is now {self.durability}")

    def defend(self):
        self.durability -= 0
        if self.durability <= 0:
            self.constitution()
        else:
            print(
                f"Your shield durability has remains the same {self.durability}")

    def constitution(self):
        print("Your shield has broken")


class Sword(Hero):
    def __init__(self):
        self.durability = 70
        self.damage = 18
        super().__init__()

    def attributes(self):
        self.strength += 20
        print(
            f"Your strength has increased by 20 points, your strength is now {self.strength}")
        self.defense += 10
        print(
            f"Your defense has increased by 10 points, your defense is now {self.defense}")

    def attack(self):
        self.damage = 18
        self.durability -= 1
        if sword.durability <= 0:
            sword.constitution()
        else:
            print(
                f"Your sword durability has decreased by 1 is now {self.durability}")

    def defend(self):
        self.durability -= 2
        if self.durability <= 0:
            self.constitution()
        else:
            print(
                f"Your sword durability has decreased by 2 and is now {self.durability}")

    def constitution(self):
        print("Your sword has broken")


class Staff(Hero):
    def __init__(self):
        self.durability = 85
        self.damage = 12
        super().__init__()

    def attributes(self):
        self.strength += 10
        print(
            f"Your strength has increased by 10 points, your strength is now {self.strength}")
        self.defense += 5
        print(
            f"Your defense has increased by 5 points, your defense is now {self.defense}")

    def attack(self):
        self.damage = 12
        self.durability -= 1
        if staff.durability <= 0:
            staff.constitution()
        else:
            print(
                f"Your staff durability has decreased by 1 and is now {self.durability}")

    def defend(self):
        self.durability -= 1
        if self.durability <= 0:
            self.constitution()
        else:
            print(
                f"Your staff durability has decreased by 5 and is now {self.durability}")

    def constitution(self):
        print("Your staff has broken")


# Creating instances of characters and weapons for first part of the game
hero = Hero()
player_weapon = Weapon()
shield = Shield()
sword = Sword()
staff = Staff()
dragon = Dragon()


# End game sequence
def end_game():
    exit(0)


# Game over sequence
def game_over():
    print("Game Over!")
    print("""
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@""")
    exit(0)


# Part 2 Sequence


def part_two():
    demon = Demon()

    print("\nYou have now reached part 2 of the game")
    print("You now find yourself inside a mysterious dungeon")
    print("""
     _________________________________________________________
 / | -_ - _ - |
/ |_-_ - _ - _ - _ - - |
  |                            _ - _-- |
  |,                            |
  |     .-'````````'.        '(`         .-'```````'- . |
  |    .` | `.      `)'     .` | `. |
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -
/   -_- _ -             _- _---                       -_-  -_
""")
    print("\nYou're suddenly attacked by a demon!!! What do you do?")

    while hero.hp > 0 or demon.hp > 0:
        choice = int(input(
            "What will you do (1)Attack, (2)Defend, (3)Do Nothing (4)view inventory? > "))

        if choice == 1:
            demon.take_damage()
            player_weapon.attack_handling()
            if demon.hp <= 0:
                print("CONGRATS!! YOU JUST BEAT THE PYTHON ADVENTURE GAME!!")
                print(
                    "You now return to your kingdom, patiently waiting for the next call to action.")
                end_game()
        elif choice == 2:
            hero.take_damage_demon()
            player_weapon.defense_handling()
            if hero.hp <= 0:
                game_over()
        elif choice == 3:
            hero.take_critical_damage_demon()
            if hero.hp <= 0:
                game_over()
        elif choice == 4:
            hero.use_item()
        else:
            print("That's not a choice!! Let's try again.")

    end_game()


# The transition scene between part 1 and part 2 of the game
def transition_phase():
    print("\nSomething seems off, you notice a weird aura in the sky")
    print("""  ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
      ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
         .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
             .`            | |  |  : .:|       ` | || | : |: |          | ||
      '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
         .                 .    ` *|  || :       `    | | :| | :      |:| |
 .                .          .        || |.: *          | || : :     :|||
        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
     .             *              .     +:`|!             . ||||  :.||`
 +                      .                ..!|*          . | :`||+ |||`
     .                         +      : |||`        .| :| | | |.| ||`     .
       *     +   '               +  :|| |`     :.+. || || | |:`|| `
                            .      .||` .    ..|| | |: '` `| | |`  +
  .       +++                      ||        !|!: `       :| |
              +         .      .    | .      `|||.:      .||    .      .    `
          '                           `|.   .  `:|||   + ||'     `
  __    +      *                         `'       `'|.    `:""")
    choice = int(input("Do you follow it to the source? (1)Yes (2)No > "))
    if choice == 1:
        part_two()
    elif choice == 2:
        print("The aura eventually envelops your kingdom and you disappear into darkness")
        game_over()
    else:
        print("I'm assuming you meant to put yes, please proceed")
        part_two()


# Potion Shop


def potion_shop():
    print("You've now entered the potion shop")
    print("""
    (       "     )
  ( _  *         WHAT KIND OF POTION WOULD YOU LIKE?
     * (     /      \    ___
        "     "        _/ /
       (   *  )    ___/   |
         )   "     _ o)'-./__
        *  _ )    (_, . $$$
        (  )   __ __ 7_ $$$$
         ( :  { _)  '---  $
    ______'___//__\   ____,|
     )           ( \_/ _____\_
   .'             \   \------''.
   |='           '=|  |         )
   |               |  |  .    _/
    \    (. ) ,   /  /__I_____|
     '._/_)_(\__.'   (__,(__,_]
    @---()_.'---@  """)

    print(f"You currently have {hero.money} money")
    choice = 0

    while choice != range(1, 5):
        choice = int(input(
            "Please make selection (1)Red Potion - 20 money, (2)Blue Potion - 30 money, (3)Green Potion - 40 money, (4)Exit Shop > "))

        if choice == 1:
            if hero.money < 20:
                print("You don't have enough money!")
            else:
                print("You have selected the red potion")
                hero.spend_money("Red")
        elif choice == 2:
            if hero.money < 30:
                print("You don't have enough money!")
            else:
                print("You have selected the blue potion")
                hero.spend_money("Blue")
        elif choice == 3:
            if hero.money < 40:
                print("You don't have enough money!")
            else:
                print("You have selected the green potion")
                hero.spend_money("Green")
        elif choice == 4:
            print("Thank you come again!")
            main_menu()
        else:
            print("Invalid choice please try again")


# Part 1 sequence


def start_game():
    greeting()

    last_chance = int(
        input("This is your last chance to back out, will you proceed (1)Yes, (2)No > "))
    if last_chance == 1:
        player_weapon.player_weapon()
    elif last_chance == 2:
        print("You have taken the coward's way out! Goodbye!")
        end_game()
    else:
        print("Those were your only two options")
        main_menu()

    print("\nYou look in sky and see a dragon approaching the castle!!")

    while hero.hp > 0 or dragon.hp > 0:
        choice = int(input(
            "What will you do (1)Attack, (2)Defend, (3)Do Nothing (4)view inventory? > "))

        if choice == 1:
            dragon.take_damage()
            player_weapon.attack_handling()
            if dragon.hp == 0:
                print("Victory is yours!")
                transition_phase()
        elif choice == 2:
            hero.take_damage()
            player_weapon.defense_handling()
            if hero.hp <= 0:
                game_over()
        elif choice == 3:
            hero.take_critical_damage()
            if hero.hp <= 0:
                game_over()
        elif choice == 4:
            hero.use_item()
        else:
            print("That's not a choice!! Let's try again.")


# Greeting scene before part 1 sequence

def greeting():
    message = """WELCOME TO THE PYTHON ADVENTURE GAME!!
     ^       /\             /\   ~!~
        ^   (())           (())
 ^         /(())\         /(())\      ~!~
          (((())))       (((())))
          |^|^^|^|_______|^|^^|^|
      |    |^^^^|-_-_-_-_-|^^^^|   |
     (())  | "" |+_+_+_+_+| "" |  (())
    ((())) |    |[X]_+_[X]|    | ((()))
   (((())))|    |+_+_+_+_+|    |(((())))
   |^|^^|^||____|-_-_-_-_-|____||^|^^|^|
    |^^^^|_-_-_-_-_-_-_-_-_-_-_-_|^^^^|
~^~~| "" |_-_-_-_-_-_-_-_-_-_-_-_| "" |~~
~~  |    |_+_+_+_+_+_+_+_+_+_+_+_|    | ~^~
 ~^^|    |_+[X]+_[X]_+_[X]_+[X]+_|    |~~^
    |    |_+_+_+_+_+/l\+_+_+_+_+_|    |
    |    |_-_-_-_-_|:::|_-_-_-_-_|    |
    |____|_+_+_+_+_|:::|_+_+_+_+_|____|"""

    print(message)


# Main menu


def main_menu():
    message = "PYTHON ADVENTURE GAME \nMain Menu\n"
    print(message)

    print("Once you start the game there is no going back! If you need potions now is the time to buy them!\n")

    choice = int(input(
        "Choose you path brave hero (1)Start Game, (2)Potion Shop, (3)Quit Game > "))

    if choice == 1:
        start_game()
    elif choice == 2:
        potion_shop()
    elif choice == 3:
        print("Why are you leaving?? Your adventure hasn't even started yet!!")
        end_game()
    else:
        print("Since you can't follow directions, you're being thrown into the game!")
        start_game()


# Invokes main menu function to start the game
main_menu()
