previous_guesses = []
mistakes_list = []


def format_guesses_user_order(previous_guesses):
    """This function sorts previous_guesses list by user's order.
    :param previous_guesses: previous guesses of the user
    :type previous_guesses: str
    :return: sequence of letters
    :rtype: list
    """
    create_list1 = previous_guesses[0:-1]
    last_item1 = previous_guesses[-1]
    last_item_and1 = "and " + str(last_item1)
    last_item_list1 = [last_item_and1]
    new_list1 = create_list1 + last_item_list1
    sequence1 = ", ".join(new_list1)
    return sequence1


def format_guesses_alphabetical_order(previous_guesses):
    """This function sorts previous_guesses list by alphabetical order.
    :param previous_guesses: previous guesses of the user
    :type previous_guesses: str
    :return: sequence of letters
    :rtype: list
    """
    alphabetical_order = sorted(previous_guesses)
    create_list2 = alphabetical_order[0:-1]
    last_item2 = alphabetical_order[-1]
    last_item_and2 = "and " + str(last_item2)
    last_item_list2 = [last_item_and2]
    new_list2 = create_list2 + last_item_list2
    sequence2 = ", ".join(new_list2)
    return sequence2


def present_guesses(previous_guesses, lower_cased_guessed):
    """This function presents the list of previous guesses in two formats.
    The first format is guessing order.
    The second format is alphabetical order.
    :param lower_cased_guessed: a lower-cased string of user's input
    :type lower_cased_guessed: str
    :param previous_guesses: previous guesses of the user
    :type previous_guesses: str
    :return: None
    """
    if len(previous_guesses) > 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        current_list = format_guesses_user_order(previous_guesses)
        print(current_list)
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_list = format_guesses_alphabetical_order(previous_guesses)
        print(alphabetical_list)
    elif len(previous_guesses) == 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        print(previous_guesses[0], "and", previous_guesses[1])
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_two_letters = sorted(previous_guesses)
        print(alphabetical_two_letters[0], "and", alphabetical_two_letters[1])
    else:
        print("You have only guessed one letter:", lower_cased_guessed)
    return None


def input_validation(lower_cased_guessed):
    """This function gets an input from the user and checks if it's a valid input for Hangman.
    A valid input is a letter of English alphabet which was not previously guessed by the user.
    Note that isalpha is not helpful because it defines non-English alphabet as valid.
    If the input is valid, the function prints the input and adds it to previous_guesses list.
    Else, the function prints the relevant error.
    :param lower_cased_guessed: a lower-cased string of user's input
    :type lower_cased_guessed: str
    :return: valid
    :rtype: bool
    """
    compare = lower_cased_guessed not in previous_guesses
    only_english = lower_cased_guessed in "abcdefghijklmnopqrstuvwxyz"
    valid = only_english and len(lower_cased_guessed) == 1 and compare
    if valid:
        previous_guesses.append(lower_cased_guessed)
    if len(lower_cased_guessed) > 1:
        print("Please suggest just one letter...")
    if not only_english:
        print("""Please suggest a letter of English alphabet.
              No numbers, symbols or any other letters, please...""")
    if not compare:
        print("You have already guessed this letter...Please suggest a different letter.")
        present_guesses(previous_guesses, lower_cased_guessed)
    return valid


def reveal_progress(secret_word, previous_guesses):
    """
    This function reveals the progress of the game.
    This function returns a string contains letters and underscores.
    The letters are the right guesses from previous_guesses, in their position in the secret word.
    A letter which the user has not guessed yet, is replaced with an underscore.
    :param previous_guesses: a list of the previous guesses of the user.
    :param secret_word: the word the user needs to guess
    type secret_word: string
    :return: user_interface
    :rtype: str
    """
    user_interface = ""
    for letter in secret_word:
        if letter in previous_guesses:
            user_interface = user_interface + letter
        else:
            letter_replaced = "_ "
            user_interface = user_interface + letter_replaced
    return user_interface


