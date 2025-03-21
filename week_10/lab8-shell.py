from colorama import Fore
from pathlib import Path

"""
You are writing a shell (a terminal program that interacts with your file system)

The shell accepts the following commands:
    ls      list files/folders
    touch   create a file
    mkdir   create a folder
    cat     output the contents of a file
    mv      rename/move a file

NOTE: all commands are expected to be run from the directory where the file is located, i.e. the current working directory. You *should not* be navigating to new directories programmatically

- You must use pathlib for all functions (no os module)
- You must use try/except to gracefully recover from any errors
- The script can only be stopped using ctrl-c, but must not print errors
- No generic Exceptions allowed

Last but not least - if you are trying this 'advanced' version I highly recommend trying to figure it out by slogging through documentation on pathlib (e.g. https://docs.python.org/3/library/pathlib.html - check out the list of Methods and properties of Pure Path on the left-hand side of the page) instead of using ChatGPT for starter code. Reading documentation will be a necessary part of your life as a software developer, and the more skilled you get at parsing it the better off you'll be. 
"""

def ls(arguments):
    # if ls is called with 0 arguments, the current directory is listed
    # if ls is called with 1 argument, the specified directory is listed
    pass

def touch(arguments):
    pass

def mkdir(arguments):
    pass

def cat(arguments):
    pass

def mv(arguments):
    pass

def parse(line):
    commands = {
        'ls':    { 'function': ls, 'min_args': 0 },
        'touch': { 'function': touch, 'min_args': 1 },
        'mkdir': { 'function': mkdir, 'min_args': 1 },
        'cat':   { 'function': cat, 'min_args': 1 },
        'mv':    { 'function': mv, 'min_args': 1 },
    }

    """
    Multiple statements are allowed on one line if separated with &&

    Separate the command from the arguments

    Ensure that the number of arguments is at least the value specified by min_args (print an error in red if not)

    Ensure that the command is valid (print an error in red if not)

    If all checks succeed, run the function(s) associated with the command(s)
    """

def loop():
    # repeatedly prompt the user for input
    # if the input is not blank, parse() it
    pass # remove

if __name__ == '__main__':
    loop()