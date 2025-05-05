from Modules.file_handling import print_files
from Modules.suspected_files import log_suspicious_files, mark_as_safe
from Modules.directory_handling import directory_stats
from Modules.file_removing import remove_suspected_files

def print_menu(dir_name:str) -> None:
    """
    Function that prints the menu options to the user
    :param: dir_name: The name of current directory
    :return: Nothing
    """
    print("Choose an action (1-6):\n"
          "1 - Scan all files in a directory and show files details\n"
          f"2 - Create a log file with all suspected files details in '{dir_name}'\n"
          f"3 - Mark a file as safe (will not be scanned in future scans) in '{dir_name}'\n"
          f"4-  Show statistics of files in '{dir_name}'\n"
          f"5 - Delete all suspected files in '{dir_name}'\n"
          "6 - Exit the program")

def user_choices(dir_path:str, dir_name:str, safe_list:dict, names_path:str, extensions_path:str, proj_path:str) -> None:
    """
    Function that handles the user choice and performs the correct action according to the user input
    :param dir_path: The directory path to scan files from
    :param dir_name: The directory name entered by the user
    :param safe_list: The list of safe files (to not scan)
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param proj_path: The project path
    :return: Nothing
    """

    # While the user still hasn't exited the program (6th option)
    while True:
        try:
            user_action = int(input("Enter the operation number: "))
        except ValueError:
            print("Invalid operation, enter a number")
            continue

        if user_action == 1:
            dir_name = input("Enter directory name to scan (files_to_scan or another_dir): ")
            dir_path = f"{proj_path}/{dir_name}"
            print_files(dir_path, safe_list)

            # Printing the menu to the user
            print_menu(dir_name)

        elif user_action == 2:
            log_suspicious_files(dir_path, names_path, extensions_path, safe_list, proj_path)
            print("Success! Suspected files info written into a log file")

        elif user_action == 3:
            mark_as_safe(dir_path, safe_list)

        elif user_action == 4:
            directory_stats(dir_path, names_path, extensions_path, safe_list, dir_name)

        elif user_action == 5:
            remove_suspected_files(dir_path, names_path, extensions_path, safe_list)

        elif user_action == 6:
            print("Goodbye!")
            break




def menu(safe_list:dict, names_path:str, extensions_path:str, proj_path:str) -> None:
    """
    The menu that the user will be working with and presented with
    :param proj_path: The project path
    :param safe_list: The list of safe files (to not scan)
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :return: Nothing
    """
    try:
        # Automatically going to the first option upon loading the program
        dir_name = input("Enter directory name to scan (files_to_scan or another_dir): ")
        dir_path = f"{proj_path}/{dir_name}"

        # Printing the info of the files
        print_files(dir_path, safe_list)

        # Printing the menu to the user
        print_menu(dir_name)

        # Handling user action
        user_choices(dir_path,dir_name,safe_list,names_path,extensions_path, proj_path)

    except ValueError:
       raise ValueError("The operation must be an integer")

