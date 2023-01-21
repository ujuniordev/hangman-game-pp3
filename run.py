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
    - If the user enters a letter he hadn't guessed before, check whether
      it's in the word, reveal it, and display the list of guessed letters.
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
import random, stages
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
        correct_guesses: list of str - The list where the correct guesses'
        letters are kept.
    """

    dashed_word = ''
    # Iterate the letters in the word to print either the guessed letter 
    # or the dash
    for letter in word:
        if letter in correct_guesses:
            dashed_word += f' {letter}'
        else:
            dashed_word += ' _'

    print(dashed_word)


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

    # Wrap your input request logic in a while True block.
    while True:
        # 1. Ask user for input. Always strip inputs.
        # Where you'll want to compare the input to something and the
        # said comparison is not case sensitive, then convert to the target
        # case
        user_guess = input('\nGuess a letter. \n').strip().lower()

        # 2. Check whether input violates a validation rule.
        # Do this for all your rules in separate if statements.
        # If if does, warn them and go back to the top of the while loop.
        if len(user_guess) > 1 or not user_guess.isalpha():
            print('Please enter a valid letter.')
            continue

        if user_guess in guessed_letters:
            print('You\'ve already guessed that letter.')
            continue

        # 3. If we ever get here, it means we never went into any of
        # the if statements, i.e. none of the rules were violated so
        # the input must be valid.
        # We can break out of the loop and use the input.
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

    if len(set(word)) == len(correct_guesses):
        print('\nCongrats, you guessed the word!')
        print('--------------------------------')
        check_play_again()

    if num_incorrect_guesses == NUM_INCORRECT_GUESSES_ALLOWED:
        print(f'\nSorry, you lost\n\nThe word was {word}\n')
        check_play_again()


def check_play_again():
    """ After the end game result is displayed, check if the user
        wants to play again or not.

    Returns:
        str - The lowercase letter y for yes/play again or any
              other letter to exit the game, without any spaces.
    """
    play_gain = input("Enter y to play again or any other key to exit: \n").strip().lower()
    if play_gain == 'y':
        main()
    else:
        exit()


def main():
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

    guessed_letters = []
    correct_guesses = []
    num_incorrect_guesses = 0

    print('Welcome to the Hangman Game! Try to guess the secret word')

    word = get_word()
    print('\n')
    print_dashed_word(word, correct_guesses)

    while num_incorrect_guesses < NUM_INCORRECT_GUESSES_ALLOWED:

        print('\n')

        guessed_letter = get_user_guess(guessed_letters)

        guessed_letters.append(guessed_letter)

        if guessed_letter not in word:
            num_incorrect_guesses += 1
            print(f'Wrong letter! '
                  f'{NUM_INCORRECT_GUESSES_ALLOWED - num_incorrect_guesses} guesses'
                  f' left.')

        else:
            correct_guesses.append(guessed_letter)
        print(stages.get_hangman_stage(num_incorrect_guesses))
        print_dashed_word(word, correct_guesses)
        print(f'These are the guessed letters: {guessed_letters}')
        end_game(word, correct_guesses, num_incorrect_guesses)


main()
