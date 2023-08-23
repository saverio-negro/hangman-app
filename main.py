import os
import random
import words
import arts

def is_linux():
    return os.name == "posix"

def clear():
    os.system("clear") if is_linux() else os.system("cls")

def display_chosen_word(chosen_word):
    display = []
    for letter in chosen_word:
        if letter != " ":
            display.append("_")
        else:
            display.append(" ")
    return display

def play_hangman():
    
    stages = arts.stages
    words_list = words.words_list
    lives = 6
    chosen_word = words_list[random.randint(0, len(words_list) - 1)]
    display = display_chosen_word(chosen_word)
    end_of_game = False
    is_correct = False
    guessed_letters = []
    
    print(arts.logo)
    print("Welcome to the Hangman Game!\n")
    print(" ".join(display))
    print(stages[lives])
    
    while not end_of_game:
        guess = input("Make a guess by chosing a letter: ").lower()
        clear()
        
        for index in range(len(chosen_word)):
            letter = chosen_word[index]
            
            if letter == guess:
                display[index] = guess
                is_correct = True
    
        if not is_correct:
            if guess in guessed_letters:
                print(f'The letter {guess} has already been guessed. Try guessing another letter.')
                print(" ".join(display))
                print(stages[lives])
            else:
                guessed_letters.append(guess)
                lives -= 1
                print(" ".join(display))
                print(stages[lives])
                print(f'You guessed "{guess}", that\'s not in the word. You lose a life.')
        else:
            is_correct = False
            if guess in guessed_letters:
                print(f'The letter "{guess}" has already been guessed. Try guessing another letter.')
                print(" ".join(display))
                print(stages[lives])
            else:
                guessed_letters.append(guess)
                print(" ".join(display))
                print(stages[lives])
        
        if "_" not in display:
            end_of_game = True
            print("You win! 😎\n")
        elif lives == 0:
            end_of_game = True
            print(f"You lose. The word to guess was: {chosen_word}. 😭\n")
    
    keep_playing = input("Do you want to play another Hangman game? Type 'y', or 'n': ")    

    if keep_playing == "y":
        clear()
        play_hangman()
    else:
        print("Bye bye!")

play_hangman()