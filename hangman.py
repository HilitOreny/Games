"""using random module, a secret word will be randomly chosen"""
import random


def create_word_list():
    """
    This function opens a file called "words.txt".
    The function reads the file, copies its content to a list
    and formats it.
    """
    file = open("words.txt", "r")
    content = file.readlines()
    file.close()
    word_list = [item.removesuffix("\n") for item in content]
    return word_list


def choose_word(words_list: list):
    """
    This function chooses a random word from the list.
    This word will be later used by other functions as the secret word for the game.
    param words_list type: list
    :return: random_word
    :rtype: str
    """
    random_word = random.choice(words_list)
    return random_word


def create_underscore(word1):
    """
    This function converts the secret word to a sequence of underscores.
    :param word1: a word which the user needs to guess
    :type word1: str
    :return: a sequence of underscores
    :rtype: str
    """
    beginning_string: str = ""
    for _ in word1:
        beginning_string = beginning_string + "_ "
    return beginning_string


def reveal_progress(word2, list1):
    """
    This function reveals the progress of the game.
    This function returns a string of letters and underscores.
    The letters are the right guesses, in their position in the secret word.
    A letter which the user has not guessed yet, is replaced with an underscore.
    :param list1: a list of the previous guesses of the user.
    :param word2: the word the user needs to guess
    type word2: str
    :return: user_interface
    :rtype: str
    """
    user_interface = ""
    for letter in word2:
        if letter in list1:
            user_interface = user_interface + letter
        else:
            user_interface = user_interface + "_ "
    return user_interface


def format_guesses(list2):
    """This function converts a list of letters to a string.
    :param list2: previous guesses of the user
    :type list2: list
    :return: sequence of letters
    :rtype: str
    """
    converted = ', '.join(map(str, list2[0:-1]))
    final = converted + " and " + str(list2[-1])
    return final


def present_guesses(user_guesses_list, one_letter):
    """This function presents the list of previous guesses in two formats.
    The first format is guessing order.
    The second format is alphabetical order.
    :param one_letter: a lower-cased string of user's input
    :type one_letter: str
    :param user_guesses_list: previous guesses of the user
    :type user_guesses_list: list
    """
    if len(user_guesses_list) > 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        current_list = format_guesses(user_guesses_list)
        print(current_list)
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_order = sorted(current_list)
        alphabetical_list = format_guesses(alphabetical_order)
        print(alphabetical_list)
    elif len(user_guesses_list) == 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        print(user_guesses_list[0], "and", user_guesses_list[1])
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_two_letters = sorted(user_guesses_list)
        print(alphabetical_two_letters[0], "and", alphabetical_two_letters[1])
    else:
        print("You have only guessed one letter:", one_letter)


class MultipleCharacters(Exception):
    """This class is later used for user's input validation"""


def one_character_validation(character):
    """
    this function validates that the user's input is only 1 character.
    :param character: a lower-cased string of user's input
    :type character: str
    :return: a statement whether the input is only 1 character.
    :rtype: bool
    """
    try:
        if len(character) != 1:
            raise MultipleCharacters
    except MultipleCharacters:
        print("Please suggest just one letter...")
    return len(character) == 1


class Repeat(Exception):
    """This class is later used for user's input validation"""


def non_repeat_validation(current_letter, validation_list):
    """
    this function validates that the user's input is only 1 character.
    :param current_letter: a lower-cased string of user's input
    :type current_letter: str
    :param validation_list: a list of letters which were already guessed
    :type validation_list: list
    :return: a statement whether the input is only 1 character.
    :rtype: bool
    """
    try:
        if current_letter in validation_list:
            raise Repeat
    except Repeat:
        print("""You have already guessed this letter...
    Please suggest a different letter.""")
    return current_letter in validation_list


class NoAlpha(Exception):
    """This class is later used for user's input validation"""


