def get_hangman_stage(incorrect_guesses):
    NUM_INCORRECT_GUESSES_ALLOWED = 6
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