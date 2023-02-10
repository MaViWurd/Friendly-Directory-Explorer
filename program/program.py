import os
import subprocess

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

def main():
    path = os.getcwd()
    while True:
        os.system('clear')
        print(colored(f"Current directory: {path}", 'yellow'))
        print("\nSubdirectories:")
        dirs = list_dirs(path)
        for i, d in enumerate(dirs):
            print(f"{i + 1}. {d}")
        print("\nEnter the number of the directory you want to navigate to,")
        print(colored("'b' to navigate to the parent directory,", 'red'))
        print(colored("'q' to quit:", 'red'))
        user_input = input()
        if user_input == 'q':
            break
        elif user_input == 'b':
            back_dir(path)
        else:
            try:
                choice = int(user_input)
                if 1 <= choice <= len(dirs):
                    change_dir(path, dirs[choice - 1])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        path = os.getcwd()

if __name__ == '__main__':
    main()
