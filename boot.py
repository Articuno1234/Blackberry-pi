# Hex Computer a small python operating system
# Hex Computer is (c) 2017

try:
    import subprocess
    import sys
    import os
    import dta
    import dtadata
    from system import cpu
    from system import data
    from system import apps
    from pcdata import pcin
except ImportError:
    print("=============\n"
          "Error 1\n"
          "=============\n")
    print("information:\n"
          "\n"
          "One of Hex Computers Requirements are not installed! or a file is not installed!")
    subprocess.call(("pip3", "install", "sys"))
    subprocess.call(("pip3", "install", "os"))
    subprocess.call(("sudo", "apt-get", "install", "beep"))
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

def login(menu=True):
     clear_screen()
     print("=============================\n"
           "=                           =\n"
           "=     Blackberry pi         =\n"
           "=                           =\n"
           "=   Welcome {}           =\n"
           "=                           =\n"
           "=============================\n".format(data.USER))
     if INTERACTIVE_MODE:
        input("/ ")
     desktop()
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
    print("|--------|\nShutdown       \n|----|\napps   \n|------|\nlogout    \n|-------|\nPC INFO       \n|-----|\nmulti-game\n       |------|\npython")
    choice = user_choice()
    if choice == "shutdown":
        if INTERACTIVE_MODE:
            input("Press enter to Shutdown!")
        clear_screen()
        sys.exit(1)
    if choice == "multi-game":
        multi = dta.multi_game()
        print(multi)
    if choice == "python":
        clear_screen()
        print("~~Python3 Terminal~~")
        subprocess.call(("python3"))
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

whatsnew = "+ Added python3 Terminal\n Added New Login screen\n "
def changelog():
     clear_screen()
     print("=--------------=\n"
           "=  Change log  =\n"
           "=--------------=\n")
     print("{}".format(whatsnew))
     wait()
     sysmenu()
def sysmenu():
     clear_screen()
     print("===============\n"
           "Blackberry pi\n"
           "===============\n")
     print("Welcome {}\n".format(data.USER))
     print("login")
     print("\nRestart")
     print("\nShutDown")
     print("\nUpdate")
     choice = user_choice()
     if choice == "login":
        wait()
        login(menu=True)
     if choice == "restart":
        restart_mode()
        sysmenu()
        print("Restarted!")
     if choice == "shutdown":
        if INTERACTIVE_MODE:
            input("Press enter to Shutdown!")
        clear_screen()
        sys.exit(1)
     if choice == "update":
         subprocess.call(("git", "clone", "https://github.com/Articuno1234/Blackberry-pi"))
         print("Done!")
         wait()
         sysmenu()

changelog = changelog()
print(changelog)
