import os
import requests
import re

from dotenv import load_dotenv
from pathlib import Path
from shutil import copyfile
from cli import get_user_input


# Interactive CLI - get year and day to setup
print("\n-----------Advent of code setup V.0.0.1-----------\n")

## Settings
load_dotenv()
day, year = get_user_input()   
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
BASE_DIR = Path(__file__).resolve().parent.parent
SETUP_DIR = BASE_DIR / "setup_aoc"
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
