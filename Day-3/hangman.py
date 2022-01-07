import random

word_list = ["ardvark", "baboon", "camel"]

## randomly choose a word from word_list and assign to variable choosen word
choosen_word = random.choice(word_list)
print(choosen_word)

display = []

for letter in choosen_word:
    display.append("_")
print(display)

end_game = False
## ask the user to guess a letter and assign answer to variable called, and make guess to lowercase
while not end_game:
    guess = input(("Enter your guess: ")).lower()

## checking if the guessed letter of user is present in the choosen word and replace it with letter in the position

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_game = True
        print("you win")




