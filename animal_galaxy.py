import random, sys, time, os
import oceania as o
import pond as p
import vipers_planet as vi
import vulcan as vu

#import sys, time, os
#import random
#import sys, time, os
#import sys
#import time

player_animal_select = 0
player_occupation = ""
player_animal = ""
player_name = ""
player_planet_select = 0
player_planet = ""

animal_list = ["human", "cat", "toad", "falcon", "octopus", "parrot", "owl"]
animal_list_appendages = ["hands", "paws", "webbed feet", "wings", "tentacles", "wings", "wings"]
animal_list_plural = ["humans", "cats", "toads", "falcons", "octopodes", "parrots", "owls"]
animal_list_adjectives = ["humane", "feline", "amphibian", "avian", "tentacled", "brightly coloured", "supposedly wise"]

planet_list = ["Earth", "Catnaveral", "Pond", "Vulcan", "Oceania", "Vipers' Planet"]

planet_dictionary = {"Earth" : "The third rock orbiting a yellow sun in the Milky Way.", "Catnaveral" : "Catnaveral is a balmy, forested planet, fourth from its sun. All the cats who live there live on one ring-shaped continent which sits around the planet's equator. Traces of the compounds that are used to produce rocket fuel are present in the atmosphere.", "Pond" : "Pond is a predominantly water-logged planet with 8/10ths of its surface covered by seas and oceans, it has a relatively humid climate and is home to wide variety of amphibieans and monsterously large vegetation. The dominant species of the planet are the Giant Toads, who live on continent sized lilies, and despite being jumpy by nature the species has managed to come together under one unified banner, the great Toad Nation.", "Vulcan" : "Your instruments cannot determine anything about this planet. Even its atmosphere is a mystery.", "Oceania": "Here aquatic life forms were detected. Alien whales could be a source of ambergris.", "Vipers' Planet" : "This planet is swarming with venomous vipers."}
welcome_dictionary = {0 : "Welcome", 1 : "Welcome back"}
cat_spiel_dictionary = {0 : " We cats are the foremost pilots and doctors in the Animal Galaxy. I am Wing Commander Felius.\nNormally, we'd be happy to help out any starfarer in need, but a recession caused by the exploding catnip price has left us with a shortage of rocket fuel. If you want some, the only way to get it is to travel to the Tricksy Forest yourself and collect some fruit from the good tree. We use the fruit's nectar to make fuel. The tree you want has pale bark and blue fruit.\nDo you want to travel to the Tricksy Forest? (Yes/No): ", 1 : " Do you have the blue fruit? (Yes/No): "}
cat_alchemy_dictionary = {0 : "If you have any fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere.", 1 : "If you have any more fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere.", 2 : "If you have any more fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere."}
space_nectar = []
planet_list_start = 1
felius_fruit = [0, 0] #Fuel at index 0, Potion at index 1
visited = False
maze_dictionary = {0 : "an open area under the forest canopy.", 1 : "a thicket of briars.", 2 : "a few evergreen trees.", 3 : "some flowering bushes.", 8 : "a winding track running east to west.", 4 : "moss growing on some silvery stones.", 5 : "a withered old tree, long past sprouting any fruit.", 6 : "a pale tree with blue fruit!", 7 : "a sign written in claw markings in the ground. It says 'meow meow bountiful tree north of here'."}

items_list = []


def human_planet():
    print(f"After fitting all the requisite parts to your ship, your interstellar engine whirs into life!\nYou return to Earth as {a_an_check(player_animal)} {player_animal}. Congratulations!")
    if not player_animal.title == "Human":
        print(f"However, you are still {a_an_check(player_animal)} {player_animal}...")
    else:
        print(f"As you're a human again, you'll have no trouble fitting in.")
    return

def a_an_check(word_string):
    if word_string[0] in "aeiou":
        return "an"
    else:
        return "a"

def player_reward(item_string):
    items_list.append(item_string)
    return

def player_reward_check():
    if len(items_list) >= 5:
        return True
    else:
        return False

def player_yes_no_choice(string_start):
    #yes_or_no = ""
    yes_or_no = input(string_start)
    if yes_or_no.lower()[0] == "y":
        print("")
        return True
    elif yes_or_no.lower()[0] == "n":
        print("")
        return False
    else:
        player_yes_no_choice(string_start)

def player_animal_choice():
    global player_animal_select
    global player_animal
    try:
        player_animal_select = int(input("Please enter a number 1-6: "))
        player_animal = animal_list[player_animal_select]

        if player_animal_select < 1 or player_animal_select > 6:
            player_animal_choice()

    except ValueError:
        player_animal_choice()
    return

def player_name_choice():
    global player_name
    try:
        player_name = str(input("Please enter your name: "))

    except ValueError:
        player_name_choice()
    return

