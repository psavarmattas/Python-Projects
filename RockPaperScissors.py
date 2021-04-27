""" 
----------------------------------------
Rock Paper Scissors
----------------------------------------
This program or a mini-game is designed when you don’t have anyone 
to play or you are under lockdown alone. There are a number of functions 
that this program requires so let us have an overview of each.

1. A random function: to generate rock, paper, or scissors. 
2. Valid function: to check the validity of the move.
3. Result function: to declare the winner of the round.
4. Scorekeeper: to keep track of the score.

The program requires the user to make the first move before it makes one 
the move. Once the move is validated the input is evaluated, the input entered 
could be a string or an alphabet. After evaluating the input string a winner 
is decided by the result function and the score of the round is updated by the 
scorekeeper function.
----------------------------------------
"""

import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    # Echo the user's choice
    print ("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("Tie! ")
    # if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        print ("Paper beat rock, I win! ")
        continue
    else:       
        print ("You win!")