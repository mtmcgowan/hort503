# Import the argv library
from sys import argv

# Unpack arguments
script, input_file = argv

# Define a function that prints an entire file
def print_all(f):
    print(f.read())

# Define a function that sets a file position to the beginning of the file
def rewind(f):
    f.seek(0)

# Define a function that prints a particular line in a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Call the functions using different strategies
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Study Drills

# 1. Comment the script
# 2. Done

# 2. Each time print_a_line is run, you are passing.....

current_line = 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)

current_line = current_line + 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)

current_line = current_line + 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)

# 3. Find each place....
# OK

# 4. Research online what the seek function for file does....
# Seek sets the current position in a file to a given position. 0 sets it to the beginning.

# 5. Research the shorthand notation +=, and rewrite the script to use += instead.
# x += 2 is equivalent to x = x + 2
current_line = 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)

current_line += 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)

current_line += 1
print("The current line is {current_line}")
print_a_line(current_line, current_file)
