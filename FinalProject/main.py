from Modules.menu import menu
import os

def main() -> None:
    """
    This is the main function
    :return: Nothing
    """

    # The safe list(dictionary) that we will be marking safe files in
    safe_list = {}

    # The project path
    proj_path = os.path.dirname(os.path.abspath(__file__))

    # The path of suspicious names text file
    names_path = os.path.join(proj_path, "suspicious_file_names.txt")
    # The path of suspicious extensions text file
    types_path = os.path.join(proj_path, "suspicious_file_types.txt")


    try:
        menu(safe_list, names_path, types_path, proj_path)
    except BaseException as m:
        print(f"Error: {m}")

if __name__ == "__main__":
    main()
