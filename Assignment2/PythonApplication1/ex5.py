# EXERCISE 5: More Variables and Printing
print("")
print("EXERCISE 5: More Variables and Printing")
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Study Drills
# 1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
print("")
print("EXERCISE 5: More Variables and Printing")
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do no just type in the measurements. Work out the math in Python.
weight_lb = 155
weight_kg = -1
height_in = 69
height_cm = -1

weight_kg = weight_lb /2.2046
height_cm = height_in * 2.54

print(f"My weight in pounds: {weight_lb}")
print(f"My weight in kilograms: {weight_kg}")
print(f"My height in inches: {height_in}")
print(f"My height in centimeters: {height_cm}")