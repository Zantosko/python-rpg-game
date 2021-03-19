class Hero:
    def __init__(self):
        self.hp = 100
        self.strength = 15
        self.defense = 10

    def take_damage(self):
        self.hp -= 20
        print(
            f"The goblin attacks and inflicts 20 damage on you, your health is now {self.hp}")

    def take_critical_damage(self):
        self.hp -= 50
        print(
            f"The goblin attacks and inflicts 50 damage on you, your health is now {self.hp}")


class Goblin:
    def __init__(self):
        self.hp = 100
        self.strength = 20
        self.defense = 15

    def take_damage(self):
        self.hp -= 25
        print(
            f"You inflicted 25 damage to the goblin, his health is now {self.hp}")


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
      / || \
        ||
        ||
        ||
        ||
        ||
        ||""")
        choice = int(input(
            f"Please select your weapon (1){self.weapons[0]}, (2){self.weapons[1]}, (3){self.weapons[2]} > "))

        if choice == 1:
            return print(f"You have selected the {self.weapons[0]}")
        elif choice == 2:
            return print(f"You have selected the {self.weapons[1]}")
        elif choice == 3:
            return print(f"You have selected the {self.weapons[2]}")
        else:
            print("That is not a choice!! Please try again")

        while choice > 3:

            choice = int(input(
                f"Please select your weapon (1){self.weapons[0]}, (2){self.weapons[1]}, (3){self.weapons[2]} > "))

            if choice == 1:
                return print(f"You have selected the {self.weapons[0]}")
            elif choice == 2:
                return print(f"You have selected the {self.weapons[1]}")
            elif choice == 3:
                return print(f"You have selected the {self.weapons[2]}")
            else:
                print("That is not a choice!! Please try again")


def greeting():
    message = """WELCOME TO THE PYTHON ADVENTURE GAME!!
CAN YOU DEFEAT THE EVIL GOBLIN AND PROTECT YOUR CASTLE??
     ^       /\             /\   ~!~
        ^   (())           (())
 ^         /(())\         /(())\      ~!~
          (((())))       (((())))
          |^|^^|^|_______|^|^^|^|
      /\   |^^^^|-_-_-_-_-|^^^^|   /\
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


def end_game():
    exit(0)


def game_over():
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


def part_two():
    print("You have now reached part 2 of the game")
    print("You've now entered a dungeon")
    print("""
     _________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \
  |                            _-  _--                      |
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |
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
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \


""")
    print("You're suddenly attacked by a demon!!! What do you do?")
    end_game()


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
         ( :  { _)  '---  $\
    ______'___//__\   ____, \
     )           ( \_/ _____\_
   .'             \   \------''.
   |='           '=|  |         )
   |               |  |  .    _/
    \    (. ) ,   /  /__I_____\
     '._/_)_(\__.'   (__,(__,_]
    @---()_.'---@  """)
    choice = int(input(
        "Please make selction (1)Red Potion, (2)Blue Potion, (3)Green Potion, (4)Exit Shop > "))

    if choice == 1:
        print("You have selcted the red potion")
    elif choice == 2:
        print("You have selcted the blue potion")
    elif choice == 3:
        print("You have selcted the green potion")
    elif choice == 4:
        print("Thank you come again!")
        main_menu()
    else:
        print("Invalid choice please try again")

    while choice != range(1, 5):
        choice = int(input(
            "Please make selction (1)Red Potion, (2)Blue Potion, (3)Green Potion, (4)Exit Shop > "))

        if choice == 1:
            print("You have selcted the red potion")
        elif choice == 2:
            print("You have selcted the blue potion")
        elif choice == 3:
            print("You have selcted the green potion")
        elif choice == 4:
            print("Thank you come again!")
            main_menu()
        else:
            print("Invalid choice please try again")


def start_game():
    greeting()

    hero = Hero()
    goblin = Goblin()

    last_chance = int(
        input("This is your last chance to back out, will you proceed (1)Yes, (2)No > "))
    if last_chance == 1:
        player_weapon = Weapon()
        player_weapon.player_weapon()
    elif last_chance == 2:
        end_game()
    else:
        print("Those were your only two options")
        main_menu()

    while hero.hp > 0 or goblin.hp > 0:
        choice = int(input(
            "What will you do (1)Attack, (2)Defend, (3)Do Nothing? > "))

        if choice == 1:
            goblin.take_damage()
            if goblin.hp == 0:
                print("Victory is yours!")
                part_two()
        elif choice == 2:
            hero.take_damage()
            if hero.hp == 0:
                print("Game over!")
                game_over()
        elif choice == 3:
            hero.take_critical_damage()
            if hero.hp == 0:
                print("Game Over!")
                game_over()
        else:
            print("That's not a choice!! Let's try again.")


def main_menu():
    message = """PYTHON ADVENTURE GAME
Main Menu"""
    print(message)

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


main_menu()
