import os  # Importing the OS library for file and directory operations
import time  # making understanding of the text better

previous = []


def current_path():
    # Returns the current working directory path
    return os.getcwd()


def previous_path(path_to_save):
    previous.append(path_to_save)
    print(f"Path saved: {path_to_save}")


def move_path(move_to):
    try:
        os.chdir(move_to)
        print(f'Successfully moved to {move_to}')
    except FileNotFoundError:
        print(f'No such file or directory: {move_to}')


def create_path(path_type, path_name):
    try:
        if path_type.lower() == "f":
            os.mkdir(path_name)
            print(f'Folder "{path_name}" created.')
        elif path_type.lower() == 't':
            created_text_file = os.path.join(os.getcwd(), path_name)
            with open(created_text_file, "w") as f:
                f.write("")  # creates an empty text file
            print(f'Text file "{path_name}" created.')
        else:
            print(f'Incorrect type: {path_type}')
    except FileExistsError:
        print('File or folder already exists. Try a different name.')


def ask_save_path():
    previous_path(current_path())


def play():
    try:
        while True:
            action_type = input(
                'Choose an action:\n'
                'r = Show current path\n'
                'l = List files\n'
                'c = Create folder or text file\n'
                'q = Move to another path\n'
                'z = Go back one directory\n'
                'z2 = Go back two directories\n'
                's = Save current path\n'
                'rt = Return to saved path\n'
                'x = Exit\n'
                'Enter choice: '
            ).lower()

            if action_type == 'r':
                print(f"Current working directory: {current_path()}")
                time.sleep(0.75)
            elif action_type == 'l':
                print(f"Directory contents: {os.listdir(current_path())}")
                time.sleep(1.25)
            elif action_type == 'c':
                file_type = input('Choose type ("f" for folder, "t" for text file): ')
                file_name = input('Enter the name: ')
                create_path(file_type, file_name)
            elif action_type == 'q':
                path = input('Enter the path you want to move to: ')
                move_path(os.path.join(current_path(), path))
            elif action_type == 'z':
                os.chdir(os.path.abspath('..'))
                print('returned back')
                time.sleep(0.5)
            elif action_type == 'z2':
                os.chdir(os.path.abspath('../..'))
                print('returned back 2 times')
                time.sleep(0.5)
            elif action_type == 's':
                ask_save_path()
                time.sleep(0.5)
            elif action_type == 'rt':
                if not previous:
                    print('No saved path to return to.')
                else:
                    move_path(previous[0])
            elif action_type == 'x':
                print('Exited.')
                break
            else:
                print(f'Unknown command: "{action_type}"')

    except (KeyboardInterrupt, SystemExit):
        print("\nProgram stopped safely.")


play()
