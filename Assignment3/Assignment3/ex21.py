def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Study Drills
# 1. If you aren't really sure...
# OK

# 2. A the end of the script is a puzzle. I'm taking...
# OK

# 3. Once you have the  formula worked out....
def subtract(a, b):
    print(f"SUBTRACTING {b} - {a}")
    return b - a
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what)

# 4. Do the inverse. Write a simple formula and use the functions in the same way to calculate it.
print(400 / 4 - 10)

what = subtract(10, divide(400, 4))
print("That becomes: ", what)
