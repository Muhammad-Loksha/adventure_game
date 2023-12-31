# importing the important modules
from time import sleep
import sys
import random


def print2_sleep(first_text, second_text):
    """
    This function prints two texts in a single print and
    sleeps for 2 seconds
    """
    print(f"{first_text}{second_text}")
    sleep(2)


def print_sleep(text):
    """
    This function prints text and
    sleeps for a second
    """
    print(text)
    sleep(1)


def run():
    # first play game menu
    print("Welcome to the adventure game!")
    print_sleep("1 - Play The Game")
    print_sleep("2 - Exit")
    while True:
        message = "Please enter 1 to play or 2 to exit: "
        user_number = input(message)
        if user_number == "1":
            stage0()
            break
        if user_number == "2":
            sys.exit()


def stage0():
    # game story
    print_sleep(".")
    print_sleep(".")
    print_sleep(".")
    characters = ["King", "Emperor", "Queen", "Prince", "Princess", "Duke",
                  "Duchess"]
    character = random.choice(characters)
    places0 = ["Village", "Town", "Hamlet", "Borough"]
    place0 = random.choice(places0)
    places1 = ["Castle", "Fortress", "Citadel", "Keep", "Palace", "Tower",
               "Stronghold", "Bastion"]
    place1 = random.choice(places1)
    creatures = ["Dragon", "Chimera", "Hydra", "Kraken", "Minotaur", "Phoenix"]
    creature = random.choice(creatures)
    places2 = ["Desert", "Jungle", "Mountain Range", "Canyon", "Swamp"]
    place2 = random.choice(places2)
    randoms = {"character": character, "creature": creature, "place": place0,
               "place1": place1, "place2": place2}
    print2_sleep(f"You are in front of the {character}'s {place1} at night,",
                 f" it is located on the highest point of the {place0}.")
    print2_sleep(f"There is a rumor that the {character} of the {place0}",
                 " is good on the outside and evil on the inside")
    print2_sleep(f"As he/she uses a {creature} to kill anyone who disagrees",
                 " with his opinion or gets in his/her way," +
                 "even the innocent.")
    print2_sleep(f"Behind you there is a dangerous dark {place2} in",
                 " which some strange things are happening!")
    print2_sleep(f"You must save the people of your {place0} from",
                 f" the oppression of the {character}.")
    print_sleep("Which place are you going to go?")
    stage1(0, randoms)


def stage1(counter, randoms):
    # first stage that has first choice
    character = randoms["character"]
    place1 = randoms["place1"]
    place2 = randoms["place2"]
    print_sleep(f"1 - Go to the {character}'s {place1}")
    print_sleep(f"2 - Go to the dark {place2}")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter += 1
            place1_stage(counter, randoms)
            break
        if user_number == "2":
            counter += 1
            place2_stage(counter, False, randoms)
            break


def place1_stage(counter, randoms):
    # wick character place stage
    character = randoms["character"]
    place1 = randoms["place1"]
    print2_sleep(f"You have entered the {character}'s {place1} and you are",
                 " now slowly walking through it.")
    print2_sleep("But the path you are walking in ends with",
                 " two paths, left and right.")
    print_sleep("1 - Go Right")
    print_sleep("2 - Go Left")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter += 1
            right_path(counter, randoms)
            break
        if user_number == "2":
            counter += 1
            left_path(counter, randoms)
            break


def left_path(counter, randoms):
    # left path stage
    print_sleep("The road is blocked.")
    print_sleep("Wait!")
    containers = ["chest", "barrel", "crate", "trunk"]
    container = random.choice(containers)
    randoms["container"] = container
    print_sleep(f"There is an old {container} beside you.")
    print_sleep("1 - Open it")
    print_sleep("2 - Leave it")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter += 2
            container_stage(counter, randoms)
            break
        if user_number == "2":
            counter -= 1
            right_path(counter, randoms)
            break


def container_stage(counter, randoms):
    # container stage that has the weapons that the user will choose
    container = randoms["container"]
    print_sleep(f"Let's see what is inside this {container}.")
    container_title = container.capitalize()
    first_weapons = ["Bow", "Crossbow"]
    first_weapon = random.choice(first_weapons)
    throing_weapons = ["Atlatl", "Boomerang", "Chakram", "Javelin", "Shuriken"]
    second_weapons = throing_weapons
    second_weapon = random.choice(second_weapons)
    third_weapons = throing_weapons
    third_weapon = random.choice(third_weapons)
    print_sleep(f"{container_title} Contents: ")
    print_sleep(f"   * 1 {first_weapon}")
    print_sleep(f"   * 3 {second_weapon}")
    if third_weapon == second_weapon:
        third_weapon = "Knife"
    print_sleep(f"   * 1 {third_weapon}")
    print_sleep(f"1 - Take the {first_weapon} and the {second_weapon}s")
    print_sleep(f"2 - Take the {third_weapon}")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter += 3
            randoms["first_weapon"] = first_weapon
            randoms["second_weapon"] = second_weapon
            right_path(counter, randoms)
            break
        if user_number == "2":
            counter -= 2
            randoms["third_weapon"] = third_weapon
            right_path(counter, randoms)
            break


