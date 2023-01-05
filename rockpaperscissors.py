"""
Rock Paper Scissors
"""

import random

def chooseWeapon():
    return random.randint(1,3)

def main():
    userWeapon = input("Enter your choice: rock, paper, or scissors:")
    userWeapon = userWeapon.lower()

    valid = True
    
    if userWeapon == 'rock' or userWeapon == 'paper' or userWeapon == 'scissors':
        valid = True
    else:
        valid = False

    while valid == False:
        userWeapon = input("Please enter a valid choice, either rock, paper, or scissors:")
        userWeapon = userWeapon.lower()
        if userWeapon == 'rock' or userWeapon == 'paper' or userWeapon == 'scissors':
            valid = True

    play = True
                
    while play:
        computer = chooseWeapon()
        if computer == 1:
            print("The computer threw rock, you threw " + userWeapon)
        elif computer == 2:
            print("The computer threw paper, you threw " + userWeapon)
        else:
            print("The computer threw scissors, you threw " + userWeapon)
                
        if userWeapon == 'rock':
            user = 1
            if computer == 2:
                win = False
            elif computer == 3:
                win = True
                    
        elif userWeapon == 'paper':
            user = 2
            if computer == 1:
                win = True
            elif computer == 3:
                win = False
                
        else:
            user = 3
            if computer == 1:
                win = False
            elif computer == 2:
                win = True

        if computer == user:
            print("You tied.")
        elif win:
            print("You beat the computer!\n")
        elif not win:
            print("The computer beat you.\n")

        choice = input("Enter Y or y to play again, and any other key to stop gameplay.:")

        if choice == 'y' or choice == 'Y':
            userWeapon = input("\nEnter your choice: rock, paper, or scissors:")
            userWeapon = userWeapon.lower()
            play = True
        else:
            play = False
                
main()

        
