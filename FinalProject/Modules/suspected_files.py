from Modules.file_handling import get_suspected_files_info, get_names_in_list, get_all_files_info

import os
import time
import base64

def danger_files_dict(dir_path:str, names_path:str, extensions_path:str, safe_list:dict) -> dict:
    """
    Function that scans all files in a directory and returns the information of dangerous files
    :param dir_path: The name of the directory to scan its files_to_scan
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param safe_list: The list of safe files (to not scan)
    :return: the information of suspicious files as a dictionary
    """

    files_dict = get_suspected_files_info(dir_path, safe_list) # The files that the function will look for danger in
    names_list = get_names_in_list(names_path) # List of all suspicious names
    extension_list = get_names_in_list(extensions_path) # List of all suspicious extensions

    dangerous_files = {}

    # Going through each non-safe file and checking it's danger level
    for key, value in files_dict.items():
        danger_level = 0
        if value['name'] in names_list:
            danger_level += 1

        if value['extension'] in extension_list:
            danger_level += 1

        if value['size'] > 10000000:
            danger_level += 1

        # If the file was found as dangerous - add it to the dictionary of dangerous files
        if danger_level > 0:
            dangerous_files[key] = {
                "name": value['name'],
                "extension": value['extension'],
                "size": value['size'],
                "danger_level": danger_level
            }

    return dangerous_files

def log_suspicious_files(dir_path:str, names_path:str, extensions_path:str, safe_list:dict, proj_path:str) -> str:
    """
    Function that detects suspicious files in a given directory and writes their information into a log file
    :param dir_path: The path of the directory that was scanned
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param safe_list: The list of safe files (to not scan)
    :param proj_path: The project path
    :return: The Data that was written to the file
    """

    # Getting the timestamp and the salt
    unix_timestamp = int(time.time())
    salt = base64.urlsafe_b64encode(os.urandom(48)).decode('utf-8')

    # Name of the log file
    log_name = str(unix_timestamp)+salt

    # The data that will be written into the log file
    data_to_write = danger_files_dict(dir_path, names_path, extensions_path, safe_list)

    try:
        with open(f"{proj_path}/log_files/{log_name}.log", "w") as f:
            for key,value in data_to_write.items():
                f.write(
                    f"--------------{key}---------------\n"
                    f"File name: {value['name']}\n"
                    f"File Extension: {value['extension']}\n"
                    f"File Size: {value['size']} Bytes\n"
                    f"Danger Level: {value['danger_level']}\n"
                    f"--------------{'-'*len(key)}---------------\n")
    except FileNotFoundError:
        raise FileNotFoundError("Cant log file, file not found")
    except PermissionError:
        raise PermissionError("Cant log file, no permissions")
    except OSError:
        raise OSError(f"OSError: {log_name}")


    return log_name



def mark_as_safe(dir_path:str, safe_list:dict) -> None:
    """
    Function that gets a file name from the user and marks it as a safe file
    :param dir_path: the directory to mark the safe file from
    :param safe_list: The list of safe files (to not scan)
    :return: Nothing
    """

    # Getting the files information and the file to mark as safe
    files_dict = get_all_files_info(dir_path)
    safe_file = input("Enter a file name you would like to mark as safe: ")

    # If the file exists in the directory
    if safe_file in files_dict.keys():
        # If the file directory already contains a safe file
        if dir_path in safe_list.keys():
            # If the file to mark as safe hasn't already been marked as safe in this directory
            if safe_file not in safe_list[dir_path]:
                safe_list[dir_path].append(safe_file) # appending the safe file to the safe file list of this directory
                print(f"'{safe_file}' has been marked as safe")
            # If the file has already been marked as safe display a message
            else:
                print(f"'{safe_file}' already has been marked as safe")
        # If a file has yet to be marked as safe in the current directory - create a list and add the first file to be marked as safe
        else:
            safe_list[dir_path] = [safe_file]
            print(f"'{safe_file}' has been marked as safe")

    # If the file to mark as safe doesn't exist in this directory
    else:
        print(f"The file '{safe_file}' doesn't exist in the directory '{dir_path}'")

    # Printing safe list updated state
    print(f"Updated safe list: {safe_list}")



