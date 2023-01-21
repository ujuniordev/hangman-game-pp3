"""
The Hangman game

1 - As soon as the game starts the computer picks a random word from the
    list of words.

2 - The computer displays the representation of the word in dashes.
    Each dash is a letter of the word.

3 - The user has 6 chances to guess the word by trying 1 letter at a time.
    - If the user enters an invalid character, print an error message
      and ask them to try again, no penalties for that.
    - If the user had already guessed the letter before, print a message
      and give him another chance, no penalties for that.
    - If the user enters a letter he hadn"t guessed before, check whether
      it"s in the word, reveal it, and display the list of guessed letters.
    - If the letter is not in the word, display the list of letters that
      were entered, reduce one life from the 6 chances counter
      and display the remaining chances.

4 - Repeat 3 until the remaining chances are over or when the word is guessed.
    - If the word is guessed, display the success/victory message and ask if
      the user wants to play again or exit the game.
    - If the chances were over, display the game over message ask if the user
      wants to play again or exit the game.

5 - If after the end of the game the user says he wants to play again,
    start 1 again.
  - If the user says no then the game ends and exit.
"""

# Import the random function + stages file + words list
import random
import stages
from words import words

NUM_INCORRECT_GUESSES_ALLOWED = 6


def get_word():
    """ Gets a random word from the words.py file.

    Returns:
        str - Word.
    """
    return random.choice(words)


def print_dashed_word(word, correct_guesses):
    """ Based on the random word, displays the corresponding dashes of the
        legth of the word.

    Args:
        word: str - The random word.
        correct_guesses: list of str - The list where the correct guesses"
        letters are kept.

    Returns:
        str - The dashed word or the guessed letter if it is in the word
    """

    dashed_word = ""

    # Iterate the letters of the word to print either the guessed letter
    # or the dash
    for letter in word:
        if letter in correct_guesses:
            dashed_word += f" {letter}"
        else:
            dashed_word += " _"

    print(dashed_word)
    print("\n")


def get_user_guess(guessed_letters):
    """ Once the game has started, this function request the user for a letter
        and makes the character validation.

    Validations:
        - Only a single roman alphabet letter.
        - Unique letters, meaning that they should not have been used before
          in the game.

    Args:
        guessed_letters: list of str - List of letters previously guessed.

    Returns:
        str - The letter the user added in a lower case format with spaces
        removed.
    """

    # Input validation while
    while True:
        # Stores the input letter in user_guess variable
        # Strip the inputs to avoid blank spaces
        # Convert the letters to lower case
        user_guess = input("\nEnter a letter: \n => ").strip().lower()

        # Checks if the input is only an alphabetical letter
        # If not, print the message to the user and continue to the next action
        if len(user_guess) > 1 or not user_guess.isalpha():
            print("Please enter a valid letter.")
            continue

        # Check if it"s the first time the user enters this letter
        # If not, prints the message to the user and continue to the
        # next action
        if user_guess in guessed_letters:
            print("You\"ve already guessed that letter.")
            continue

        # If we get here it means the letter is valid and can be used
        break

    return user_guess


def end_game(word, correct_guesses, num_incorrect_guesses):
    """ Check if the user guessed the word or not and displays the result
        to the user

    Args:
        word: str - The random word.
        correct_guesses: list of str - The list of letters with the
                         correct guesses.
        num_incorrect_guesses: int - The incremental number of
                               incorrect guesses.

    Returns:
        boolean: True if the user guessed the word or false if not and
                 the maximal number of attempts were reached.
    """

    # First remove the duplicated letter by checking the length of the word
    # as a set then check if the length of the word is equal to the length of
    # the correct guesses list
    # If true then print the success message and call the play again function
    if len(set(word)) == len(correct_guesses):
        print("\nCongrats, you guessed the word!")
        print("--------------------------------")
        check_play_again()

    # Check if the number of incorrect attempts is equal to the maximum
    # number of allowed attempts
    # If true then print failure message and call the play again function
    if num_incorrect_guesses == NUM_INCORRECT_GUESSES_ALLOWED:
        print(f"\nSorry, you lost\n\nThe word was {word}\n")
        check_play_again()


def check_play_again():
    """ After the end game result is displayed, check if the user
        wants to play again or not.

    Returns:
        str - The lowercase letter y for yes/play again or any
              other letter to exit the game, without any spaces.
    """

    # In the end of the game ask the user if he wants to play
    # again by pressing y to yes or any other key to no
    # If yes then the game starts again
    # If no, then exit
    play_gain = input("Enter y to play again or any "
                      "other key to exit: \n => ").strip().lower()

    if play_gain == "y":
        main(initial_play=False)
    else:
        exit()


def main(initial_play=True):
    """ Run the game
    """

    # List with the guessed letters
    guessed_letters = []

    # List with the correct letters that were guessed
    correct_guesses = []

    num_incorrect_guesses = 0

    # Initial message
    if initial_play:
        print("\nWelcome to the Hangman Game! \nTry to guess the secret word")

    # Start game, gets the random word and prints the dashes or
    # the correct letters
    word = get_word()
    print("\n")
    print_dashed_word(word, correct_guesses)

    while num_incorrect_guesses < NUM_INCORRECT_GUESSES_ALLOWED:

        guessed_letter = get_user_guess(guessed_letters)

        guessed_letters.append(guessed_letter)

        if guessed_letter not in word:
            num_incorrect_guesses += 1
            print(f"\nWrong letter! "
                  f"{NUM_INCORRECT_GUESSES_ALLOWED - num_incorrect_guesses}"
                  f" guesses left.")

        else:
            correct_guesses.append(guessed_letter)
        print(stages.get_hangman_stage(num_incorrect_guesses,
                                       NUM_INCORRECT_GUESSES_ALLOWED))
        print_dashed_word(word, correct_guesses)
        print(f"These are the guessed letters: {guessed_letters}")
        end_game(word, correct_guesses, num_incorrect_guesses)
        print("\n")


main()
