ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"];


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5]))

# Study Drills

# 1. Take each function......translate them to what Python does.

# pop(more_stuff)
# append(stuff, next_one)
# join(' ', stuff)
# join('#', stuff[3:5))

# 2.

# Call pop with argument more_stuff
# call append with arguments stuff and next_one
# call join with arguments ' ' and stuff
# call join with arguments '#' and stuff[3:5]

# 3. Go read about "object-oriented programming"....
# Ok

# 4. Read up on what a "class" is in Python
# A class appears to be quite similar to a 'struct' in C. It stores a specific arrangement of data and can also define methods for altering its state. A method is a function, but a function is not necessarily a method...

# 5. Do not worry if you do not have any idea what I'm.....
# Ok, not a drill....

# 6. Find 10 examples of things in the real world that would fit in a list.
data_storage = ["Myth", "Book", "Floppy disk", "Zip disk", "Compact disk", "Hard disk drive", "DNA", "Smoke signals"];
print(data_storage)

print("Using the sort function")
data_storage.sort()
print(data_storage)

