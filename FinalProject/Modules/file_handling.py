import os

def get_all_files_info(dir_path:str) -> dict:
    """
    Returning a dictionary containing the relevant info of all files
    :param dir_path: The directory path to scan files from
    :return: Files dictionary containing the relevant info
    """
    try:

        files_dict = {} # The dictionary that will be returned

        files = os.listdir(dir_path) # List of all file names in current directory(with extension)

        for file in files:
            file_path = os.path.join(dir_path, file) # File path

            # If it's a file and not a directory
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path) # File size
                file_name = os.path.splitext(file)[0] # File name
                file_extension = os.path.splitext(file)[1].lstrip('.') # File extension

                # Adding the file to the dictionary
                files_dict[file] = {"name": file_name, "extension": file_extension, "size": file_size}

        return files_dict

    except FileNotFoundError:
        raise FileNotFoundError(f"Directory Not Found: {dir_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {dir_path}")


def get_suspected_files_info(dir_path:str, safe_list:dict) -> dict:
    """
    Returning a dictionary containing the relevant info of non-safe files
    :param safe_list: The list of safe files (to not scan)
    :param dir_path: The directory path to scan files from
    :return: Files dictionary containing the relevant info
    """
    try:

        files_dict = get_all_files_info(dir_path)

        suspected_files_dict = {}

        for key, value in files_dict.items():
            # If the file hasn't been marked as safe
            if (dir_path in safe_list.keys() and key not in safe_list[dir_path]) or dir_path not in safe_list.keys():
                suspected_files_dict[key] = value

        return suspected_files_dict

    except FileNotFoundError:
        raise FileNotFoundError(f"Directory Not Found: {dir_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {dir_path}")


def get_safe_files_info(dir_path: str, safe_list: dict) -> dict:
    """
    Returning a dictionary containing the relevant info of safe files
    :param safe_list: The list of safe files (to not scan)
    :param dir_path: The directory path to scan files from
    :return: Files dictionary containing the relevant info
    """
    try:

        files_dict = get_all_files_info(dir_path)

        safe_files_dict = {}

        for key, value in files_dict.items():
            # If the file has been marked as safe
            if dir_path in safe_list.keys() and key in safe_list[dir_path]:
                safe_files_dict[key] = value

        return safe_files_dict


    except FileNotFoundError:
        raise FileNotFoundError(f"Directory Not Found: {dir_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {dir_path}")

def print_files(dir_path:str, safe_list:dict) -> None:
    """
    Printing the relevant info of all files_to_scan in a given directory
    :param dir_path: The path of the directory that was scanned
    :param safe_list: The list of safe files (to not scan)
    :return: Nothing
    """
    files_dict = get_suspected_files_info(dir_path, safe_list)

    # Printing the files to the user
    print(f"Found {len(files_dict)} files:")
    for key, value in files_dict.items():
        print(f"--------------{key}---------------\nFile name: {value['name']}\nFile Extension: {value['extension']}\nFile Size: {value['size']}\n--------------{'-'*len(key)}---------------")

def get_names_in_list(file_path: str) -> list:
    """
    Reads the document of all  names and returns it in a list.
    :raise: FileNotFoundError if the file path does not exist
    :raise: PermissionError if the user does not have permissions to read from this file
    :raise: OSError if the file path input is not a string
    :return: list of all names
    """

    try:
        with open(file_path, 'r') as names:
            return names.read().split()
    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file doesn't exist: {file_path}")
    except PermissionError:
        raise PermissionError("You don't have permission to read from the file")
    except OSError:
        raise OSError("The names file path must be a string of a path")

