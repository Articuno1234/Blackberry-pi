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

c = ["Heads won! ()", "Tails won |~~"]
r = ["Heads was chosen", "Tails was chosen"]
def h_t():
    clear_screen()
    print("~~~Heads or tails~~~\n"
          "Welcome to Heads or tails\n"
          "For Blackberry pi.\n"
          "\n Choose"
          "\nheads \n Tails\n Random")
    choice = user_choice()
    if choice == "heads":
        clear_screen()
        print("Heads was chosen!")
        wait()
        print("{}".format(random.choice(c)))
        wait()
        multi_game()
    if choice == "tails":
        clear_screen()
        print("Tails was chosen!")
        wait()
        print("{}".format(random.choice(c)))
        wait()
        multi_game()
    if choice == "random":
        clear_screen()
        print("{}".format(random.choice(r)))
        wait()
        print("{}".format(random.choice(c)))
        wait()
        multi_game()
def multi_game():
     clear_screen()
     print("~~~Multi-game Version {}~~~".format(dtadata.VERSION))
     print("1. dice")
     print("2. heads or tails")
     print("0. exit")
     choice = user_choice()
     if choice == "1":
         clear_screen()
         dice()
     if choice == "2":
         h_t()
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
