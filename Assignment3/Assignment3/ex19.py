def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drills

# 1. Go back through the script and type a comment above each line explaining in English what it does.
# Define a function cheese_and_crackers, which accepts two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print several statements that uses the input variables
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Call the new function with two integers
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# Assign two variables with integers
amount_of_cheese = 10
amount_of_crackers = 50

# Call the new function with the two variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# Call the new function with nested arithmatic
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Call the new function with variables and arithmatic
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 2. Start at the bottom.....
# Done

# 3. Write at least one more function of your own design, and run it 10 different ways.
import time
def tell_joke(humor_level):
    if humor_level == "Hilarious":
        print("So Darth Vader walks into a cantina and the bartender says...")
        time.sleep(2)
        print("'Nice suit, that musta cost an arm and a leg!'")
        time.sleep(2)
    elif humor_level == "Funny":
        print("What do you call 2 monkeys that share an Amazon account?")
        time.sleep(2)
        print("Prime mates!")
        time.sleep(2)
    elif humor_level == "Dad":
        print("I thought about going on an all-almond diet.")
        time.sleep(2)
        print("But that's just nuts!")
        time.sleep(2)
    elif humor_level == "Lame":
        print("What do you call a man with no arms, no legs, and hanging on a wall?")
        time.sleep(2)
        print("Art!")
        time.sleep(2)
    else:
        print("Please pick a humor level: Hilarious, Funny, Dad, or Lame")

level = "Funny"
tell_joke(level)

tell_joke("Hilarious")
tell_joke("La" + "me")