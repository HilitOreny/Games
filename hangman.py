import random


def create_word_list():
    file = open("words.txt", "r")
    content = file.readlines()
    file.close()
    word_list = [item.removesuffix("\n") for item in content]
    return word_list


def choose_word(words_from_file_list: list):
    random_word = random.choice(words_from_file_list)
    return random_word


def create_underscore(word1):
    beginning_string: str = ""
    for _ in word1:
        beginning_string = beginning_string + "_ "
    return beginning_string


def reveal_progress(word2, list1):
    user_interface = ""
    for letter in word2:
        if letter in list1:
            user_interface = user_interface + letter
        else:
            user_interface = user_interface + "_ "
    return user_interface


def format_guesses_user_order(list2):
    converted = ', '.join(map(str, list2[0:-1]))
    final = converted + " and " + str(list2[-1])
    return final


def format_guesses_alphabetical_order(list3):
    alphabetical_order = sorted(list3)
    alphabetical_converted = ', '.join(map(str, alphabetical_order[0:-1]))
    alphabetical_final = alphabetical_converted + " and " + str(alphabetical_order[-1])
    return alphabetical_final


def present_guesses(user_guesses_list, one_letter):
    if len(user_guesses_list) > 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        current_list = format_guesses_user_order(user_guesses_list)
        print(current_list)
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_list = format_guesses_alphabetical_order(user_guesses_list)
        print(alphabetical_list)
    elif len(user_guesses_list) == 2:
        print("Here is a list of the letters you have guessed by guessing order: ")
        print(user_guesses_list[0], "and", user_guesses_list[1])
        print("Here is a list of the letters you have guessed by alphabetical order: ")
        alphabetical_two_letters = sorted(user_guesses_list)
        print(alphabetical_two_letters[0], "and", alphabetical_two_letters[1])
    else:
        print("You have only guessed one letter:", one_letter)


def input_validation(character, attempts_list):
    compare = character not in attempts_list
    only_english = character in "abcdefghijklmnopqrstuvwxyz"
    valid = only_english and len(character) == 1 and compare
    if valid:
        attempts_list.append(character)
    if len(character) > 1:
        print("Please suggest just one letter...")
    if not only_english:
        print("""Please suggest a letter of English alphabet.
              No numbers, symbols or any other letters, please...""")
    if not compare:
        print("You have already guessed this letter...Please suggest a different letter.")
        present_guesses(attempts_list, character)
    return valid


def check_letter(word3, character2):
    check_in = character2 in word3
    return check_in


def present_message(true_guess):
    if true_guess:
        print("Correct guess!")
    else:
        print("Wrong guess! A poor man will be soon hanged!")


def create_mistakes_list(true_guess, character3, user_mistakes_list):
    if not true_guess:
        user_mistakes_list.append(character3)
    return user_mistakes_list


def counting_mistakes(my_list):
    my_list_num = len(my_list)
    print("Number of mistakes: ", my_list_num)
    return my_list_num


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


def find_winning_number(letter_in_word, winning_number):
    if letter_in_word:
        winning_number = winning_number + 1
    return winning_number


def check_winning(word4, winning_num):
    you_won = len(word4) == winning_num
    if you_won:
        print("Congratulations, you won!")
    return you_won


def game_loop(secret_word):
    previous_guesses = []
    mistakes_list = []
    correct_guesses_num = 0
    mistakes_num = 0
    while mistakes_num < 6:
        letter_guessed: str = input("Please suggest a letter: ")
        lower_cased_guessed = letter_guessed.lower()
        validation_result = input_validation(lower_cased_guessed, previous_guesses)
        if not validation_result:
            continue
        progress = reveal_progress(secret_word, previous_guesses)
        print(progress)
        present_guesses(previous_guesses, lower_cased_guessed)
        is_correct = check_letter(secret_word, lower_cased_guessed)
        present_message(is_correct)
        your_mistakes_list = create_mistakes_list(is_correct, lower_cased_guessed, mistakes_list)
        mistakes_num = counting_mistakes(your_mistakes_list)
        print(diagram(mistakes_num))
        if mistakes_num == 6:
            print("Game over! You lost!")
            print("Your secret word was:", secret_word)
            break
        find_winning_number(is_correct, correct_guesses_num)
        check_winning(secret_word, correct_guesses_num)
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
chosen_word = choose_word(new_list)
print(create_underscore(chosen_word))
game_loop(chosen_word)
