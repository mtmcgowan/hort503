# EXERCISE 8: Printing, Printing
print("")
print("Exercise 8: Printing, Printing")
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Study Drills

# 1. Comment what each line does. (I commented blocks of similar code)
# Define a string with a particular format
formatter = "{} {} {} {}"

# Print a formatted string with different types of arguments
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# Recursively use the string format as the arguments for a format function call
print(formatter.format(formatter, formatter, formatter, formatter))

# Use longer strings as arguments for the format function
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))