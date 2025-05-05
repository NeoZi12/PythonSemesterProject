def safe_files_size(dir_name:str, safe_list:list, proj_path:str) -> None:
    """
    Function that prints sizes in MB of safe files
    :param dir_name: the directory to mark the safe file from
    :param safe_list: The list of safe files (to not scan)
    :param proj_path: The project path
    :return: Nothing
    """

    files_dict = get_all_files_info(dir_name,proj_path)

    for key, value in files_dict.items():
        if key in safe_list:
            file_size = round(value["size"]/1000000, 2)
            print(f"{key}: {file_size} MB")

def file_amount_sus_extensions(dir_name:str, names_path:str, extensions_path:str, safe_list:list, proj_path:str) -> None:
    """
    Function that prints suspicious extensions amount of files
    :param dir_name: the directory to mark the safe file from
    :param names_path: the path of suspicious names txt file
    :param extensions_path: the path of suspicious extensions txt file
    :param safe_list: The list of safe files (to not scan)
    :param proj_path: The project path
    :return: Nothing
    """

    suspected_files = suspected_files_dict(dir_name, names_path, extensions_path, safe_list, proj_path)

    extension_list = [value['extension'] for key, value in suspected_files.items()]

    for extension in set(extension_list):
        print(f".{extension}: {extension_list.count(extension)} files")