def right_path(counter, randoms):
    # right path stage
    character = randoms["character"]
    print2_sleep(f"You found the {character}'s room,",
                 " but there are two guards in front of it.")
    print_sleep("You have to fight them to get in.")
    if "first_weapon" in randoms:
        first_weapon = randoms["first_weapon"]
        second_weapon = randoms["second_weapon"]
        print_sleep(f"1 - Use your {first_weapon} and {second_weapon}s")
        print_sleep("2 - Use your hands")
        while True:
            user_number = input("Please enter 1 or 2: ")
            if user_number == "1":
                counter += 1
                print_sleep("You hit the first guard!")
                print_sleep(f"You have 2 {second_weapon}s left.")
                print_sleep("You didn't hit the second guard!!")
                print2_sleep(f"You only have one {second_weapon} left,",
                             " so you only have one chance!")
                print_sleep("Watch out he is approaching you!!!")
                print2_sleep("Finally you hit him and",
                             f" you can now enter the {character}'s room.")
                character_room(counter, randoms)
                break
            if user_number == "2":
                counter -= 3
                print2_sleep("Unfortunately, the two guards are",
                             " armed.")
                lose_stage(counter)
                break
    elif "third_weapon" in randoms:
        third_weapon = randoms["third_weapon"]
        print_sleep(f"1 - Use your {third_weapon}")
        print_sleep("2 - Use your hands")
        while True:
            user_number = input("Please enter 1 or 2: ")
            if user_number == "1":
                counter -= 2
                print2_sleep(f"You throw your {third_weapon} at the first",
                             " guard, and you actually kill him, but...")
                print2_sleep("before you can pick up your knife, the second",
                             " guard managed to stab you with his spear!!!")
                lose_stage(counter)
                break
            if user_number == "2":
                counter -= 3
                print2_sleep("Unfortunately, the two guards are",
                             " armed.")
                lose_stage(counter)
                break
    else:
        print_sleep("You have nothing but your hands to fight")
        counter -= 3
        print2_sleep("Unfortunately, the two guards are",
                     " armed.")
        lose_stage(counter)


def character_room(counter, randoms):
    # character room stage in which the user will find the key
    character = randoms["character"]
    creature = randoms["creature"]
    place2 = randoms["place2"]
    print_sleep(f"You have entered the {character}'s room.")
    print2_sleep(f"The {character} is sleeping in his bed, so you have",
                 " to sneak up on him without making any noises,")
    print_sleep(" or he/she will wake up and you don't want him/her either.")
    print2_sleep(f"You found a necklace on the {character}'s neck and the ",
                 "necklace had a golden key emblazoned" +
                 f" with a symbol of a {creature}!")
    input("Please enter ANY KEY to pick it up: ")
    print("Key captured")
    print2_sleep(f"You must go to the {creature} in",
                 f" the Dark {place2} and kill it")
    input(f"Please enter ANY KEY to go to dark {place2}: ")
    print_sleep(".")
    print_sleep(".")
    print_sleep(".")
    place2_stage(counter, True, randoms)


def lose_stage(counter):
    # lose stage stage in which the user loses
    print_sleep("And you were killed in the end.")
    print_sleep("A sad end for a brave hero.")
    print_sleep("You lost!")
    play_again(counter)


def place2_stage(counter, key, randoms):
    # place 2 stage in which the fanatasy crature exists
    place2 = randoms["place2"]
    print2_sleep(f"You are now in the dark {place2}, ",
                 "you can hardly see in this pitch darkness.")
    print_sleep("There is the sound of leaves moving behind you")
    print_sleep("You think something is following you!")
    print_sleep("1 - Run Away!!")
    print_sleep("2 - Stay where you are and watch")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter -= 1
            print_sleep("There is a wolf with two wings chasing you!")
            print_sleep("You run as fast as you can, but it's useless...")
            print_sleep("It killed you in the end.")
            lose_stage(counter)
            break
        if user_number == "2":
            counter += 2
            creatures2 = ["little fairy", "sprite", "dwarve", "goblin"]
            creature2 = random.choice(creatures2)
            randoms["creature2"] = creature2
            print_sleep(f"Behind the bushes seems to be a {creature2}.")
            print2_sleep("Look! She's walking in a certain direction",
                         ", follow her!")
            creature2_stage(counter, key, randoms)
            break


