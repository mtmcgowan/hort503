people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# Study Drill

# 1. What do you think the if does to the code under it?
# It runs the indented code if the argument equates to True

# 2. Why does the code under the if need to be indented four spaces?
# Because Python does not use brackets and uses indents instead.

# 3. What happens if it isn't indented?
# The code is no longer in the statement block and can cause erratic behavior (and may fail to compile)

# 4. Can you put other boolean expressions from....
# Yea, sure.
cats = 10
dogs = 10
if dogs == cats:
    print("There is balance in the fur-se.")
if cats > dogs:
    print("Snack time!")
