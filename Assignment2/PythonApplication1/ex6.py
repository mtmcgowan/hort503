# EXERCISE 6: Strings and Text
print("")
print("Exercise 6: Strings and Text")

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# Study Drills
# 1. Go through this program and write a comment above each line explaining it.
print("")
print("Exercise 6: Strings and Text")

# Assign a variable as an integer
types_of_people = 10
# Assign a variable as a formatted string
x = f"There are {types_of_people} types of people."
# Assign a variable as a string
binary = "binary"
# Assign a variable as a string
do_not = "don't"
# Assign a variable as a formatted string using multiple keyword arguments
y = f"Those who know {binary} and those who {do_not}."

# Print the strings stored in x and y
print(x)
print(y)

# Print two formatted strings with keyword arguments. The second keyword is nested in single quotes, which are also printed.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assign a boolean
hilarious = False
# Assign a string with an empty keyword argument
joke_evaluation = "Isn't that joke so funny?! {}"
# Print a string using a variable suffix '.format', which fills in keywords with the value stored in the 'hilarious' variable.
print(joke_evaluation.format(hilarious))

# Assign two strings
w = "This is the left side of..."
e = "a string with a right side."

# Use the addition operator on two strings to concatenate them.
print(w + e)

# 2. Find all the places where a string is put inside a string. There are four places.
# From the textbook, lines 2,6,11,12. Line 17 puts a string coerced boolean inside a string.

# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# Don't be annoying. Nobody likes learning from annoying teachers....

# 4. Explain why adding the two strings w and e with + makes a longer string.
# The + operator is overloaded so that when two strings are used as arguments, they are concatenated.