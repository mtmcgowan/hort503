# EXERCISE 10: What Was That?
print("")
print("Exercise 10: What Was That?")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Study Drills

# 1. Memorize all the escape sequences by putting them on flash cards.
# Skipped

# 2. Use ''' instead. Can you see why you might use that instead of """?
# Easier to type, also may help avoid requiring as many escape sequences for nested double-quotes

# 3. Combine escape sequences and format strings to create a more complex format.
# Define a time format
my_time = "{}/{}/{}, {}:{}:{}"

# Assign variables for a moment in time
day = 20
month = 1
year = 2018
hour = 10
minute = 22
second = 10

# Print the stored time in the specified custom format
print(my_time.format(day, month, year, hour, minute, second))