def alpha_validation(user_input):
    """
    this function validates that the user's input contains only letters.
    :param user_input: a lower-cased string of user's input
    :type user_input: str
    :return: does the user's input contain only letters?
    :rtype: bool
    """
    try:
        if not user_input.isalpha():
            raise NoAlpha
    except NoAlpha:
        print("""Please suggest a letter.
              No numbers or symbols, please...""")
    return user_input.isalpha()


def check_letter_in_word(word3, character2):
    """
    :param word3: the secret word
    :type word3: str
    :param character2: the character which the user entered
    :type character2: str
    :return: is the character in the word?
    :rtype: bool
    """
    check_in = character2 in word3
    return check_in


def present_message(true_guess):
    """
    :param true_guess: is the guess correct?
    :type true_guess: bool
    """
    if true_guess:
        print("Correct guess!")
    else:
        print("Wrong guess! A poor man will be soon hanged!")


def create_mistakes_list(true_guess, character3, user_mistakes_list):
    """
    :param true_guess: is the guess correct?
    :type true_guess: bool
    :param character3: the character which the user entered
    :type character3: str
    :type user_mistakes_list: list
    :return: an updated version of the user_mistakes_list
    :rtype: list
    """
    if not true_guess:
        user_mistakes_list.append(character3)
    return user_mistakes_list


def counting_mistakes(my_list):
    """
    :param my_list: a list of mistakes
    :type my_list: list
    :return: the number of mistakes
    :rtype: int
    """
    my_list_num = len(my_list)
    print("Number of mistakes: ", my_list_num)
    return my_list_num


def diagram(number):
    """
    this function returns the relevant diagram
    based on the number of mistakes.
    :param number: number of mistakes
    :type number: int
    :rtype: str
    """
    hangman_diagram = {0: "x-------x", 1: """
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
    current_diagram = hangman_diagram[number]
    return current_diagram


def find_winning_number(letter_in_word, winning_number):
    """
    :param letter_in_word: is the letter in the secret word?
    :type letter_in_word: bool
    :param winning_number: the number of correct guesses
    :return: a number of the correct guesses of the user
    :rtype: int
    """
    if letter_in_word:
        winning_number = winning_number + 1
    return winning_number


def check_winning(word4, winning_num):
    """
    :param word4: the secret word
    :type word4: str
    :param winning_num: the correct guesses of the user
    :type winning_num: int
    :return: has the user guessed all the letters?
    :rtype: bool
    """
    you_won = len(word4) == winning_num
    if you_won:
        print("Congratulations, you won!")
    return you_won


def game_loop(secret_word):
    """
    the loop creates multiple turns.
    """
    previous_guesses_list = []
    mistakes_list = []
    correct_guesses_num = 0
    mistakes_num = 0
    while mistakes_num < 6:
        letter_guessed: str = input("Please suggest a letter: ")
        lower_cased_guessed = letter_guessed.lower()
        valid1 = one_character_validation(lower_cased_guessed)
        valid2 = non_repeat_validation(lower_cased_guessed, previous_guesses_list)
        valid3 = alpha_validation(lower_cased_guessed)
        valid = valid1 and valid2 and valid3
        if not valid:
            continue
        progress = reveal_progress(secret_word, previous_guesses_list)
        print(progress)
        present_guesses(previous_guesses_list, lower_cased_guessed)
        is_correct = check_letter_in_word(secret_word, lower_cased_guessed)
        present_message(is_correct)
        your_mistakes_list = create_mistakes_list(is_correct, lower_cased_guessed, mistakes_list)
        mistakes_num = counting_mistakes(your_mistakes_list)
        print(diagram(mistakes_num))
        if mistakes_num == 6:
            print("Game over! You lost!")
            print("Your secret word was:", secret_word)
            break
        find_winning_number(is_correct, correct_guesses_num)
        winning = check_winning(secret_word, correct_guesses_num)
        if winning:
            break


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
new_list = create_word_list()
chosen_word = choose_word(new_list)
print(create_underscore(chosen_word))
game_loop(chosen_word)
