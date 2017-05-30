import sys
import os
from system import data
from system import apps
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

def restart_mode():
    if INTERACTIVE_MODE:
        input("Press enter to Restart.")
def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")

def log_on():
    if INTERACTIVE_MODE:
        input("Press enter to Login!.")
def desktop():
    clear_screen()
    print("---------------------------------------------------\n")
    print("|--------|\nShutdown       \n|----|\napps   \n|------|\nlogout")
    choice = user_choice()
    if choice == "shutdown":
        if INTERACTIVE_MODE:
            input("Press enter to Shutdown!")
    if choice == "apps":
        clear_screen()
        print(apps.INTRO)
        print(apps.APPS)
        wait()
        desktop()
    if choice == "logout":
        sysmenu()

def sysmenu():
     clear_screen()
     print("===============\n"
           "Hex Computer\n"
           "===============\n")
     print("Welcome {}".format(data.USER))
     print("login")
     print("\nRestart")
     print("\nShutDown")
     choice = user_choice()
     if choice == "login":
        log_on()
        desktop()
     if choice == "restart":
        restart_mode()
        sysmenu()
        print("Restarted!")
     if choice == "shutdown":
        if INTERACTIVE_MODE:
            input("Press enter to Shutdown!")
sysmenu = sysmenu()
print(sysmenu)

