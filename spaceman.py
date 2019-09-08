import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    matching_letters = "".join([i for i in secret_word if i in letters_guessed])
    if matching_letters == secret_word:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = [i if i in letters_guessed else "_" for i in secret_word]
    
    return "".join(guessed_word)



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    return guess in secret_word



def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    print("Hello and welcome to Spaceman! Here's how the game works:")
    print("You are given a number of blanks representing a secret word. You can guess any letter. ")
    print("If the letter you guess is in the secret word, the spot where that letter is will be filled in.")
    print("If you can guess all the letters, you win!")
    
    letters_guessed = []
    num_incorrect_guesses = 0

    while True:
        letter = input("Guess a letter: ")
        
        if len(letter) != 1:
            print("You must enter exactly one character as a guess")
            continue
        
        if letter in letters_guessed:
            print("You already guessed {}!".format(letter))
            continue
        
        letters_guessed.append(letter)

        if is_guess_in_word(letter, secret_word):
            print("Guess was in secret word!")
        else:
            print("Guess was not in secret word")
            num_incorrect_guesses += 1
            print("You are on guess {} out of {} max guesses".format(num_incorrect_guesses, len(secret_word)))

        if num_incorrect_guesses > len(secret_word):
            print("You lost")
            print("Secret word was: ", secret_word)
            break

        print("Guessed word so far: ", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print("You won!")
            break
        
        print()


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)