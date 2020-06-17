"""
Hangman v1.01

Updates in 1.01:
-Added feature where when user input an empty string,it will be recognize as wrong (Before this version you will get an error if you blank the input when the game asks you to give a letter)
"""
from random import randint
trial = 0
list_of_word = ["cow","pig","sheep","eagle","scorpion","cat","dog","lizard","snake","tiger","lion","panther","crocodile","spider","elephant","panda","beaver","squirrel","chicken","wolf","buffalo","parrot","dolphin","tortoise","turtle","peacock","catfish","lizard","butterfly","python","anaconda","baboon","monkey","raccoon","dragonfly","penguin","goose","duck","sparrow","kangaroo"]
animal = list_of_word[randint(0, len(list_of_word) - 1)]
animal_full = animal
length_animal = len(animal)
length_guess = []
string_guess = ""
guess = ""
where = None
game_start = False
correct = False
after_answering = False

def print_the_hangman():
    if trial == 0:
        print("""
_________
|        |
|
|
|
|
|
        """)
    elif trial == 1:
        print("""
_________
|        |
|        O
|
|
|
|
        """)
    elif trial == 2:
        print("""
_________
|        |
|        O
|        |
|        |
|
|
        """)
    elif trial == 3:
        print("""
_________
|        |
|        O
|       /|
|        |
|
|
        """)
    elif trial == 4:
        print("""
_________
|        |
|        O
|       /|\\
|        |
|
|
        """)
    elif trial == 5:
        print("""
_________
|        |
|        O
|       /|\\
|        |
|       /
|
        """)
    elif trial == 6:
        print("""
_________
|        |
|        O
|       /|\\
|        |
|       / \\
|
        """)

def win(trial,string_guess):
    print(string_guess)
    print(f"You win! in {trial} trial")
    while True:
        trial = 0

def check_guessing(guess,animal,after_answering,correct):
    global string_guess
    global trial
    if guess == "":
        trial += 1
        correct = False
        after_answering = True
        guessing(game_start,correct,string_guess,trial,after_answering)
    guess = guess[0]
    if guess in animal:
        while guess in animal:
            where = animal.index(guess)
            length_guess.insert(where, guess.upper())
            length_guess.pop(where + 1)
            animal = list(animal)
            animal.pop(where)
            animal.insert(where, "_")
            string_guess = " ".join(length_guess)
            correct = True
        after_answering = True
        guessing(game_start,correct,string_guess,trial,after_answering)
    else:
        trial += 1
        correct = False
        after_answering = True
        guessing(game_start,correct,string_guess,trial,after_answering)
        
def guessing(game_start,correct,string_guess,trial,after_answering):
    if game_start == False:
        while len(length_guess) != length_animal:
            length_guess.append("_")
        string_guess = " ".join(length_guess)
        game_start = True
    print_the_hangman()
    if after_answering == True:
        if correct == True:
            print("Your guessing is right!")
            correct = False
            after_answering = False
            x = "_" in string_guess
            if x == False:
                win(trial,string_guess)
        elif correct == False:
            print(f"Trial : {trial}")
            if trial == 6:
                print("You lose :(")
                print(f"The animal is : {animal_full}")
                while True:
                    trial = 6
            print("Your guessing is wrong! Try again!")
            after_answering = False
    print(string_guess)
    guessing_2()

def guessing_2():
    guess = input("Guess da word! Type your guessing : ")
    guess.lower()
    guess.strip()
    check_guessing(guess,animal,after_answering,correct)

guessing(game_start,correct,string_guess,trial,after_answering)
