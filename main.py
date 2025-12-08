import os  # Importing the OS library for file and directory operations

previous = []

def current_path():
    # Returns the current working directory path
    return os.getcwd()

def previous_path(user_input, path_to_save):
    if user_input.lower() in ['yes', 'y']:
        previous.append(path_to_save)
        print(f"Path saved: {path_to_save}")
    else:
        print('Skipped saving the current path.')

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
    save = input("Do you want to save the current path to return later with 'rt'? (yes/y to save): ")
    previous_path(save, current_path())

def play():
    try:
        while True:
            action_type = input(
                'Choose an action:\n'
                'r = Show current path\n'
                'l = List files\n'
                'c = Create folder or text file\n'
                's = Move to another path\n'
                'z = Go back one directory\n'
                'z2 = Go back two directories\n'
                'rt = Return to saved path\n'
                'x = Exit\n'
                'Enter choice: '
            ).lower()

            if action_type == 'r':
                print(f"Current working directory: {current_path()}")
            elif action_type == 'l':
                print(f"Directory contents: {os.listdir(current_path())}")
            elif action_type == 'x':
                print('Exited.')
                break
            elif action_type == 'c':
                file_type = input('Choose type ("f" for folder, "t" for text file): ')
                file_name = input('Enter the name: ')
                create_path(file_type, file_name)
            elif action_type == 's':
                ask_save_path()
                path = input('Enter the path you want to move to: ')
                move_path(os.path.join(current_path(), path))
            elif action_type == 'z':
                ask_save_path()
                os.chdir(os.path.abspath('..'))
            elif action_type == 'z2':
                ask_save_path()
                os.chdir(os.path.abspath('../..'))
            elif action_type == 'rt':
                if not previous:
                    print('No saved path to return to.')
                else:
                    move_path(previous[0])
                    previous.clear()
            else:
                print(f'Unknown command: "{action_type}"')
    except (KeyboardInterrupt, SystemExit):
        print("\nProgram stopped safely.")

play()
