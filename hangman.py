import random
stages = ['''
  | .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .

''']

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
lives = 6
print(f'Pssst, the solution is {word}.')

display = []
for _ in range(len(word)):
    display.append("_")

game_ends = False

while not game_ends:
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives remaining: {lives}")
        if lives == 0:
            game_ends = True
            print("You lose.")

    print(' '.join(display))

    if "_" not in display:
        game_ends = True
        print("You win.")
print(stages[lives])        