def player_planet_choice():
    global player_planet_select
    global player_planet
    player_input = input("Please enter a number 1-5 to travel, a planet's name for info, or the word help: ")
    try:
        player_planet_select = int(player_input)
        if player_planet_select < planet_list_start or player_planet_select > 5:
            player_planet_choice()
        else:
            player_planet = planet_list[player_planet_select]
            #Underneath will go how to get to each planet from space.
            if player_planet_select >= 1 or player_planet_select == 0 and len(items_list) >= 5:
                planet_functions[player_planet_select]()
            else:
                print("The navigation computer cannot understand your intention.")
                player_planet_choice()

    except ValueError:
        try:
            player_planet_select = str(player_input)
            if player_planet_select.lower() == "help":
                print(f"You currently have {len(items_list)} of the 5 items you need to repair your engine coils. You are currently {a_an_check(player_animal)} {player_animal}.")
                if len(space_nectar) > 0:
                    print(f"You also have the blue fruit you collected from the Tricksy Forest.")

                print(f"The items in your possession are as follows:")
                if len(items_list) > 0:
                    for i in items_list:
                        print(i)
                else:
                    print("None.")

                player_planet_choice()

            else:
                if player_planet_select.title() in planet_list:
                    print(planet_dictionary[player_planet_select.title()])
                    player_planet_choice()
                else:
                    player_planet_choice()
        except ValueError:
            player_planet_choice()
    return

maze_grid = [[0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0]]

#X and Y
player_location = [0, 0]

def go_direction(direction):
    if direction[0] == "n":
        player_location[1] = (player_location[1] + 1) % 6
    elif direction[0] == "s":
        player_location[1] = (player_location[1] - 1) % 6
    elif direction[0] == "e":
        player_location[0] = (player_location[0] - 1) % 6
    elif direction[0] == "w":
        player_location[0] = (player_location[0] + 1) % 6
    else:
        direction = ""
        player_move()
        #return
    player_maze()
    return

def player_move():
    try:
        player_direction = str(input("To walk, please enter a compass direction or its first letter- (N)orth, (E)ast, (S)outh, or (W)est: ")).lower()
        go_direction(player_direction)
    except ValueError:
        player_move()
    return

nectar_tree = [0, 0]

def player_maze():
    global maze_grid
    global player_location
    print(f"Before you, you see {maze_dictionary[maze_grid[player_location[0]][player_location[1]]]}")#, player_location[0], player_location[1])
    if maze_grid[player_location[0]][player_location[1]] == 6:
        if player_yes_no_choice("Would you like to pick the fruit and return to Cape Catnaveral? (Yes/No): "):
            print("You pick two pieces of fruit from the tree and activate your catsportation beaconn.")
            space_nectar.append("rotten fruit")
            space_nectar.append("ripe fruit")
            cat_planet()
            return
        else:
            player_move()
    else:
        player_move()
    #return


def recursive_tree_check(player, tree):
    if player == tree:
        tree = [random.randint(0, 5), random.randint(0, 5)]
        recursive_tree_check(player, tree)
    else:
        return tree

def maze_puzzle():
    global maze_grid
    global player_location
    global nectar_tree
    player_location = [random.randint(0, 5), random.randint(0, 5)]
    nectar_tree = recursive_tree_check(player_location, nectar_tree)
  
    for n in range(0, 6):
        for m in range(0, 6):
            maze_grid[m][n] = random.randint(0, 5)
    
    for n in range(0,6):
        maze_grid[n][2] = 8

    maze_grid[nectar_tree[0]][nectar_tree[1]-2] = 7
    maze_grid[nectar_tree[0]][nectar_tree[1]] = 6

    #print(maze_grid[nectar_tree[0]][nectar_tree[1]-2], "x", nectar_tree[0], "y", (nectar_tree[1]-2) % 6, "look here")
    #print(maze_grid[nectar_tree[0]][nectar_tree[1]], "x", nectar_tree[0], "y", nectar_tree[1], "tree here")

    #print(maze_grid, "2nd print")

    maze_run = bool(1)
    player_maze()

    return


