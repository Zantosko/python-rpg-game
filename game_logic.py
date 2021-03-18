class Hero:
    def __init__(self, hp, strength, defense):
        self.hp = hp
        self.strength = strength
        self.defense = defense

    def take_damage(self):
        self.hp -= 25

    def take_low_damage(self):
        self.hp -= 15

    def take_critical_damage(self):
        self.hp -= 50


class Goblin:
    def __init__(self):
        self.hp = 100
        self.strength = 20
        self.defense = 15

    def take_damage(self):
        self.hp -= 25
        print(
            f"You inflicted 25 damage to the goblin, his health is now {self.hp}")


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


def start_game():
    greeting()

    hero = Hero(200, 15, 10)
    goblin = Goblin()

    while hero.hp > 0 or goblin.hp > 0:
        choice = int(input(
            "What will you do (1)Attack, (2)Defend, (3)Do Nothing? > "))

        if choice == 1:
            goblin.take_damage()
            if goblin.hp == 0:
                print("Victory is yours!")
                end_game()
        elif choice == 2:
            hero.take_low_damage()
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


start_game()
