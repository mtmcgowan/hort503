# Import the argv library from sys
from sys import argv
# Assign the provided argument to the filename variable
script, filename = argv

# Open filename and assign it to txt
txt = open(filename)

# Print the filename
print(f"Here's your file {filename}:")
# Print the output of the txt.read() function. This is the text in the file.
print(txt.read())

# Print a string prompt.
print("Type the filename again:")
# Propmt the user and assign the input to the file_again variable
file_again = input("> ")

# Open the filename assigned to the file_again variable
txt_again = open(file_again)

# Print the txt contents of file_again
print(txt_again.read())

txt.close()
txt_again.close()

# Study drills
# 1. Above each line, write out in English what that line does.
# Done

# 2. If you are not sure.....
# Ok

# 3. I used the word...
# Ok

# 4. Get rid of lines 10-15 where you use input and run the script again.
# Ok saved uner 'ex15_sd4.py'. It gets rid of the prompt and return part.

# 5. Use only input and try the script that way. Why is one way of getting the filename better than another?
# Using the system argument is faster, but input makes it more interactive.

# 6. Start python3.6 to start the .....
# Yea ok.

# 7. Have your script also call close() on the txt and txt_again variables. It's important to close files when you are done with them.
# Ok.