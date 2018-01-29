# Homework: Write a game similar to the one used in exercise 35

import sys
from random import *

def room_encounter():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room(hp, right_hand, left_hand):
    print_hp(hp)
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif "axe" in choice and right_hand == 1:
            hp = attack_bear(hp)
            check_hp(hp)
            bear_room(hp, right_hand, left_hand)
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room(hp, right_hand, left_hand):
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    elif ("shield" in choice) and (left_hand == 1):
        print("You hide behind your shield. The monster flees from it's own reflection")
        gold_room()
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start(*items):    
    local_items = list(items)
    hp = 20    
 
    print_hp(hp)

    scan_armory(local_items)   

    print("What do you do?")

    choice = input("> ")

    if "portal" in choice:
        go_adventuring(hp, local_items)    
    elif ("get" in choice) or ("take" in choice) or ("get" in choice):
        local_items = get_item(local_items, choice)   
    else:
        print("Your feeble barbarian brain hurts from such complex ideas....")

    print(f"Local items: {local_items}")

    start(local_items) # Recursively call the start function until the player decides to go adventuring
        

def print_hp(hp):
    print(f"Your current hp is: {hp}")

def scan_armory(*items):
    getattr(self, func)(*items)
    local_items = items
    print("You are in a an armory.")
    print(local_items)
    if (local_items[0] != 1) and (local_items[0] != 1):
        print("An two-handed battleaxe lies on the floor.")

    if (local_items[1] != 1):
        print("A shiny shield leans on a wall.")

    if (local_items[2] != 1):
        print("A rack holds a suit of chainmail.")

    if (local_items[2] != 2):
        print("A leather hauberk is discarded on the floor.")

    if (local_items[0] != 2):
        print("A shortsword sits on a table") 
    
    print("There is a glowy portal at the end of the room.")  

def get_item(items, choice):
    if ("axe" in choice) or ("battleaxe" in choice):
        if items[0] == 0 and items[1] == 0:
            print("You pick up the two-handed axe.")
            items[0] = 1
        elif items[0] == 1:
            print("You already are holding the axe.")
        else:
            print("Your hands are already full")
    elif ("suit" in choice) or ("chainmail" in choice):
        if items[2] == 0:
            print("You put on the chainmail.")
            items[2] = 1
        elif items[0] == 1:
            print("You already wearing the chainmail.")
        else:
            print("You are already wearing armor.")
    elif ("leather" in choice) or ("hauberk" in choice):
        if items[2] == 0:
            print("You put on the leather armor.")
            items[2] = 2
        elif items[0] == 2:
            print("You already wearing leather armor.")
        else:
            print("You are already wearing armor.")
    elif ("shield" in choice) or ("shiny" in choice):
        if items[1] == 0 and items[0] != 1:
            print("You pick up the shield.")
        elif items[1] == 1:
            print("You already have the shield.")
            items[2] = 1
        else:
            print("Your hands are full.")
    elif ("shortsword" in choice) or ("sword" in choice):
        if items[0] == 0:
            print("You pick up the shortsword.")
        elif items[0] == 1:
            print("You already have the shortsword.")
            items[0] = 2
        else:
            print("Your hands are full.")
    else:
        print("Your feeble barbarian brain hurts from such complex ideas....")



def attack_bear(hp):
    bear_roll = 0
    player_roll = 0
    new_hp = 0

    bear_roll = randint(1, 12)
    player_roll = randint(0, 0)

    if player_roll > bear_roll:
        print("You slice off the bear's head and move through the door")
        gold_room()
    else:
        print(f"You slip on a banana peel and the bear mauls you for {bear_roll - player_roll} damage!")
        new_hp = hp - (bear_roll - player_roll)
        return new_hp

def check_hp(hp):
    if hp <= 0:
        dead("You bleed out as your vision fades to black.")

start([0] * 5)