#Step 1 
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6

##TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

#TODO-4 - Create a "placeholder" with the same number of blanks as a chosen word
Placeholder = ["_"] * len(chosen_word)
# for letter in chosen_word:
#     Placeholder = Placeholder + "_"

#print(Placeholder)
print(" ".join(Placeholder))

#TODO-6 - Use a while loop to let the user guess again
game = True

while game:
    print(f"*********Your current lives {lives} / 6 *********")
    guess = input("Can you guess a letter for the game? ").lower()

    if guess in Placeholder:
        print(f"You have already guessed the letter {guess}")

    # Check if the guessed letter is in the chosen word
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            Placeholder[index] = guess
                
        
    if guess in chosen_word:
        lives = lives
    elif guess not in chosen_word:
        lives = lives -1
        print(f"The guessed letter {guess} is not in the word. You loose life")

    
    
    # Convert guessed_letters back to a string to display the current state of the word
    current_display = " ".join(Placeholder)
    print(current_display)

    # Check if the user has guessed the word correctly
    if "_" not in Placeholder:
        print("You won!**** Whoaaaa")
        game = False
        
    if lives == 0:
        print(f"****You Loose****. The choosen word is {chosen_word}**")
        game = False
        
    
    print(hangman_art.stages[lives])

# while game == True:
    # guess = input("Can you guess a letter for the game?").lower()
#     Display = ""
#     if "_" not in Display:
#         game = False





# for letter in chosen_word:
#     if letter == guess:
#         Display = Display + letter
#     else:
#         Display = Display + "_"

# Display_latest = Display
        
# print(Display_latest)