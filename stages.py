""" """
def get_hangman_stage(incorrect_guesses, NUM_INCORRECT_GUESSES_ALLOWED):
    """ Contains the list of the hangman stages to be displayed
        acoording to the remaining chances

        Args: incorrect_guesses - Number of incorrect attempts

        Return: str - A string containing the representation of the hangman
                      based on the index and according to the remaining
                      lifes/chances
    """
   
    # The stages are the result of the number of incorrect
    # guesses - incorrect_guesses 
    # Depending on the result, the index of the stages list
    # will be displayed to the user
    stages = ["""
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------    
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """]

    return stages[NUM_INCORRECT_GUESSES_ALLOWED - incorrect_guesses]
