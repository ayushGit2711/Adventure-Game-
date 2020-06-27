import random
import time
import pycodestyle
#function for printing with a delay

def self_print(textMessage):
    time.sleep(2)
    print(textMessage)

def intro(choice,items):
    self_print("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")
    self_print("Rumor has it that a " + choice + " is somewhere around "
               "here, and has been terrifying the nearby village.\n")
    self_print("In front of you is a house.\n")
    self_print("To your right is a dark cave.\n")
    self_print("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")
    choice_menu(items,choice)

def choice_menu(items,option):
    self_print("Enter 1 to knock on the door of house.\n")
    self_print("Enter 2 to move towards the dark cave.\n")
    take_input(items,option)

def take_input(items,option):
    while True:
        choice=input("Enter either 1 or 2.\n")
        if choice=="1":
            enter_house(items,option)
            break
        elif choice=="2":
            enter_cave(items,option)
            break
        else:
            print("WRONG INPUT!\n"+"ENTER AGAIN:\n")
            take_input(items,option)
            break

def enter_house(item,option):
    self_print("\nYou approach the door of the house.")
    self_print("\nYou are about to knock when the door "
                "opens and out steps a " + option + ".")
    self_print("\nEep! This is the " + option + "'s house!")
    self_print("\nThe " + option + " attacks you!\n")
    if "Laser Cutter" not in item:
        self_print("You feel a bit under-prepared for this,"
                   "what with only having a tiny dagger.\n")
    while True:
        self_print("Would You like to fight or Run away\n"
                  "for fighting press F and for running to field again press R.\n")
        choice2=input("Enter F or R.\n")
        if choice2=='F' or 'f':
            if "Laser Cutter" in item:
                self_print("\nAs the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                self_print("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                self_print("\nBut the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                self_print("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                self_print("\nYou do your best...")
                self_print("but your dagger is no match for the "
                            + option + ".")
                self_print("\nYou have been defeated!\n")
            start_again()
            break
        elif choice2=='R' or 'r':
            self_print("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            choice_menu(item,option)
            break
        else:
            print("WRONG INPUT!\n NOW PLAY AGAIN!\n")
            start_again()

def enter_cave(items,option):
    if "Laser Cutter" in items:
        self_print("\nYou peer cautiously into the cave.")
        self_print("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        self_print("\nYou walk back to the field.\n")
    else:
        self_print("\nYou peer cautiously into the cave.")
        self_print("\nIt turns out to be only a very small cave.")
        self_print("\nYour eye catches a glint of metal behind a "
                    "rock.")
        self_print("\nYou have found the magical Laser Cutter of Ogoroth!")
        self_print("\nYou discard your silly old dagger and take "
                    "the cutter with you.")
        self_print("\nYou walk back out to the field.\n")
        items.append("Laser Cutter")
    choice_menu(items,option)

def start_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        self_print("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        self_print("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        start_again()

def play_game():
    item=[]
    option=random.choice(["dinosaur","witch","anaconda","big spider","pirate"])
    intro(option,item)
    
play_game()
