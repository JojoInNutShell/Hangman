"""
Hangman v1.1
Updates in 1.1:
-Added more categories which are fruits,operating systems and programming languages
-Added main menu
-A little variable name difference
-Some bug fixing

I'm really sorry for the really messy code
"""
from random import randint
import sys
list_of_os = ["macintosh","ios","android","windows","ubuntu","linux","unix","parrot","dos","harmony","ms-dos","tizen","zorin","bsd","freebsd","gnu","freedos","kali","xubuntu"]
list_of_programming_lang = ["c#","c++","algol","ada","assembly","asp","bash","c","cobol","delphi","fortran","f#","html","java","javascript","matlab","pascal","lisp","perl","php","python","r","ruby","rust","vbscript"]
list_of_animal = ["cow","pig","sheep","eagle","scorpion","cat","dog","lizard","snake","tiger","lion","panther","crocodile","spider","elephant","panda","beaver","squirrel","chicken","wolf","buffalo","parrot","dolphin","tortoise","turtle","peacock","catfish","lizard","butterfly","python","anaconda","baboon","monkey","raccoon","dragonfly","penguin","goose","duck","sparrow","kangaroo"]
list_of_fruit = ["apple","avocado","blackberry","blueberry","cherry","coconut","dragonfruit","durian","grape","guava","lemon","lime","kiwi","lychee","melon","mango","watermelon","melon","orange","papaya","peach","pear","plum","pineapple","pineberry","raspberry","redcurrant","blackcurrant","strawberry","salak","yuzu","tomato"]

def main_menu():
    global where
    after_answering = False
    trial = 0
    string_guess = ""
    game_start = False
    correct = False
    length_guess = []
    where = ""
    choose = input("""
Welcome to the Hangman Game! (v1.1)

Please choose the category which you want to play :
    1) Animal
    2) Fruit
    3) Programming Language
    4) Operating System
    
    5) Exit 

    Choose : """)

    if choose == "1":
        word = list_of_animal[randint(0, len(list_of_animal) - 1)]
        word_full = word
        length_word = len(word)
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    elif choose == "2":
        word = list_of_fruit[randint(0, len(list_of_fruit) - 1)]
        word_full = word
        length_word = len(word)
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    elif choose == "3":
        word = list_of_programming_lang[randint(0, len(list_of_programming_lang) - 1)]
        word_full = word
        length_word = len(word)
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    elif choose == "4":
        word = list_of_os[randint(0, len(list_of_os) - 1)]
        word_full = word
        length_word = len(word)
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    elif choose == "5":
        sys.exit(0)
    else:
        print("Please input valid number to choose the menu")
        main_menu()

def play_again():
    choose = input("Do you want to go to the main menu 1)Yes 2)No ?  ")
    choose.lower()
    if choose == "1" or choose == "yes":
        main_menu()
    elif choose == "2" or choose == "no":
        print("Thank you for playing this game! See ya later")
        sys.exit(0)
    else:
        print("Please input a valid number")

def win(trial,string_guess):
    print(string_guess)
    print(f"You win! in {trial} trial")
    play_again()

def check_guessing(guess,after_answering,correct,word,trial,string_guess,game_start,length_guess,word_full,length_word):
    if guess == "":
        trial += 1
        correct = False
        after_answering = True
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    guess = guess[0]
    if guess in word:
        while guess in word:
            where = word.index(guess)
            length_guess.insert(where, guess.upper())
            length_guess.pop(where + 1)
            word = list(word)
            word.pop(where)
            word.insert(where, "_")
            string_guess = " ".join(length_guess)
            correct = True
        after_answering = True
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
    else:
        trial += 1
        correct = False
        after_answering = True
        guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial)
        
def guessing(after_answering,game_start,correct,string_guess,length_guess,length_word,word,word_full,trial):
    if game_start == False:
        while len(length_guess) != length_word:
            length_guess.append("_")
        string_guess = " ".join(length_guess)
        game_start = True
    print_the_hangman(trial)
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
                print(f"The word is : {word_full.upper()}")
                play_again()
            print("Your guessing is wrong! Try again!")
            after_answering = False
    print(string_guess)
    guess_input(word,after_answering,correct,trial,string_guess,game_start,length_guess,where,word_full,length_word)

def guess_input(word,after_answering,correct,trial,string_guess,game_start,length_guess,where,word_full,length_word):
    guess = input("Guess da word! Type your guessing : ")
    guess.lower()
    guess.strip()
    check_guessing(guess,after_answering,correct,word,trial,string_guess,game_start,length_guess,word_full,length_word)

def print_the_hangman(trial):
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


main_menu()
