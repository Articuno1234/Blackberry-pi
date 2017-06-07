# Do not edit!
import sys
import os
import random
import dtadata

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def user_choice():
    return input("> ").lower().strip()

def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
bef = ["You roled a", "O.O"]
nums = ["1", "2", "3", "4", "5", "6"]
aft = ["Well done!", "wow!", "Hurray"]
def dice():
     print("~~~Multi-game - Dice~~~\n")
     wait()
     print("{} {} {}".format(random.choice(bef), random.choice(nums), random.choice(aft)))
     wait()
     multi_game()

def multi_game():
     clear_screen()
     print("~~~Multi-game Version {}~~~".format(dtadata.VERSION))
     print("1. dice")
     print("0. exit")
     choice = user_choice()
     if choice == "1":
         clear_screen()
         dice()
     if choice == "0":
         if IS_WINDOWS:
             clear_screen()              
             print("Sorry we can not exit you to desktop() exit for windows is comming soon!")
             sys.exit(1)
         if IS_MAC:
             clear_screen()
             print("Sorry we can not exit you to desktop() exit for Mac is comming soon!")
             sys.exit(1)
         else:
             clear_screen()
             print("Sorry we can not exit you to desktop() exit for Linux/Ubuntu/etc. comming soon!")
             sys.exit(1)
