i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

# Study Drills
# 1. Convert this while-loop to a function that you can call, and replace 6 in the test(i < 6) with a variable.
def n_while(number):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print("The numbers: ")
    for num in numbers:
        print(num)

n_while(4)

# 2. Use this function to rewrite the script to try different numbers.
n_while(3)
n_while(2)

# 3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much in increments by.
def n_whileby(number, increment):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print("The numbers: ")
    for num in numbers:
        print(num)

# 4. Use this function
n_whileby(10, 2)

# 5 Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
# No, the incrementor is not necessary.
numbers = []

for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)
        
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
