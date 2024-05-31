import random

# List of words for the game
word_list = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "pineapple"]

def choose_word():
    # Choose a random word from the word list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    # Choose a word
    word = choose_word()
    # Initialize guessed letters
    guessed_letters = []
    # Initialize number of tries
    tries = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while tries > 0:
        # Get user input for a letter guess
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in word:
            tries -= 1
            print("Incorrect guess!")
            print(f"Tries left: {tries}")
        else:
            print("Correct guess!")

        # Display the word with guessed letters
        print(display_word(word, guessed_letters))

        # Check if the word has been fully guessed
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word!")
            break

    if tries == 0:
        print("Sorry, you've run out of tries. The word was:", word)

# Call the hangman function to play the game
hangman()
