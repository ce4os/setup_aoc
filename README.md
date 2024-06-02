# AOC setup script V 0.10

### Introduction 

At some point while solving the coding puzzles of Advent of Code, I realized that I was repeating the same tasks over and over again. To automate these repetitive and tedious tasks, I created the script setup.py. This script automates the setup process for solving an Advent of Code puzzle, allowing you to fully focus on solving the puzzle without having to go through the repetitive steps each time. Those steps are:
- downloading the puzzle input and saving it to file
- creating a file for the solution 
    - copying a file with basic utilities to the working directory
    - writing a title and import statements to the solution file
    - providing a path to the puzzle input file

Supposing that you cloned this repo the only thing you need to do before invoking the script is to get the session cookie that is stored after logging in to advent of code. In Chromium this can be done by: 
- login to [Advent of Code](https://adventofcode.com/) 
- right click: inspect 
- navigate to Application 
- Storage -> Cookies -> adventofcode.com 
- copy value 
- paste to line 43: 
SESSION_COOKIE = "session=place-the-value-here"
when you have done so, you can invoke the script with
```python
python3 setup.py
```

### Example

If you provided 2023 as the year and 1 as the day to the cli, the script will create directories like this:

```
/BASE_DIR/
├── Setup/
|   ├── setup.py
│   ├── utils.py
│   ├── README.md
|   ├── .gitignore
|   └── .git
└── 2023/
    ├── day1.py
    ├── utils.py
    └── src/
        └── day1_input
```

### Addendum

As indicated by the version number, this is an ongoing project. I plan to modularize the script,
make it possible to invoke the script with arguments, refactor the code, write tests and so on. For now, it does the trick but development never really stops.

### Issues

If you experience issues, please message me:
ce4os@proton.me