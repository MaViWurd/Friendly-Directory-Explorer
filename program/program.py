import time
import os
import subprocess
import sys
import readline
import termios
import tty

def install_termcolor():
    try:
        subprocess.run(["pip3", "install", "termcolor"])
    except:
        try:
            subprocess.run(["pip", "install", "termcolor"])
        except:
            print("Failed to install termcolor library.")

try:
    from termcolor import colored
except:
    install_termcolor()
    try:
        from termcolor import colored
    except:
        pass

def list_dirs(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return dirs

def change_dir(path, new_dir):
    try:
        os.chdir(os.path.join(path, new_dir))
        print(f"Successfully changed to directory {os.getcwd()}")
    except:
        print(f"Failed to change to directory {new_dir}")

def back_dir(path):
    os.chdir(os.path.dirname(path))
    print(f"Successfully changed to directory {os.getcwd()}")

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        user_input = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if user_input.isdigit():
        return ('number', int(user_input))
    else:
        return ('char', user_input)

def main():
    path = os.getcwd()
    while True:
        os.system('clear')
        print("+-----------------+")
        print("| Current Directory |")
        print("+-----------------+")
        print(colored(f"{os.getcwd()}\n", 'yellow'))
        print("\nSubdirectories:")
        dirs = list_dirs(path)
        for i, d in enumerate(dirs):
            print(f"{i + 1}. {d}")
        print("\nEnter the number of the directory you want to navigate to,")
        print(colored("'b' or 'B' to navigate to the parent directory,", 'red'))
        print(colored("'q' or 'Q' to quit:", 'red'))
        user_input = input().strip()
        user_input = user_input.lower()
        if user_input in ['q', 'b']:
            if user_input == 'b':
                back_dir(path)
            else:
                break
        elif user_input.isdigit():
            try:
                choice = int(user_input)
                if 1 <= choice <= len(dirs):
                    change_dir(path, dirs[choice - 1])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        path = os.getcwd()

    # Set the new working directory before launching a new shell
    os.chdir(path)
    os.system("bash")

if __name__ == '__main__':
    main()
