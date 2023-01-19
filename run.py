"""
Hangman

1 When user starts game, computer chooses a random word from a list.

2 Computer will display dashes representing the word

3 User will get a chance to guess 1 letter at a time.
    - If they enter something that's not a letter, print an error
      and ask them to try again
    - If they've guessed the letter before, tell them they have
      and give them another chance
    - If they guess a letter they haven't guessed before, check whether
      it's in the word, and reveal it.
      Also show them the list of letters they've already guessed

4 Repeat 3 until the game is over. Game is over when:
    - Word is guessed -- tell them they've won
    - They've reached a preset number of failures
"""
import stages

NUM_INCORRECT_GUESSES_ALLOWED = 6


def get_word():
    """Return a random word from the word bank.

    Returns:
        str - A word.
    """


    return 'charge'

def print_dashed_word(word, correct_guesses):
    """Given a word, display dashes representing.

    Args:
        word: str - The word to display.
        correct_guesses: list of str - List with correctly guessed letters.
    """

    dashed_word = ''

    for letter in word:
        if letter in correct_guesses:
            dashed_word += f' {letter}'
        else:
            dashed_word += ' _'

    print(dashed_word)

def get_user_guess(guessed_letters):
    """Ask the user for a letter and validate their input.

    Validations:
        - Guess should be a single letter in the roman alphabet.
        - Letters should not have been guessed previously in the game.

    Args:
        guessed_letters: list of str - List of letters previously guessed.

    Returns:
        str - The user's guess, converted to lowercase and with any leading/
        trailing spaces removed.
    """

    # Wrap your input request logic in a while True block.
    while True:
        # 1. Ask user for input. Always strip inputs.
        # Where you'll want to compare the input to something and the
        # said comparison is not case sensitive, then convert to the target
        # case
        user_guess = input('\nGuess a letter. ').strip().lower()

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


def main():

    print('Game has started!')

    word = get_word()

    guessed_letters = []
    correct_guesses = []
    incorrect_guesses = 0

    while incorrect_guesses < NUM_INCORRECT_GUESSES_ALLOWED:
        print('\n\n')
        print_dashed_word(word, correct_guesses)
        print(f'Guessed letters: {guessed_letters}')

        guessed_letter = get_user_guess(guessed_letters)

        guessed_letters.append(guessed_letter)

        if guessed_letter not in word:
            incorrect_guesses += 1
            print(f'You guessed wrong! '
                  f'{NUM_INCORRECT_GUESSES_ALLOWED - incorrect_guesses} guesses'
                  f' left.')

        if len(correct_guesses) == len(guessed_letter):
                print('\n')
                print('Congrats, you guessed the word')          

        else:
            correct_guesses.append(guessed_letter)


main()
