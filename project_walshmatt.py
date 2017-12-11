# CTI 110
# FINAL PROJECT
# Matthew 'Melissa' Walsh
# 12.07.17
# A decision making game

from random import randint

# Scenario 1
def scenario1(choice):
    if choice == "true":
        with open("s1c1.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "wt") as out_file:
            out_file.write("Rustling in the leaves, rustling in the branches, are you being watched?")
    elif choice == "false":
        with open("s1c2.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "wt") as out_file:
            out_file.write("Is right always right? You don't want to be left behind... Be aware of your surroundings...")

# Scenario 2
def scenario2(choice):
    if choice == "true":
        with open("s2c1.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nAn abandonded treehouse in the woods? Who knows how long it's been there..." +
                           " A death trap, surely.")
    elif choice == "false":
        with open("s2c2.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nMaybe left... had made you be left... behind....")

# Scenario 3
def scenario3(choice):
    if choice == "true":
        with open("s3c1.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nA being, a shadow, darkness and light. What's behind that mask?")
    elif choice == "false":
        with open("s3c2.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nWere you right or were you wrong? Did they move their head? What are they hiding...")

# Scenario 4
def scenario4(choice):
    if choice == "true":
        with open("s4c1.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nClick, click, click.... Can you see it? Can you hear it? It's behind you...")
    elif choice == "false":
        with open("s4c2.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nWatch out! It's right there! Are you really safe? You got free but are you safe?")

# Scenario 5
def scenario5(choice):
    if choice == "true":
        with open("s5c1.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nWhat is the meaning of freedom? Is anybody ever really free? You escaped for now.")
    elif choice == "false":
        with open("s5c2.txt", "rt") as in_file:
            text = in_file.read()

        print(text,"\n")

        with open("out_hello.txt", "a") as out_file:
            out_file.write("\n\nIt's there. In the corner. Can you see it? It can see you. It's watching y o u.")

# Game Start
def start():

    valid = "false"
    intake = ""
    choice = ""

    while valid == "false":
        intake = input("You find yourself lost in the middle of dense woods, the entire area around you is" +
                        " pitch black. Just barely you can make out a forked path in front of you. \n\tWill " +
                       "you choose to go left or right?: ")

        intake = intake.lower()

        if intake == "left":
            choice = "true"
            valid = "true"
        elif intake == "right":
            choice = "false"
            valid = "true"
        else:
            valid = "false"
            print("\tInvalid choice, please choose again.\n")

    scenario1(choice)

    if choice == "true":
        valid = "false"
        intake = ""
        choice = ""
    
        while valid == "false":
            intake = input("\tApproaching the tree, would you like to climb it?: ")

            intake = intake.lower()

            if intake == "yes":
                choice = "true"
                valid = "true"
            elif intake == "no":
                choice = "false"
                valid = "true"
            else:
                valid = "false"
                print("\tInvalid choice, please choose again.\n")
    
        scenario2(choice)
    else:
        valid = "false"
        intake = ""
        choice = ""
        
        number = randint(0,20)
        
        while valid == "false":
            intake = int(input('\t"Now, guess a number between 1 and 20." '))

            while intake > 20:
                intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

            while intake <= 0:
                intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

            if intake > number:
                choice = "true"
                valid = "true"
            elif intake < number:
                choice = "false"
                valid = "true"
            elif intake == number:
                valid = "false"
                print("You guessed right on the first try! Now guess again.\n")
                number = randint(0,20)
            else:
                valid = "false"
                print("\tInvalid choice, please choose again.\n")

        scenario3(choice)

        if choice == "true":
            valid = "false"
            intake = ""
            choice = ""
        
            number = randint(0,20)
            
            while valid == "false":
                intake = int(input('\t"Now, guess another number between 1 and 20." '))

                while intake > 20:
                    intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

                while intake <= 0:
                    intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

                if intake > number:
                    choice = "true"
                    valid = "true"
                elif intake < number:
                    choice = "false"
                    valid = "true"
                elif intake == number:
                    valid = "false"
                    print("You guessed right on the first try! Now guess again.\n")
                    number = randint(0,20)
                else:
                    valid = "false"
                    print("\tInvalid choice, please choose again.\n")
                    
            scenario4(choice)
        else:
            valid = "false"
            intake = ""
            choice = ""
        
            number = randint(0,20)
            
            while valid == "false":
                intake = int(input('\t"Now, guess another number between 1 and 20." '))

                while intake > 20:
                    intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

                while intake <= 0:
                    intake = int(input("That is not in the range! Guess a number between 1 and 20: "))

                if intake > number:
                    choice = "true"
                    valid = "true"
                elif intake < number:
                    choice = "false"
                    valid = "true"
                elif intake == number:
                    valid = "false"
                    print("You guessed right on the first try! Now guess again.\n")
                    number = randint(0,20)
                else:
                    valid = "false"
                    print("\tInvalid choice, please choose again.\n")

            scenario5(choice)

# Main Class
def main():
    start()

    valid = "false"
    intake = ""
    
    while valid == "false":
        intake = input("Would you like to play one more time?: ")

        intake = intake.lower()

        if intake == "yes":
            valid = "true"
        elif intake == "no":
            valid = "true"
        else:
            valid = "false"
            print("\tInvalid choice, please choose again.\n")

    if intake == "yes":
        start()

    print("\t\tThanks... for..... playing... :)")

# Start the program
main()
