## Utility functions for getting puzzle input

def get_puzzle_input_as_string(path_to_puzzle_input: str) -> str:
    """Returns content of file as a single string"""
    try:
        with open(path_to_puzzle_input) as f:
            content = f.read()
    except FileNotFoundError as err:
        print(err)
    return content

def get_puzzle_input_as_list(path_to_puzzle_input: str) -> list:
    """Returns content of a file as a list of strings one string per line"""
    try:
        with open(path_to_puzzle_input) as f:
            content = f.readlines()
    except FileNotFoundError as err:
        print(err)
    return content