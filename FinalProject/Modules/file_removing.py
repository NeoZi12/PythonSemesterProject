import os
from Modules.suspected_files import danger_files_dict

def confirm_and_remove(files_list, suspected_files, dir_path) -> None:
    """
    Function that get confirmation from the user and deletes the suspected files
    :param files_list: the list of files in the directory
    :param suspected_files: the suspected files
    :param dir_path: the path to delete the files in
    :return: Nothing
    """

    # Confirmation by the user of performing this action
    user_confirm = input("Are you sure you want to delete all suspected files? (Y/N): ")

    if user_confirm == 'Y':
        try:
            for file in files_list:
                file_path = f"{dir_path}/{file}"
                if os.path.isfile(file_path) and file in suspected_files:
                    os.remove(file_path)
                    print(f"File removed: {file}")


        except FileNotFoundError:
            print(FileNotFoundError(f"File not found"))
        except PermissionError:
            print(PermissionError(f"No permissions to remove file"))
        except OSError:
            print(OSError(f"The file to remove must be a file format"))


def remove_suspected_files(dir_path:str, names_path:str, extensions_path:str, safe_list:dict) -> None:
    """
    Function that removes all the suspected files from a directory
    :param dir_path: The directory path to scan files from
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param safe_list: The list of safe files (to not scan)
    :return: Nothing
    """

    # Getting the files list of the current directory
    files = os.listdir(dir_path)

    # Getting the suspected files
    suspected_files = danger_files_dict(dir_path, names_path, extensions_path, safe_list)

    # Deleting the suspected files with user confirmation
    confirm_and_remove(files, suspected_files, dir_path)