print(r'''






                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`


''')



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
    # Continue in the game.
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    
    if choice2 == "wait":
        # Game will continue
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ").lower()
        
        if choice3 == "red":
            print("You fell into a hole. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You got attacked by a lion. Game over.")
        else:
            print("You chose a door that does not exist. Game over.")
    
    else:
        print("You got attacked by a sea monster. Game over.")
else:
    print("You fell into a pit. Game over.")