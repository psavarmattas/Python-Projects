""" 
----------------------------------------
Mad Libs Generator
----------------------------------------
This python beginner project is a good start for beginner software developers as it has concepts 
like strings, variables, and concatenation. Mad Libs Generator teaches to manipulate user-inputted 
data as the Mad Libs refer to a series of inputs that a user enters. The input from the user could be 
anything from an adjective, a pronoun, or even a verb. After all the inputs are entered the application 
takes all the data and arranges it to build a story template. 
----------------------------------------
"""

# Loop back to this point once code finishes
loop = 1
while (loop < 10):
# All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
# Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
# Loop back to "loop = 1"
    continue_program = input("Do you want to continue(Y/N): ")
    if (continue_program == "n"):
        break
    elif (continue_program == "y"):
        loop = loop + 1
    else:
        print("Wrong input!")
        break