# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

import function
from game import *

if __name__ == '__main__':
    print("Welcome to play the sichuan Majong game!")
    user = input('please enter your name: ')
    game = game(user)

    while game.ask():
        game.start()


