# Hex Computer a small python operating system
# Hex Computer is (c) 2017

try:
    import sys
    import os
    from pcdata import errors
    from system import cpu
    from system import data
    from system import apps
    from pcdata import pcin
    from system.pcapps import Terminal
except ImportError:
    print("=============\n"
          "Error 1\n"
          "=============\n")
    print("information:\n"
          "\n"
          "One of Hex Computers Requirements are not installed! or a file is not installed!")
    sys.exit(1)
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

def password():
    return input("Enter password > ").lower().strip()


def restart_mode():
    if INTERACTIVE_MODE:
        input("Press enter to Restart.")
def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")

def pc_info():
    clear_screen()
    print("~~PC~INFO~~")
    print(pcin.OP + pcin.VERSION + pcin.RATE)
    wait()
    desktop()
def desktop():
    clear_screen()
    print("----------------------------------------------CPU [{}]-----".format(cpu.cpupercent))
    print("|--------|\nShutdown       \n|----|\napps   \n|------|\nlogout    \n|-------|\nPC INFO   \n|--------|\nTerminal")
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
    if choice == "pc info":
        pc_info()
    if choice == "Terminal":
        clear_screen()
        print(Terminal.terminal)
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
        wait()
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

