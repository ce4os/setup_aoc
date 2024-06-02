import os
import requests
import re

from pathlib import Path
from shutil import copyfile


# Interactive CLI - get year and day to setup
print("\n-----------Advent of code setup V.0.0.1-----------\n")
while True:
    # Getting input for day
    day = input("Which day to setup: ")
    year = input("For which year: ")

    # Check input
    if not day.isdigit() or not year.isdigit():
        print("Invalid input. Day and year must be numeric")
        print("Try again")
        continue
    elif int(day) > 25 or int(day) < 0:
        print("Advent calenders go from 1st of Dec to 25th of Dec\nTry again")
        continue
    elif int(year) < 2015 or int(year) > 2023:
        print("Advent of code has puzzles for the years 2015-2023")
        continue
    else:
        print("Selected day: ", day)
        print("Selected year: ", year)

    # Confirming input    
    proceed = input("Proceed [y,n]? ")
    if proceed.lower() == "y":
        break
    elif proceed == "n":
        print("Exiting")
        exit()
    if proceed != "y":
        print("Aborting...")
        continue
    
# Defining paths
SESSION_COOKIE = "session=put-your-session-cookie-here"
BASE_DIR = Path(__file__).resolve().parent.parent
SETUP_DIR = BASE_DIR / "Setup"
YEAR_DIR = BASE_DIR / year
SRC_DIR = BASE_DIR / YEAR_DIR / "src/"
PATH_DAY = YEAR_DIR / f"day{day}.py"
PATH_INPUT = SRC_DIR / f"day{day}_input"

# Create BASE_DIR/<year> and BASE_DIR/<year>/src/ if not exists
try:
    os.makedirs(SRC_DIR)
except:
    FileExistsError
    print("Directories already exists. Omitting...")

## Creating Files

# 0. Writing utilities to BASE_DIR/<year>
try:
    copyfile(SETUP_DIR / "utils.py", YEAR_DIR / "utils.py")
except FileExistsError:
    print("Utility file already exists. Omitting...")

# 1. solution and src file

# construct URLs
url_puzzle_input = f"https://adventofcode.com/{year}/day/{day}/input"
url_puzzle_description = f"https://adventofcode.com/{year}/day/{day}"

# construct request header
headers = {
    'cookie': SESSION_COOKIE
}

# 1.1 source file

# GET request for puzzle input
response = requests.get(url_puzzle_input, headers=headers)
if response.status_code == 500:
    print("500 internal Server Error.\nDid you forget to put in the session cookie?")

# process response
puzzle_input = response.content.decode()

# write to file
try: 
    with open(SRC_DIR / f"day{day}_input", "w") as file:
        file.write(puzzle_input)
except FileExistsError:
    print("Source file already exists. Omitting...")

# 1.2 Solution file

# GET request for puzzle_description
response = requests.get(url_puzzle_description, headers=headers)
if response.status_code != 200:
    print("500 internal Server Error.\nDid you forget to put in the session cookie?")

# Getting hold of the title
pattern = "--- Day \d+:[0-9a-zA-Z ]*---"
title = re.search(pattern, response.content.decode()).group()

try:
    with open(PATH_DAY, "w") as file:
        file.write(f"#{title}\n\n# Setup\nfrom utils import get_puzzle_input_as_list\npath_to_puzzle_input = 'src/day{day}_input'")
except BaseException as err:
    print("An unexpected error has occured\n", err)
