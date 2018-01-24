from sys import exit
from random import *

def gold_room():
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

def start(right_hand = 0, left_hand = 0):
    hp = 20    
    print_hp(hp)
    print("You are in a an armory.")
    
    if right_hand == 0:
        print("An long axe lies on the floor.")

    if left_hand == 0:
        print("A shiny shield leans on a wall.")

    print("There is a door to your right and left.")

    print("What do you do?")

    choice = input("> ")

    if choice == "left":
        bear_room(hp, right_hand, left_hand)
    elif choice == "right":
        cthulhu_room(hp, right_hand, left_hand)
    elif "axe" in choice:
        if right_hand == 0:
            print("You pick up the axe in your right hand.")
            right_hand = 1            
        else:
            print("The axe is in your right hand.")
        start(right_hand, left_hand)    
    elif "shield" in choice:
        if left_hand == 0:
            print("You pick up the shield in your left hand.")
            left_hand = 1
        else:
            print("The shield is in your left hand.")
        start(right_hand, left_hand)
    else:
        dead("You stumble around the room until you starve.")

def print_hp(hp):
    print(f"Your current hp is: {hp}")

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
start(0, 0)