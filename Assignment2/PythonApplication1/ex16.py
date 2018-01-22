from sys import argv

script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

# Study Drills

# 1. If you do not understand this....
# I understand.

# 2. Write a script similar to the last exercise....
# Saved as ex16_sd2.py

# 3. Theres too much repetition in this file.....
# Saved as ex16_sd3.py

# 4. Find out why we had to pass a 'w' as an extra parameter to open.
# This makes it available for 'writing'

# 5. If you open the file with 'w' mode, then do you really need the target.truncate()?
# Technically no. Truncation is automatically done if 'w' is used