def creature2_stage(counter, key, randoms):
    # creature 2 stage in which the user will find a little creature
    creature2 = randoms["creature2"]
    powerful_weapons = ["netherite Sword", "trident", "diamond sword"]
    powerful_weapon = random.choice(powerful_weapons)
    poor_weapons = ["rusty sword", "wooden axe", "wooden stick"]
    poor_weapon = random.choice(poor_weapons)
    creature = randoms["creature"]
    print_sleep(f"The {creature2} has a {powerful_weapon} in her right hand")
    print_sleep(f"And in her left hand a {poor_weapon}.")
    print_sleep(f"You have to choose one of them to fight the {creature}.")
    # powerful weapon capitalized
    pwc = powerful_weapon.capitalize()
    # poor weapon capitalized
    poowc = poor_weapon.capitalize()
    print_sleep(f"1 - {pwc}")
    print_sleep(f"2 - {poowc}")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            counter += 2
            randoms["powerful_weapon"] = powerful_weapon
            creature_stage(counter, randoms, key)
            break
        if user_number == "2":
            counter -= 2
            randoms["poor_weapon"] = poor_weapon
            creature_stage(counter, randoms, key)
            break


def creature_stage(counter, randoms, key):
    """
    main creature stage, here the user will find the main creature
    and it will be his enemy
    """
    creature2 = randoms["creature2"]
    creature = randoms["creature"]
    print2_sleep(f"The {creature2} enters a dark cave,",
                 " then shines and disappears.")
    print_sleep("You are now slowly entering this cave")
    print_sleep(f"What luck You found the {creature}!")
    print_sleep("It's in a locked cage!")
    print_sleep("1 - Open the lock with the key")
    print2_sleep("2 - Open the lock with your hands",
                 " or anything from your inventory")
    while True:
        user_number = input("Please enter 1 or 2: ")
        if user_number == "1":
            if key is True:
                print_sleep("You opened the lock.")
                print_sleep("There are skeletons" +
                            f" next to the sleeping {creature}.")
                print_sleep("The place looks really scary.")
                print_sleep(f"Oh my gosh, the {creature} has awakened!!")
                print2_sleep("You must kill it immediately",
                             " before he eats you!")
                if "powerful_weapon" in randoms:
                    powerful_item(counter, randoms)
                else:
                    poor_weapon = randoms["poor_weapon"]
                    print2_sleep(f"Your {poor_weapon} is weak.",
                                 f" You can't fight the {creature}.")
                    lose_stage(counter)
            else:
                character = randoms["character"]
                place1 = randoms["place1"]
                print2_sleep("You don't have the key,",
                             f" Find it in the {character}'s {place1}")
                while True:
                    message = ("Please enter 1 to go" +
                               f" to the {character}'s {place1}: ")
                    user_number2 = input(message)
                    if user_number2 == "1":
                        print_sleep(".")
                        print_sleep(".")
                        print_sleep(".")
                        place1_stage(counter, randoms)
                        break
            break
        if user_number == "2":
            counter -= 1
            print_sleep("Unfortunately, the lock is firmly closed.")
            print_sleep("You must use the key.")


def powerful_item(counter, randoms):
    # powerful item stage in which the user uses his powerful weapon
    powerful_weapon = randoms["powerful_weapon"]
    print_sleep(f"You can use your {powerful_weapon}.")
    while True:
        user_number = input("Please enter 1 to use it: ")
        if user_number == "1":
            creature_fight(counter, randoms)
            break


def creature_fight(counter, randoms):
    # creature fight stage in which the user fight the main creature
    creature = randoms["creature"]
    print_sleep(f"Now kill the {creature} quickly!!")
    while True:
        user_number = input("Please enter 1 to kill it: ")
        if user_number == "1":
            counter += 3
            print2_sleep("You ride on top of the",
                         f" {creature} and slash its neck!")
            winning_stage(counter, randoms)
            break


def play_again(counter):
    """
    play again stage which allows the user to play again if they wanted
    and their score is printed on the screen
    """
    print_sleep("GAME OVER!")
    print_sleep(f"Your Score is {counter}")
    while True:
        answer = input("Play again? [y/n] ")
        if answer in ("y", "Y"):
            stage0()
            break
        if answer in ("n", "N"):
            sys.exit()


def winning_stage(counter, randoms):
    # wining stage in which the user wins the game
    creature = randoms["creature"]
    print_sleep(f"Finally You Killed the {creature} and Saved the peoples.")
    print_sleep("Congratulations! You won!")
    play_again(counter)


# Call game start menu function
run()
