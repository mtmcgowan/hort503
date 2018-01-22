# EXERCISE 4: Variables and Names
print("")
print("EXERCISE 4: Variables and Names")
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills

# The error indicates that the variable 'car_pool_capacity' called in line 8 was not defined yet. This is because 'carpool_capacity' is character-by-character different than 'car_pool_capacity'.

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# For the calculations used, there shouldn't be any differences. However, by using just 4 the variable is stored as an integer instead of a float meaning that 'carpool_capacity' is also stored as an integer due to integer multiplication. Because Python 3+ seems to coerce all division anyways, division results should be stored as a float either way.

# 2. NOT A QUESTION OR TASK
# 3. Write comments above each of the variable assignments.
# As a general rule, I do not comment variable assignment if the variable name is sufficient to describe what is being assigned. Given that all variables above are assigned completely out of context and I can still get the gist of what they are doing, commenting is not necessary.

# 4. Make sure you know what = is called (equals) and what it is doing with variables.
# Equals (=) is an assignment operator that links a variable name with the data that is being stored under that name.

# 5. Remember that _ is an underscore character.
# Yep. Also it is corresponds to ASCII value 95 (between upper-case and lower-case), which means that it can cause unintuitive behavior when sorting tables by the ASCII values!
print("Result of 'Test 1' == 'Test_1':", "Test 1" == "Test_1")

# 6. Try running python 3.6 from the Terminal and try assigning variables...
# Done