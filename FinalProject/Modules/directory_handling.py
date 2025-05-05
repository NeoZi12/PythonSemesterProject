from Modules.suspected_files import danger_files_dict
from Modules.file_handling import get_suspected_files_info


def get_extensions_amount(files_dict) -> int:
    """
    Function that returns the amount of extensions without duplicates
    :param files_dict: The dictionary which contains all scanned files info
    :return: the amount of extensions without duplicates
    """

    # All extensions
    extension_list = [value['extension'] for key, value in files_dict.items()]

    # Returning the amount without duplicates
    return len(set(extension_list))

def print_largest_smallest_file(files_dict) -> None:
    """
    Prints the largest and smallest files in the directory
    :param files_dict: The dictionary which contains all scanned files info
    :return: Nothing
    """
    files_size_list = [value['size'] for key, value in files_dict.items()] # The file size list
    largest_file_size = max(files_size_list) # Largest file size
    smallest_file_size = min(files_size_list) # Smallest file size

    print(f"Largest files ({largest_file_size} Bytes):")
    for key, value in files_dict.items():
        if value['size'] == largest_file_size: # Found the largest file
            print(key)

    print(f"Smallest files ({smallest_file_size} Bytes):")
    for key, value in files_dict.items():
        if value['size'] == smallest_file_size: # Found the smallest file
            print(key)

def directory_stats(dir_path:str, names_path:str, extensions_path:str, safe_list:dict, dir_name:str) -> None:
    """
    Function that prints to the user statistics about the last scanned directory

    :param dir_path: The path of the directory that was scanned
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param safe_list: The list of safe files (to not scan)
    :param dir_name: The directory name
    :return: Nothing
    """

    files_dict = get_suspected_files_info(dir_path, safe_list)

    # Getting statistics about the directory
    file_amount = len(files_dict)
    suspected_files = danger_files_dict(dir_path, names_path, extensions_path, safe_list)
    suspected_file_amount = len(suspected_files)
    extension_amount = get_extensions_amount(files_dict)

    # Printing the statistics
    print(f"Total files in '{dir_name}': {file_amount}")
    print(f"Total suspected files in '{dir_name}': {suspected_file_amount}")
    print(f"Total unique extensions in '{dir_name}': {extension_amount}")

    if file_amount != 0:
        print_largest_smallest_file(files_dict)
