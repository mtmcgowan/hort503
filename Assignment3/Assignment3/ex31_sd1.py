print("""You enter a dark room with two doors.
Do you go through the door # 1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        insane = 0
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        insane = 1

else:
    print("You stumble around and fall on a knife and die. Good job!")

def insane():
    print("You try to read a clock on the wall. The numbers keep changing.")
    print("1. Go through an open door.")
    print("2. Click your heels.")
    dream = input("> ")

    if dream == "1":
        insane()
    else:
        print("You wake up from your dream.") 

insane()