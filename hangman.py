import random

previous_guesses = []


def create_word_list():
    file = open("words.txt", "r")
    content = file.readlines()
    file.close()
    word_list = [item.removesuffix("\n") for item in content]
    return word_list


def choose_word(new_list: list):
    random_word = random.choice(new_list)
    return random_word


def create_underscore(secret_word):
    beginning_string: str = ""
    for _ in secret_word:
        beginning_string = beginning_string + "_ "
    return beginning_string


def reveal_progress(secret_word, previous_guesses):
    user_interface = ""
    for letter in secret_word:
        if letter in previous_guesses:
            user_interface = user_interface + letter
        else:
            user_interface = user_interface + "_ "
    return user_interface


def format_guesses_user_order(previous_guesses):
    converted = ', '.join(map(str, previous_guesses[0:-1]))
    final = converted + " and " + str(previous_guesses[-1])
    return final


def format_guesses_alphabetical_order(previous_guesses):
    alphabetical_order = sorted(previous_guesses)
    alphabetical_converted = ', '.join(map(str, alphabetical_order[0:-1]))
    alphabetical_final = alphabetical_converted + " and " + str(alphabetical_order[-1])
    return alphabetical_final


def present_guesses(previous_guesses, lower_cased_guessed):
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


def input_validation(lower_cased_guessed):
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


def counting_mistakes(secret_word, lower_cased_guessed):
    mistakes_list = []
    if lower_cased_guessed not in secret_word:
        mistakes_list.append("mistake")
        print("Wrong guess! A poor man will be soon hanged!")
    else:
        print("Correct guess!")
    mistakes_list_num = len(mistakes_list)
    print("Number of mistakes: ", mistakes_list_num)
    return mistakes_list_num


def diagram(number):
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


def check_winning(secret_word, previous_guesses):
    checking_list = []
    for letter in secret_word:
        check_letter = str(letter in previous_guesses)
        checking_list.append(check_letter)
    you_won = "False" not in checking_list
    if you_won:
        print("Congratulations, you won!")
    return you_won


def game_loop():
    mistakes_num = 0
    while mistakes_num < 6:
        letter_guessed: str = input("Please suggest a letter: ")
        lower_cased_guessed = letter_guessed.lower()
        validation_result = input_validation(lower_cased_guessed)
        if not validation_result:
            continue
        progress = reveal_progress(secret_word, previous_guesses)
        print(progress)
        present_guesses(previous_guesses, lower_cased_guessed)
        mistakes_num = counting_mistakes(secret_word, lower_cased_guessed)
        diagram(mistakes_num)
        if mistakes_num == 6:
            print("Game over! You lost!")
            print("Your secret word was:", secret_word)
            break
        winning = check_winning(secret_word, previous_guesses)
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
secret_word = choose_word(new_list)
print(create_underscore(secret_word))
game_loop()