# This dictionary contains the diagram of an hanged man.
HANGMAN_DIAGRAM = {0: "x-------x", 1: """
    x-------x
    |
    |
    |
    |
    |""", 2: """
    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def counting_mistakes(secret_word, lower_cased_guessed):
    """
    This function checks if the letter suggested by the user is in the secret word,
    and prints the relevant feedback.
    If the guess was wrong, the function prints the relevant diagram,
    based on the number of the user's wrong guesses.
    When the the number of mistakes is 6, the function prints a losing message.
    :param secret_word: the word the user needs to guess
    :type secret_word: str
    :param lower_cased_guessed: a lower-cased string of user's input.
    :type lower_cased_guessed: str
    :return: list_length
    :rtype: int
    """
    if lower_cased_guessed not in secret_word:
        mistakes_list.append("mistake")
        print("Wrong guess! A poor man will be soon hanged!")
    else:
        print("Correct guess!")
    mistakes_num = len(mistakes_list)
    print("Number of mistakes: ", mistakes_num)
    current_diagram = HANGMAN_DIAGRAM[mistakes_num]
    print(current_diagram)
    if mistakes_num == 6:
        print("Game over! You lost!")
        print("Your secret word was:", secret_word)
    return mistakes_num


def check_winning(secret_word, previous_guesses):
    """This functions checks if the user guessed all the letters of the secret word.
    :param secret_word: the word the user needs to guess
    :type secret_word: str
    :param previous_guesses: previous guesses of the user
    :type previous_guesses: list
    :return: you_won param
    :rtype: bool
    """
    checking_list = []
    for letter in secret_word:
        check_letter = str(letter in previous_guesses)
        checking_list.append(check_letter)
    you_won = "False" not in checking_list
    if you_won:
        print("Congratulations, you won!")
    return you_won


def game_loop():
    """
    This function creates a loop to create multiple turns for the same game.
    First, a secret word is chosen and presented on the screen.
    Afterwards, in each turn, the user suggests a letter.
    If the user's input is not valid,
    the program prints an error and urges the user to suggest a different input.
    Then, a string contains letters and underscores is presented on the screen.
    As the loop runs, the user suggests more letters and sees the letters he/she already guessed.
    The loop breaks when the user wins or loses.
    The user wins when he/she finds all the letters of the secret word.
    The user loses the game in the sixth mistake.
    """
    mistakes_num = 0
    winning = False
    secret_word = choose_word()
    print(create_underscore(secret_word))
    while winning == False and mistakes_num < 6:
        letter_guessed: str = input("Please suggest a letter: ")
        lower_cased_guessed = letter_guessed.lower()
        validation_result = input_validation(lower_cased_guessed)
        if not validation_result:
            continue
        progress = reveal_progress(secret_word, previous_guesses)
        print(progress)
        winning = check_winning(secret_word, previous_guesses)
        if winning:
            break
        mistakes_num = counting_mistakes(secret_word, lower_cased_guessed)
        if mistakes_num == 6:
            break
        present_guesses(previous_guesses, lower_cased_guessed)
    return None


def create_underscore(secret_word):
    """
    This function converts the secret word to a sequence of underscores.
    :param secret_word: a word which the user needs to guess
    :type secret_word: str
    :return: a sequence of underscores
    :rtype: str
    """
    beginning_string: str = ""
    for _ in secret_word:
        beginning_string = beginning_string + "_"
    return beginning_string


def choose_word():
    """
    This function uses a file called "words".
    The file contains English basic vocabulary which is used in both American and British dialects.
    The function reads the file and copies its content to a list.
    The function formats the list and then, chooses a random word from the list.
    This word will be the secret word for the game.
    :return: random_word
    :rtype: str
    """
    import random
    file = open("words.txt", "r")
    for _ in file:
        content = file.read()
        formatted_list = content.split("\n")
    file.close()
    random_word = random.choice(formatted_list)
    return random_word


print("""Welcome to hangman!
In this game, your goal is to guess the secret word before an innocent man is hanged.
The secret word will be shown as a sequence of underscores (_). Each underscore represents a letter.
For example, _ _ _ is a three-letter word.
Each turn, you will suggest a letter.
If the letter occurs in the secret word, the letter will appear in the word in its position.
If the suggested letter does not occur in the word, your mistake is fatal!
A diagram of an hanged person will gradually appear, based on the number of your wrong guesses.
In the sixth mistake, you will lose the game and the poor man will be hanged!
Let's Begin!
Here is your secret word: """)
game_loop()
