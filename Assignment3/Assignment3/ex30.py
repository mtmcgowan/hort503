people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("Maybe we could take the trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# Study Drills
# 1. Try to guess what elif and else are doing
# elif is 'else-if' which only executes if the previous statements evalute to false and the current statements is true
# else executes if all previous statements evaluated to false

# 2. Change the numbers of cars, people, and trucks, and then trace through each if-statement to see what will be printed.
cars = 20
people = 30
trucks = 200


#if cars > people:
    # Should be False
#    print("We should take the cars.")
#elif cars < people:
    # Should be True
#    print("We should not take the cars.")
#else:
    # Will not evaluate
#    print("We can't decide.")

#if trucks > cars:
    # True
#    print("That's too many trucks.")
#elif trucks < cars:
    # Will not evaluate
#    print("Maybe we could take the trucks.")
#else:
    # Will not evaluate
#    print("We still can't decide.")

#if people > trucks:
    # True
#    print("Alright, let's just take the trucks.")
#else:
#    print("Fine, let's stay home then.")

# 3. Try some more complex boolean expressions like cars > people or trucks < cars.
print(cars > people or trucks < cars)

# 4. Above each line write an English description of what the line does.
# Assign three integer variables
people = 30
cars = 40
trucks = 15

# Check if there are more cars than people
if cars > people:
    print("We should take the cars.")
# Check if there are more people than cars
elif cars < people:
    print("We should not take the cars.")
# If neither is true (cars == people)
else:
    print("We can't decide.")
# Check if there are more trucks than cars
if trucks > cars:
    print("Maybe we could take the trucks.")
# Else if check if there are more cars than trucks.
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Otherwise (trucks == cars)
else:
    print("We still can't decide.")

# Check if there are more people than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# Otherwise (people <= trucks)
else:
    print("Fine, let's stay home then.")