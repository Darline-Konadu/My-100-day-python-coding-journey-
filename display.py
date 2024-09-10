import random
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
print(f'Pssst, the solution is {word}.')
display = []
the_length = len(word)
for _ in range(the_length):
    display += "_"
game_ends = False

while not game_ends:
    guess = input("Guess a letter: ").lower()
    for position in range(the_length):
        letter = word[position]
        print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        game_ends = True
        print("You win.")

