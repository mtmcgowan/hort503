# EXERCISE 3: Numbers and Math
print("")
print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Study Drills
# 1. Above each line, use the # to write a comment to yourself explaining what the line does.
# Actually, commenting EVERY line is a bad style to use and is unnecessary to convey to a reader what the code is doing.
# Instead it is better to comment blocks of code that group together for a specific purpose and comment the block.

# 2. Remember in Exercise 0 when you started python 3.6? Start it and use Python as a calculator.
# Done

# 3. Find something you need to calculate and write a new .py file that does it.
# Instead, I will perform calculations here so I can keep my coding script consolidated in a single .py file:
print("The integer remainder of 564/56:", 564%56)

# 4. Rewrite ex3.py to use floating point numbers so it's more accurate. 20.0 is floating point
# Technically, Python 3 appears to be using "true division" even when an operand is applied to two integer values.
# Furthermore, the more technical way to 'force' floating point division on an integer is to coerce it:
print("The integer quotient of 564/56:", float(564)/56)