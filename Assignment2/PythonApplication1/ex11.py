# EXERCISE 11
print("")
print("Exercise 11: Asking Questions")

print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Study Drills
# 1. Go online and find out what Python's input does.
# The input() method reads a line from input, convets it into a string and returns it.

# 2. Can you find other ways to use it? Try some of the samples you find.
number = 1
print("Am I holding one or two fingers behind my back?", end = ' ')
guess = input()
print("Your guess was:", int(guess) == number)

# 3. Write another "form" like this to ask some other questions
print("What is your name?", end = ' ')
name = input()
print("What is your quest?", end = ' ')
quest = input()
print("What is the air-speed velocity of an unladen swallow (in miles-per-hour)?", end = ' ')
airspeed = input()

if (type(airspeed) is int):
    if (int(airspeed) == 24):
        print("Right. Off you go.")
    else: print("<you are cast into the Gorge of Eternal Peril because of your comedic ignorance>")
elif (type(airspeed) is str):
    if (airspeed == "African or European swallow?"):
        print("What? I don't know that! Auuuuuuuuuugh!")
    else: print("<you are cast into the Gorge of Eternal Peril because of your comedic ignorance>")

