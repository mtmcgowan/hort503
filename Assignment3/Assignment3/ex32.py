the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruits}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")


# Study Drills
# 1. Take a look at how you used range. What does it do?
# range generates a list of integers from the first argument to the second argument.

# 2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements
# Depends on what you want elements for. In the case of using it as a for loop array, either works.
elements2 = range(0, 6)
print("Type of original elements: ", type(elements))
print("Type of test elements: ", type(elements2))

for i in elements2:
    print(f"Element was: {i}")

# 3. Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?
# Remove elements, sort them, search them.