def cat_planet():
    global visited
    global player_animal_select
    global space_nectar

    print(f"As you approach re-entry, you see white clouds over the Cat Capital, Cape Catnaveral. A spiral runway of sky beacons guides you down towards the surface.\n")

    if player_animal_select == 1:
        print(f"{welcome_dictionary[visited]} to Cape Catnaveral, fellow {animal_list_adjectives[player_animal_select]}!\n{cat_spiel_dictionary[visited]}")
    else:
        print(f"{welcome_dictionary[visited]} to Cape Catnaveral, my {animal_list_adjectives[player_animal_select]} friend!\n{cat_spiel_dictionary[visited]}")
    


    if player_yes_no_choice("") and visited == False and len(space_nectar) == 0:
        print("Nice, I'll use catsportation to move you there. Don't get lost.")
        visited = True
        maze_puzzle()
    elif len(space_nectar) == 0:
        print("Suit yourself mate. Go back into space.")
        visited = False
        space_area()
    else:
        pass
    

    if "ripe fruit" in space_nectar and "rotten fruit" in space_nectar:
        print("Oh, you have the quink-fruit? Pass it to me, and I shall use our fuel extractor cell to process it. It doesn't need to be good fruit, it can even be rotten. It'll be rendered down by the photonic pulveriser.")
        if(player_yes_no_choice("Give Felius the rotten fruit? (Yes/No): ")):
            space_nectar.remove("rotten fruit")
            felius_fruit[0] = 2
        else:
            print("Do you have other fruit you want to give me?")
            if(player_yes_no_choice("Give Felius the ripe fruit? (Yes/No): ")):
                space_nectar.remove("ripe fruit")
                felius_fruit[0] = 1
            else:
                print("Keep the fruit then, it makes good jam.")

        
        if felius_fruit[0] > 0:
            print("Felius takes some of the fruit in his paws and gives it to his wife, Starmariner Fluffy. Fluffy places it in a bronze hopper above a mysterious grinding machine covered with LEDs.")
            print("You now have Arboreal Rocket Fuel in your possession!")
            items_list.append("Arboreal Rocket Fuel")
        
        print(cat_alchemy_dictionary[felius_fruit[0]])
        if(player_yes_no_choice("Hand over the fruit? (Yes/No): ")):
            if felius_fruit[0] == 2:
                space_nectar.remove("ripe fruit")
                felius_fruit[1] = 1
                print("Fluffy goes away for an hour and returns with a white capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                player_animal_select = 0
                player_animal = animal_list[player_animal_select]
                print(f"You feel light-headed and the room turns dark. When you open your eyes, it looks like something has changed. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}.")

            elif felius_fruit[0] == 1:
                space_nectar.remove("rotten fruit")
                felius_fruit[1] = 2
                print("Fluffy goes away for an hour and returns with a green capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                player_animal_select = random.randint(0, 5)
                player_animal = animal_list[player_animal_select]
                print(f"You feel nauseous and the room turns dark. When you open your eyes, it looks like something has changed. Something has gone wrong. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}!")

            elif felius_fruit[0] == 0:
                space_nectar.remove("ripe fruit")
                felius_fruit[1] = 1
                print("Fluffy goes away for an hour and returns with a white capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                player_animal_select = 0
                player_animal = animal_list[player_animal_select]
                print(f"You feel light-headed and the room turns dark. When you open your eyes, it looks like something has changed. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}.")

        else:
            print("See you around then. Safe travels.")



    print("You return to your spacecraft.")
    space_area()

    return

planet_functions = {0: human_planet, 1 : cat_planet, 2 : p.toad_planet, 3 : vu.vulcan_planet, 5 : vi.viper_planet , 4 : o.octopus_planet}

def item_check():
    global items_list
    global planet_list_start
    if len(items_list) >= 5:
        print("You now have the items you need to repair your ship and return to Earth, if you so choose.")
        planet_list_start = 0
        #if player_yes_no_choice(""):
        #    human_planet()
            #planet_functions[0]()

def space_area():
    print("\nYour spacecraft roars with life as the remains of your engines blast you through space.")
    item_check()
    index = planet_list_start
    print("To travel to one of the planets in the local solar system, enter its number. If you would prefer to learn more about a planet first, enter its name.")
    for p in planet_list[planet_list_start:6:1]:
        print(f"{index} : {p}, a planet populated by {animal_list_plural[index]}.")
        index += 1

    player_planet_choice()
    return

def enter_space():
    print("Glancing at your instruments, you see the Snakecharmer's interstellar engine coils have been wrecked beyond repair. To return to Earth, five items will be needed. The local solar system looks completely unfamiliar. However, your scanners can detect life on five planets.")
    space_area()
    return

def character_setup():
    items_list = []
    space_nectar = []

    print("Welcome to the Snakecharmer Spacecraft 0.9\n...\nAcceleration abnormal. Central computer failing.\nYou feel a crash, and in a second every light has failed. The cockpit has turned darker than the void of space.\nAwaking from a daze, you find you have been transformed as if by magic into an animal. Please select a number to choose which.\n1 : Cat\n2 : Toad\n3 : Falcon\n4 : Octopus\n5 : Parrot\n6 : Owl")
    player_animal_choice()
    print(f"You glance at what were your hands, and see {animal_list_appendages[player_animal_select]} in their stead. Congratulations, you're {a_an_check(player_animal)} {player_animal} now. What is your name, by the way?")
    player_name_choice()
    print(f"Welcome to being a {player_animal}, {player_name}. Hope you have fun as {a_an_check(player_animal)} {player_animal}.")
    print("...\nThe gravity of the nearby solar system is pulling in the Snakecharmer with great force!")
    enter_space()
    return

#maze_puzzle()
if __name__ == '__main__':
    character_setup()