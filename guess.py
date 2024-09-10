word_list = ["ardvark","baboon","camel"]
import random
word = random.choice(word_list)
print(f'Pssst,the solution is {word}.')
display = []
the_length = len(word)
for _ in range(the_length):
    display += "-"
print(display)

guess = input("Guess a letter: ").lower()
for position in range(len(word)):
    letter = word[position]
    if letter == guess:
        display[position] = letter
print(display)        
        