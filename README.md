# PYTHON RPG GAME

## Description

<img src="/img/Game_Screenshot.png" align="center">

- This is a decision based terminal game where the choices made by the user impact the outcome of the game.

- Every section of the game will prompt the user with a choice. A user can make a coice by entering a number and pressing enter.

- Each choice will will have a number in parenthesis(ex: (1)Attack), this means that the user needs to press that number and then press enter to invoke that action.

- If a letter or invalid number is entered the game will either return an error or prompt you to try again.

## Key Features

- **Access Inventory Feature** - During a battle sequence the player has the opition to access their inventory. Accessing their inventory allows the player to use potions that they purchased from the potion shop at the start of the game. When potions are purchased the selected potion is appended to an empty list (hero's inventory). The inventory can then be accessed by invoking two special methods that iterate over the inventory. The first method organizes the inventory while the second method searches the inventory based on the player's selection to access and then remove the selected potion.

- **Interactive Weapons Feature** - When the player starts the game they'll reach a certain point where they are prompted to select a weapon (shield, sword, staff). Once a weapon is selected, depending on the player's choice it will call the specific instance of the weapon that they selected. The specific weapon classes inherit from the hero class and utilize the `super()` method to overide class with the weapon's durability stat, while at the same time maintaining the hero's base stats. This also allows for the hero's attack and defense stats to be altered in correlation to the selected weapon.

## What was learned

- Programming fundamentals and how to implement them based on the situation.

  - Variables
  - Functions
  - While loops and For loops
  - if, elif, else statements

- Object Oriented Programming(OOP)

  - Utilizing classes
  - Class inheritance
  - Manipulating sub classes and their parent classes
  - How to use the super() method

- Gained a better understanding of Git and GitHub

  - Working with a team and utilizing separate branches to develop distinct features for the game.
  - Devloped a better understanding of how to handle merge conflicts.
  - Understanding the importance of feature branches and how it's bad practice to work off of the main branch.
