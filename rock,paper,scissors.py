import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
player_choice = input("Choose rock, paper or scissors: ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])
if player_choice == "rock":
    print("You chose Rock:")
    print(rock)
elif player_choice == "paper":
    print("You chose Paper:")
    print(paper)
elif player_choice == "scissors":
    print("You chose Scissors:")
    print(scissors)
else:
    print("Invalid choice, you lose!")
    exit()
print("Computer chose:")
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
elif computer_choice == "scissors":
    print(scissors)
if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins!")