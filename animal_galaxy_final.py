#Sha's Work

import random, sys, time, os

############################################################################################################################################


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

planet_dictionary = {"Earth" : "The third rock orbiting a yellow sun in the Milky Way.", "Catnaveral" : "Catnaveral is a balmy, forested planet, fourth from its sun. All the cats who live there live on one ring-shaped continent which sits around the planet's equator. Traces of the compounds that are used to produce rocket fuel are present in the atmosphere.", "Pond" : "Pond is a predominantly water-logged planet with 8/10ths of its surface covered by seas and oceans, it has a relatively humid climate and is home to wide variety of amphibians and monstrously large vegetation. The dominant species of the planet are the Giant Toads, who live on continent sized lilies, and despite being jumpy by nature the species has managed to come together under one unified banner, the great Toad Nation.", "Vulcan" : "Your instruments cannot determine anything about this planet. Even its atmosphere is a mystery.", "Oceania": "Here aquatic life forms were detected. Alien whales could be a source of ambergris.", "Vipers' Planet" : "This planet is swarming with venomous vipers."}
welcome_dictionary = {0 : "Welcome", 1 : "Welcome back"}
cat_spiel_dictionary = {0 : "We cats are the foremost pilots and doctors in the Animal Galaxy. I am Wing Commander Felius.\nNormally, we'd be happy to help out any starfarer in need, but a recession caused by the exploding catnip price has left us with a shortage of rocket fuel. If you want some, the only way to get it is to travel to the Tricksy Forest yourself and collect some fruit from the good tree. We use the fruit's nectar to make fuel. The tree you want has pale bark and blue fruit.\nDo you want to travel to the Tricksy Forest? (Yes/No): ", 1 : "Was that hard? (Yes/No): "}
cat_alchemy_dictionary = {0 : "If you have any fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere.", 1 : "If you have any more fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere.", 2 : "If you have any more fruit, Fluffy could use the nectar to make an elixir of physical restoration. She's the greatest biochemist in the eastern hemisphere."}
space_nectar = []
planet_list_start = 1
felius_fruit = [0, 0] #Fuel at index 0, Potion at index 1
visited = False
maze_dictionary = {0 : "an open area under the forest canopy.", 1 : "a thicket of briars.", 2 : "a few evergreen trees.", 3 : "some flowering bushes.", 8 : "a winding track running east to west.", 4 : "moss growing on some silvery stones.", 5 : "a withered old tree, long past sprouting any fruit.", 6 : "a pale tree with blue fruit!", 7 : "a sign written in claw markings in the ground. It says 'meow meow bountiful tree north of here'."}

items_list = []

cat_access = True

os.system("color")

def readout(mess):
    for c in mess:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c != "\n":
            time.sleep(0.001)
        else:
            time.sleep(0.2)
    sys.stdout.write("\n")
    sys.stdout.flush()
    return

def human_planet():
    readout(f"After fitting all the requisite parts to your ship, your interstellar engine whirs into life!\nYou return to Earth as {a_an_check(player_animal)} {player_animal}. Congratulations!")
    if not player_animal.title == "Human":
        readout(f"However, you are still {a_an_check(player_animal)} {player_animal}...")
    else:
        readout(f"As you're a human again, you'll have no trouble fitting in.")
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
        readout("")
        return True
    elif yes_or_no.lower()[0] == "n":
        readout("")
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
    global player_animal
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
                readout("The navigation computer cannot understand your intention.")
                player_planet_choice()

    except ValueError:
        try:
            player_planet_select = str(player_input)
            if player_planet_select.lower() == "help":
                
                readout(f"You currently have {len(items_list)} of the 5 items you need to repair your engine coils. You are currently {a_an_check(player_animal)} {player_animal}.")
                if len(space_nectar) > 0:
                    readout(f"You also have the blue fruit you collected from the Tricksy Forest.")

                readout(f"The items in your possession are as follows:")
                if len(items_list) > 0:
                    for i in items_list:
                        readout(i)
                else:
                    readout("None.")

                player_planet_choice()

            else:
                if player_planet_select.title() in planet_list:
                    readout(planet_dictionary[player_planet_select.title()])
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
    readout(f"Before you, you see {maze_dictionary[maze_grid[player_location[0]][player_location[1]]]}")#, player_location[0], player_location[1])
    if maze_grid[player_location[0]][player_location[1]] == 6:
        if player_yes_no_choice("Would you like to pick the fruit and return to Cape Catnaveral? (Yes/No): "):
            readout("You pick two pieces of fruit from the tree and activate your catsportation beacon.")
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

    #readout(maze_grid[nectar_tree[0]][nectar_tree[1]-2], "x", nectar_tree[0], "y", (nectar_tree[1]-2) % 6, "look here")
    #readout(maze_grid[nectar_tree[0]][nectar_tree[1]], "x", nectar_tree[0], "y", nectar_tree[1], "tree here")

    #readout(maze_grid, "2nd print")

    maze_run = bool(1)
    player_maze()

    return


def cat_planet():
    global visited
    global player_animal_select
    global space_nectar
    global cat_access
    print(u"\u001b[31m\n       \`*-.    \n        )  _`-. \n       .  : `. . \n       : _   '  \ \n       ; *` _.   `*-._          \n       `-.-'          `-.       \n         ;       `       `.     \n         :.       .        \    \n         . \  .   :   .-'   .   \n         '  `+.;  ;  '      :   \n         :  '  |    ;       ;-. \n         ; '   : :`-:     _.`* ;\n      .*' /  .*' ; .*`- +'  `*' \n      `*-*   `*-*  `*-*'        \u001b[0m\n")

    if cat_access and not "Arboreal Rocket Fuel" in items_list:
        readout(f"As you approach re-entry, you see white clouds over the Cat Capital, Cape Catnaveral. A spiral runway of sky beacons guides you down towards the surface.\n")

        if player_animal_select == 1:
            readout(f"{welcome_dictionary[visited]} to Cape Catnaveral, fellow {animal_list_adjectives[player_animal_select]}!\n{cat_spiel_dictionary[visited]}")
        else:
            readout(f"{welcome_dictionary[visited]} to Cape Catnaveral, my {animal_list_adjectives[player_animal_select]} friend!\n{cat_spiel_dictionary[visited]}")
        


        if player_yes_no_choice("") and visited == False and len(space_nectar) == 0:
            readout("Nice, I'll use catsportation to move you there. Remember, there is only one road, running east to west. Try exploring everywhere north and south of it. Don't get lost.")
            visited = True
            maze_puzzle()
        elif len(space_nectar) == 0:
            readout("Suit yourself mate. Go back into space.")
            cat_access = False
            visited = False
            space_area()
        else:
            pass
        

        if "ripe fruit" in space_nectar and "rotten fruit" in space_nectar:
            readout("Oh, you have the quink-fruit? Pass it to me, and I shall use our fuel extractor cell to process it. It doesn't need to be good fruit, it can even be rotten. It'll be rendered down by the photonic pulveriser.")
            if(player_yes_no_choice("Give Felius the rotten fruit? (Yes/No): ")):
                space_nectar.remove("rotten fruit")
                felius_fruit[0] = 2
            else:
                readout("Do you have other fruit you want to give me?")
                if(player_yes_no_choice("Give Felius the ripe fruit? (Yes/No): ")):
                    space_nectar.remove("ripe fruit")
                    felius_fruit[0] = 1
                else:
                    readout("Keep the fruit then, it makes good jam.")

            
            if felius_fruit[0] > 0:
                readout("Felius takes some of the fruit in his paws and gives it to his wife, Professor Fluffy. Fluffy places it in a bronze hopper above a mysterious grinding machine covered with LEDs.")
                readout("You now have Arboreal Rocket Fuel in your possession!")
                items_list.append("Arboreal Rocket Fuel")
            
            readout(cat_alchemy_dictionary[felius_fruit[0]])
            if(player_yes_no_choice("Hand over the fruit? (Yes/No): ")):
                if felius_fruit[0] == 2:
                    space_nectar.remove("ripe fruit")
                    felius_fruit[1] = 1
                    readout("Fluffy goes away for an hour and returns with a white capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                    player_animal_select = 0
                    player_animal = animal_list[player_animal_select]
                    readout(f"You feel light-headed and the room turns dark. When you open your eyes, it looks like something has changed. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}.")

                elif felius_fruit[0] == 1:
                    space_nectar.remove("rotten fruit")
                    felius_fruit[1] = 2
                    readout("Fluffy goes away for an hour and returns with a green capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                    player_animal_select = random.randint(0, 5)
                    player_animal = animal_list[player_animal_select]
                    readout(f"You feel nauseous and the room turns dark. When you open your eyes, it looks like something has changed. Something has gone wrong. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}!")

                elif felius_fruit[0] == 0:
                    space_nectar.remove("ripe fruit")
                    felius_fruit[1] = 1
                    readout("Fluffy goes away for an hour and returns with a white capsule. She hands you it and you swallow it. It would be rude to refuse! Cats are very particular.")
                    player_animal_select = 0
                    player_animal = animal_list[player_animal_select]
                    readout(f"You feel light-headed and the room turns dark. When you open your eyes, it looks like something has changed. You are now {a_an_check(animal_list[player_animal_select])} {animal_list[player_animal_select]}.")

            else:
                readout("See you around then. Safe travels.")
    else:
        readout("As you approach Catnaveral three green lasers lance the side of the Snakecharmer Spacecraft with a frightening thwack. It looks like it would be best to turn back.")
        space_area()

    readout("You return to your spacecraft.")
    space_area()



    return

planet_functions = {}

def item_check():
    global items_list
    global planet_list_start
    if len(items_list) >= 5:
        readout("You now have the items you need to repair your ship and return to Earth, if you so choose.")
        planet_list_start = 0
        #if player_yes_no_choice(""):
        #    human_planet()
            #planet_functions[0]()

def space_area():
    readout("\nYour spacecraft roars with life as the remains of your engines blast you through space.")
    item_check()
    index = planet_list_start
    readout("To travel to one of the planets in the local solar system, enter its number. If you would prefer to learn more about a planet first, enter its name.")
    for p in planet_list[planet_list_start:6:1]:
        readout(f"{index} : {p}, a planet populated by {animal_list_plural[index]}.")
        index += 1

    player_planet_choice()
    return

def enter_space():
    readout("Glancing at your instruments, you see the Snakecharmer's interstellar engine coils have been wrecked. To return to Earth, five items will be needed. The local solar system looks completely unfamiliar. However, your scanners can detect life on five planets.")
    space_area()
    return

def character_setup():
    items_list = []
    space_nectar = []

    readout("Welcome to the Snakecharmer Spacecraft 0.9\n...\nAcceleration abnormal. Central computer failing.\nYou feel a crash, and in a second every light has failed. The cockpit has turned darker than the void of space.\nAwaking from a daze, you find you have been transformed as if by magic into an animal. Please select a number to choose which.\n1 : Cat\n2 : Toad\n3 : Falcon\n4 : Octopus\n5 : Parrot\n6 : Owl")
    player_animal_choice()
    readout(f"You glance at what were your hands, and see {animal_list_appendages[player_animal_select]} in their stead. Congratulations, you're {a_an_check(player_animal)} {player_animal} now. What is your name, by the way?")
    player_name_choice()
    readout(f"Welcome to being a {player_animal}, {player_name}. Hope you have fun as {a_an_check(player_animal)} {player_animal}.")
    readout("...\nThe gravity of the nearby solar system is pulling in the Snakecharmer with great force!")
    enter_space()
    return

############################################################################################################################################
#Shaleem's Planet

points_sha = 0

def integer_check_sha(user_input, correct_answer):
    try:
        player_answer = int(user_input)
        if player_answer == correct_answer:
            readout(f"Well Done")
            global points_sha
            points_sha += 1
        #    readout(f"You have {points_sha} points.")
            return

        elif player_answer < 0 or player_answer > 2:
            integer_check_sha("Enter the number correctly. Please: ", correct_answer)
        else:
            readout(f"Wrong answer.")
        #    global wrong_answers_sha
        #    wrong_answers_sha += 1
    except ValueError:
        return
    
def multiple_choice_question_sha(question, option_0, option_1, option_2, correct_answer):
    readout(question)
    readout(f"Option 0: {option_0}")
    readout(f"Option 1: {option_1}")
    readout(f"Option 2: {option_2}")

    integer_check_sha(input("Choose your Answer, type 0 or 1 or 2: "), correct_answer)
    return

def octopus_planet():
    message = "Welcome to Oceania, a world covered in water and ruled by the Whale Queen.\n\n\nUpon landing your craft on the water, you are greeted by a pod of dolphins.\nYou wear your diving helmet (which is equipped with a “universal language translator”), open the hatch and gently glide into the water. \n\nThe leader of the dolphins asks for the purpose of your visit to Oceania.\nYou explain the situation you and your crew are facing and ask if the dolphins would help you source the highly sought-after Ambergris.\nAmbergris is an essential component of the rocket-fuel which when added to the fuel provides enough thrust to the rockets to propel the craft through the wormhole.\nThe dolphin informs you that only the Whale Queen can give you Ambergris. Being highly sought after, special permission must be asked before anyone can have even a small piece of Ambergris.\nYou ask to see the Whale Queen, and the dolphin gestures you to follow it.\nAfter a short journey you arrive at a beautiful lagoon. This is where the Whale Queen holds court, and upon your arrival you are taken directly to meet her.\n\nYou respectfully address the Whale Queen and explain that you are there to source Ambergris for your rocket engines. The Whale Queen is sympathetic to your story, BUT….\n\nBefore anyone can possess the sacred Ambergris, one must prove to the residents of Oceania that they are worthy of owning Ambergris.\n\nYou may prove your worth by answering these three questions correctly:\n\n"
    for char in message:
        sys.stdout.write (char)
        sys.stdout.flush()
        time.sleep(0.005)
        if char != "\n":
            time.sleep(0.005)
        else:
            time.sleep(0.05)

    multiple_choice_question_sha("Your first question is:\nWhat is the largest mammal on your home planet Earth?", "Blue Whale", "Great White Shark", "Giant Squid",0)
    print ("\n")
    multiple_choice_question_sha("Your second question is:\nWhich of these sea creatures has the longest life-span?", "Loch Ness Monster", "Iceland Sharks", "Jellyfish",2)
    print ("\n")
    multiple_choice_question_sha("Your third question is:\nWhat is more?", "Number of stars in the Milky Way Galaxy", "Pieces of plastic in Earth's Oceans", "Hair on a human's head",1)
    print ("\n")
    global points_sha
    if points_sha >= 1:
        readout(f"Congratulations!\nYou have proven that you are worthy of owning Ambergris.\n\nThe Whale Queen presents you with a large piece of Ambergris and instructs the dolphins to escort you back to your spaceship.\n\nNow you can continue your journey to the other planets.")
        readout("You now have Ambergris in your possession!") 
        items_list.append("Ambergris")
        space_area()
    return

############################################################################################################################################
#Lee's Planet

ttt_board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Define the print_ttt_board function
def print_ttt_board():
    global ttt_board
    readout(f"   ╻   ╻   \n {ttt_board[1]} ┃ {ttt_board[2]} ┃ {ttt_board[3]} \n   ┃   ┃   \n╺━━╋━━━╋━━╸\n   ┃   ┃   \n {ttt_board[4]} ┃ {ttt_board[5]} ┃ {ttt_board[6]} \n   ┃   ┃   \n╺━━╋━━━╋━━╸\n   ┃   ┃   \n {ttt_board[7]} ┃ {ttt_board[8]} ┃ {ttt_board[9]} \n   ╹   ╹    ")
    
def player_turn():
    global ttt_board
    choice = input("Please choose a corresponding number 1-9 to place your X. ")
    choice = int(choice)
    if ttt_board[choice] in "123456789":
        ttt_board[choice] = "X"
    else:
            readout("Sorry, that space is not empty!")
            player_turn() 
    return
    
def playerMove(letter, move):
    global ttt_board
    ttt_board[move] = letter

def get_computer_move():
    global ttt_board
    # if the center square is empty choose that
    if ttt_board[5] in "123456789":
        return 5
 
    while True:
        move = random.randint(1, 9)
        # if the move is blank, go ahead and return, otherwise try again
        if ttt_board[move] in "123456789":
            return move
            
        break
 
    return 5
def winner(letter):
    global ttt_board
# returns True if that player has won.

    return ((ttt_board[7] == letter and ttt_board[8] == letter and ttt_board[9] == letter) or 
    (ttt_board[4] == letter and ttt_board[5] == letter and ttt_board[6] == letter) or 
    (ttt_board[1] == letter and ttt_board[2] == letter and ttt_board[3] == letter) or 
    (ttt_board[7] == letter and ttt_board[4] == letter and ttt_board[1] == letter) or 
    (ttt_board[8] == letter and ttt_board[5] == letter and ttt_board[2] == letter) or 
    (ttt_board[9] == letter and ttt_board[6] == letter and ttt_board[3] == letter) or 
    (ttt_board[7] == letter and ttt_board[5] == letter and ttt_board[3] == letter) or 
    (ttt_board[9] == letter and ttt_board[5] == letter and ttt_board[1] == letter))

def toad_game():
    while(winner("O") == False and winner("X") == False):
        print_ttt_board()
        player_turn()
        print_ttt_board()
        ttt_board[get_computer_move()] = "O"
        get_computer_move()
    else:
        if winner("O") == True:
            readout("The Glorious Toad Nation is victorious!! No exotic drive cooling fluid for you sorry, old chum.")
            space_area()
        elif winner("X"):
            readout("Congratulations! You have emerged victorious against our greatest champion, you have secured the precious exotic drive cooling fluid.\nGood luck on your journey and go with the blessing of the great Toad Nation.")
            readout("You now have Exotic Drive Cooling Fluid in your possession!")
            items_list.append("Exotic Drive Cooling Fluid")
            space_area()
    return            

def toad_planet():
    readout("Descending through the atmosphere, the finer details of a vast and wonderful world are slowly revealed to you.\nWhat at first appeared to be continent sized landmasses are, in fact, unbelievably huge lily pads.\nThese continent sized water lilies are all connected by a series of smaller (yet still gigantic) lilies, presumably for travel and transportation. \nUpon the largest of these enormous lilies lies a sprawling metropolis and as you get even closer to the surface, you can truly appreciate the scale of the place.\nThe castle at the heart of the metropolis is hundreds of kilometres wide and as you descend past its highest tower you check your altitude meter which says you're still 2000m from sea level!\nApproaching the surface you can finally start to make out the inhabitants of this strange new world.\nThey are Gigantic Toads and they are happily hopping about their daily business\n200m from the surface, one of them jumps straight up and passes by your ship window, smiling and waving his suitably giant top hat at you.\nWell they seem friendly at least, you think before landing at the gates of the impressive castle.\n")
    time.sleep(4)    
    readout("Upon exiting your craft you are greeted by an opulently dressed Giant Toad..")
    print(u"\u001b[32m\n                   &(       #&,      @*@                                        \n               &     &      #%      /    &*&                                    \n                &,.   %%    &&    %(   ##                                       \n                   **@ %%   &% &&#* &/*                                         \n                     @,*&&(&%#(,/,@.*                                           \n                     &**(&&&%#(*..**/                                           \n                      %%/&%(*.,(* &(                                            \n                     /&&*%%&#.   @&*                                            \n                    %@*@@%&& /##.%%&%%%                                         \n               ###%#(*&@&&(((((///(/###%%%##%%%%%%%%%%                          \n            /((##(#(((((((#(((//*****(#(#/(# (###(#####%/(                      \n             &&%%########((/#((((##**##(#*,./((/((((((######                    \n               %&#/*, *,@&&&&%&&&@@/%###(**/(//,/..,/#%//####.                  \n                    (#&%%%(%%##%##%&##%#%*/(,*/(*//,#(*((#(####                 \n                      /(#(%%&@&&%(#@@%#%%##(*/((./(**(/(#%%%&#(#/               \n                         #%%&%%%#%((#*(/(//#(((*#/(#(###/(//(/&##%(             \n                            #%#(##(/,**(///**/*/*/((*%%##%%##/%%###(#%((        \n                              #%#(/(##/.(**//((((#&%%%/&%/####%####%(####       \n                       ,#(##(*(# *##,.//,,*,**/(*%%%(,(/./.(#(/(#(%@%%##&       \n  /              #((###%(((*(/,*,(#       (***/#&@#%%%*((%,#&%((#%(#(##&        \n       ,**,,*(((((#####%#%##%##%%%%%%%%%%%#####%####((///(%%%%&#%%%%%#(/*,,..   \n  .         ......,,,,,,,,,,,,,,**/(%#######%%##%%%#(/*,,,,,.........\u001b[0m")
    readout("\n'Greetings brave space hopper, what brings you to the fair world of Pond and to the gates of the great castle Jumpalot, The beating heart of the Glorious Toad Nation?'\nYou explain that in order to get back home you need to obtain 3 litres of exotic drive cooling fluid, and you'd detected some on this planet\n'Of course we would be more than hoppy to help but as is our way, you must first defeat our champion at our national pastime, TicTacToad, before you can claim your prize!'\n")
    readout("How to play!- Players take turns marking the spaces in the 3×3 grid. \nThe grid is numbered 1-9 reading from the top left to bottom right respectively.\nThe player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.")
    toad_game()
    return

############################################################################################################################################
#Sehrish's Planet

import random, sys, time, os

def viper_introduction():
    vipers_planet=("Hooray, you just landed on the Vipers' Planet and turned into a parrot. \nBe careful! this planet is full of wriggly, slimy snakes, they are very aggressive and mad. Vipers belong to a venomous family which is gigantic in population. They don't like other species on their planet. \n The only way to keep them calm is to feed them or solve their riddle to save yourself. \n\n\n Please enter yes to play or no to quit. ")
    for i in vipers_planet:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    return

def viper_riddle():
    
    answer="future"
    readout("What is always in front of you but can't be seen?")
    riddle_time_answer = str(input("Please enter your answer:").lower())
    if riddle_time_answer.lower().find(answer) > -1:
        readout("Yey!")
        viper_reward()
        return
    elif riddle_time_answer.lower().find(answer) == -1:
        readout("Try 1 more time.")
        #need countdown for limited times
        viper_riddle()
        return
    else:
        readout("You are nearly there")
        viper_riddle()
        return
        
    return


def player_yes_no():
        
        player_yes_no_string = str(input("Please enter yes or no:"))
        if player_yes_no_string.lower()[0] == "y":
            readout("Yes")
            #linked this function to the other
            viper_riddle()
        elif player_yes_no_string.lower()[0] == "n":
            readout("No")
            readout("You return to your spacecraft.")
            space_area()
        else:
            player_yes_no()
        return

def read_banana():
    message = u"\u001b[33m         @@@@(@(@@                                                 *****   ,***\n  **   **,@@@@((///&@                                              *** *** .****\n  ,*****,     %@@%**,*@                                             *****    ***\n                  @@,..%(,*%@@@@@@@,          . .                               \n                   ,@@/.............@@@&                                        \n                   @@//*../.......//...*@@                                      \n                  @@/./@..................@@                                    \n                  @@/..@%...................@@                                  \n                  @@/...&,...................@@@                                \n                  @@/.....@.....*@@@@&.*@@@@@..@@                @@@@@          \n                  ,@&/.... ...&@.............@..@@               @@   .@        \n                   @%/.,......@..@,   @.@  @.....@@               &&..@@@@@@@@@@\n                    ((/.........@     /.&   @.....@@             @     ,/      .\n                     @@/.......&*(@,  @.&//*/......@@          @.@        .@@@% \n                     .@@/.......@@@@ /%.@@@*@.......@@         @@  @@,        *@\n                      ,@(/.......@@@@..........@.....@*     @@%../@@@@@         \n                       *@//....@@............@.......@@@@@&...*/@@              \n        @@  @           (@(,.....*@/...(@@   @........@@...*/@@,                \n       @    @            &@/.....,@@ .@@@@@@..........@@/@@@                    \n       *@     @@        . @@/......@@@@@@@@@..........(@                        \n     @@  @      @ @@  .@@..@@*.......@*******@.........@*                       \n  @@ @.   @    ,@ @*.....,/&@(..........**.............@@                       \n @@    /.     @,&@@@@@@@@@  @@/........................@@                       \n @   @    *@%               .@/.......................%@*                       \n  @@  ,,                     @&, .....................@@                        \n                             @@.......................@@                        \n                             @@.../..................@@                         \n                            @@(...@...........,,,...@@%                         \n                            @@/../@................,@@                          \n                            @@,..//.............../@@                           \n                           @@/../@...............&@/                            \n                          @@%,./&../............@@                              \n                         /@@/.//@............./@@                               \n                         @@/,//@.........././@@                                 \n                        @@////@...........*/@/                                  \n.                       @@/*/@.*/......./(@/                        . .         \n                        @@//&...../..,/@@                                       \n                         @@/.....,//@@                                          \n                         @%&//(@@@/                             \u001b[0m"
    for x in message:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)
    return

def viper_reward():
    readout("Here is your reward. This Infinity Banana will last you all the way back to your home planet.")
    readout("You now have the Infinity Banana in your possession!")
    items_list.append("Infinity Banana")
    read_banana()
    space_area()

    return

def viper_planet():
    viper_introduction()
    player_yes_no()
    return
############################################################################################################################################
#Moe's Planet

import random, sys, time, os

#player_name = "place holder"
#player_animal = "placeholdian"

secret_words = ["aerospace", "pilot", "boeing", "airbus","aerofoil","jetstream","cockpit","avionics","altimeter","horizon","captain","thrust"]

def get_words():
    word = random.choice(secret_words).upper()
    return word

def save_ruby (tries):
    show_image =[""""  
                      |
                      |
                     / \\
                    /   \\
                    \   / 
                     \ /
                """,
                """
                      |
                      |
                     / \\
                    /   \\
                    \   /
                     \   
                """,
                """
                      |
                      |
                     / \\
                    /   \\
                    \   / 
                """,
                """
                      |
                      |
                     / \\
                    /   \\
                        /
                """,
                """
                      |
                      |
                     / \\
                    /   \\
                """,
                """
                      |
                      |
                     / \\
                    /   
                """,
                """
                      |
                      |
                     / \\

                """,
                """
                      |
                      |
                     /
                """,
                """
                      |
                      |
                """,
                """   |
                
                """
                    ]   
    return show_image[tries]
    
def game(word):
    correct_word = False
    letters_guessed = []
    words_guessed = []
    full_word= "_"* len(word)
    tries = 9
    success = False
    #readout("\nWord ", word, "\n")Cheat

    readout("\n\nSaveruby has been initiated!")
    readout(save_ruby(tries))
    readout("Guess the word: "+ full_word)
    readout("")
    
    while tries > 0 and not correct_word:
        guess = input("Guess a letter, or if you're clever the full word please: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                readout(f"{guess}? You have already guessed that one, silly")
            elif guess not in word:
                readout(guess, "Doesn't exist in the word.")
                tries -= 1
                letters_guessed.append(guess)

                print (save_ruby(tries))
                print (full_word)

            else:
                print ("Get in! You're one step closer to home!")
                full_word_list = list (full_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for i in indices:
                    full_word_list[i] = guess
                    full_word= "" .join(full_word_list)
                if "_" not in full_word:
                    success= True
                print (save_ruby(tries))
                print (full_word)

        elif len(guess) == len (word) and guess.isalpha():
            if guess in words_guessed:
                print ("You have already guessed the word ", guess)
                
            elif guess != word:
                print (guess, " is incorrect.")
                tries -= 1
                words_guessed.append(guess)

                print (save_ruby(tries))
                print (full_word)
            else:
                correct_word: True
                full_word = word
                readout(f"How could you best me? The crystal is yours, {player_animal}. You have earned the esteemed rank - Master of the Rubalised Crystal.")
                readout("The guardian eagle is impressed. He will now beam you back to your spaceship in the blink of an eye.")
                return True
        else:
            print ("Nope, that's invalid.") 

            print (save_ruby(tries))
            print (full_word)

            print ("\n")

        if success:
            print ("Well done, you have guessed the word.")

        else:
            print ("... you're not there yet.")
    else:
        return False
    
def initiate():
    word = get_words()
    
    while game(word) == False:
        readout("I'm feeling generous today, have another go or your crystal is toast!")
        word = get_words()
        game(word)
    else:
        return True

def slow_text (string):
    
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)        
        #time.sleep(0)#debugging
    return

def yes_or_no(question):
    answer = input(question + " (Enter 'yes' to continue or 'no' to chicken out): ").lower().strip()
    readout("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        readout("Input yes or no")
        answer = input(question + " (Enter 'yes' to continue or 'no' to chicken out):").lower().strip()
        readout("")
    if answer[0] == "y":
        return True
    else:
        return False

def vulcan_planet():

    slow_text (f"Greetings {player_name}.\n\
You have traversed the vast void of deep space and have entered the unforgiving atmosphere of \n\
the planet Vulcan.\n\
You are met with howling supersonic winds and treacherous mountains that could overshadow Everest.\n\
This land is rampant with superfast flying beasts that could shred you up should they be alerted to your presence.\n\
You have embarked on a daring mission to find the elusive temple of the rubalised crystal.\n\
The high winds and low visibility make it almost impossible for you to navigate the terrain.\n\
Many have tried and met their demise... this is your only shot to aquire the fabled crystal in order\n\
to recreate a wormhole in the fabric of space-time so you can get back home.")
    if yes_or_no(" Now would be a good time to turn back \n\
or are you willing to risk it?"):
        readout("So... you have chosen death! let's continue")
    else:
        readout("Did you really think you could leave now?! let's continue")

    slow_text ("After treading the desolate landscape for what seems to be an eternity\n\
your space rover's navigation instrument starts to chime indicating you have arrived at the temple of the guardian.\n\
This is where the rubalised crystal is being protected! You exit your rover and with the help of your\n\
anchor boots claw your way to a green shadowy hue.\n\
Oh great... this appears to be a keypad next to the stone entrance.\n\
you will have to answer the riddle below correctly, in order to disarm the forcefield so you can enter the temple.\n\
Do hurry... we don't have much time, this planet's core is very unstable and could collapse in on itself.")


    attempt = 0

    while True:
        print ("\n")
        print ("                              You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. ")
        print (" Please enter your guess or type 'clue', 'another clue', or 'I'm too dumb'.")
        ans= input()
        attempt += 1

        if ans == "candle":
            print ("So, Einstein, you got it right in "+ str(attempt) +" attempt(s). The forcefield has been deactivated!")
            break

        elif ans == 'clue':
            readout("I can be a source of relaxation")

        elif ans == 'another clue':
            readout("I'm pretty bright and waxy")

        elif ans == "I'm too dumb":
            readout('Ha Ha... I knew you didnt have it in you')
            readout("You return to your spacecraft.")
            space_area()
            break

        else: 
            readout("Don't you want the crystal? Give it another go!")

    slow_text ("As you enter the great temple you begin to marvel at the grandeur.\n\
The atmosphere inside is eerie and silent,\n\
a stark contrast to the world outside.\n\
you see a huge shadow pass over you at blinding speed leaving you disorientated by the plumes of volcanic dust \n\
now surrounding you. you hear a thunderous voice echo through the temple - \n")
    print(u"\u001b[33m\n                                   ...     .                                             \n                                           ..'lxxxxdlcc:::;,,'.                                     \n                                   .  'cloc,.';clodddl:,.:xO0Ooc:;.                                 \n                                  .lxox0Oxoc.'c,...;x00kl;lkkdoc:::,.                               \n                               .,,':kkd:;,'...xx;..'odooc:lxdc;cl:,:xo;.                            \n                             ,okkxkxoc::cc;:lco0Oc''lx:;ddd0Kx;.,c;':olo:.                          \n                          .,lOKKK0Odclx00xc;;;;:oxxc,od,:kkkdl;..',..cllxl.                         \n                         .;ldxxxxooxxxolcc;'.;dxocc;'cx:.,;,,::;:c;..:ko;lc'                        \n                       ':dOkxl;..'okkxoc;'...,ck0ko:..:c,,,,'.':dkxo:,,c:..:,                       \n                     'odk00Oxc,'.''''..',''lOkl;:cl:;lxdll;:c':kll0kc;'''.',,.                      \n                   .ckOxddlc;'..,;:,'';c:cokko:,..',;:ol;,;cl:;dkkOl........'.                      \n                  .oK0Oxoc;,'.';cc:;cdxxkKXOdc,..:dxd:;,,;clolc;:c::cc:;c:;:xx;                     \n                 .ldolc;'.';,''...'l0KOxddxddl;..':lxxo:.'okkkxxdxxxxOKXXXXXKOkc.                   \n                 ....,''.''';clcccokkkkxoc;'''.';dkOOxdoooxKXX000000KXXXKXX0xdxkx:.                 \n                  .;c:;,',cdOOkxdolloddoc:,....:ool:,'.,coold0XK0OkxxxxxkkkxxkOO00l                 \n                  ;olc;:oOKK00OkxxkKKKOxoc,,'....',:lcclc:;';xOdc:::;;;:cldkO00KKX0,                \n                 .;'..,ok00K0OkkOOKXXKOdccccc::::dOx:oOolxo..,.         ..';oOXXXN0,                \n                      .':ddooccoodooxkdodkkxoldxdl:'.:c.ck;                  'xXXKd.                \n                      .dOOxdlc:;,,,lOOk0XKOdld00Ooc;;'..;:.                   .o0d.                 \n                     ;OXK0Odlcccc:l0X0KK0OxlckXxlx0Ox:....                     .:.                  \n                    ;xkxoc;';ldoloONNXK0kxddxkx,.cOKO,....                                          \n                    .......;xkxxdkKK0Oxo:cxOOOx;..,lo'...';,.                                       \n                     .,,'.:k0OkkkkxxdollclOKKK0l'..,;',,'':dko;.                                    \n                    .::;',xKKK0OOkOkkxxdddOXX0o,''',,,lOOkxxO0kd;.                                  \n                   .;;'..cKNXXX0xkKKK0OOkddkd:;,,....,,cx0K0Okdol:'.                                \n                   ..   'kK0Okdc;oXXXXKOxlllcccc:.......';::;,,,,,,,.                               \n                       .;:,':cc::o0KOxooxddddddd:.....'',,;,....',;:cc:,.                           \n                           .ldolloxdc::dOOOOOOko,...',,;;::c:'',,;:cc::c:'.                         \n                           .dkxdddoollco0KKKK0x:,,;,',;::clll:,;:cllll:,....                        \n                           .x0OOkkxxdc:ckXXNKxlcccc;..';:loodl::cloddxkkxl;:;'.                     \n                           .dXKK00Od;..cdOKKkdodo:,..',;:cll:cccoodxkkO0KKOolol'                    \n                            cXXXKx:'...'okOOkkkkc.  .';cloddc'';coxkO00KXXX0c',;.                   \n                            .kKx;.......'lO0000c. . ...':ldOOl,,;,,:lxOKXXXXO:                      \n                             :c.  .'''.. .,oOKd.   ......',:oo:;::'   ..,:codxc.                    \n                                   .'.  ....,c;.....  ..',,,;;:::cc.         ...                    \n                                         ..'..''.''.     ..',:cccloc.                               \n                                           .',,;,,'.         ..,:lod;                               \n                                             .';::;.             .,ll.                              \n                                                ....               ...  \u001b[0m")

    slow_text("\n""I am Speedtail, guardian of the rubalised crystal!"" Once the dust settles you see a magnificent golden eagle perched upon a throne \n\
with a mesmerising gem clutched in its razor sharp claws.\n\
""Sooo… you think you have what it takes to be the rightful master of the crystal?\n\
I, the mighty guardian of the rubalised crystal challenge you\n\
to the ultimate game of ""Hangruby"". Ahh... it's like hangman you say but guess the word wrong and i shall shatter this crystal\n\
in my grip, in turn washing away your hopes of ever fixing your jump-drive and returning to your planet! This'll be a cakewalk if you know anything about aviation.""")

    if initiate() == True:
        readout("You now have the Rubalised Crystal in your possession!")
        items_list.append("Rubalised Crystal")
        space_area()

    return

############################################################################################################################################
#Shaleem's Planet

points_sha = 0

def integer_check_sha(user_input, correct_answer):
    try:
        player_answer = int(user_input)
        if player_answer == correct_answer:
            readout(f"Well Done")
            global points_sha
            points_sha += 1
        #    readout(f"You have {points_sha} points.")
            return

        elif player_answer < 0 or player_answer > 2:
            integer_check_sha("Enter the number correctly. Please: ", correct_answer)
        else:
            readout(f"Wrong answer.")
        #    global wrong_answers_sha
        #    wrong_answers_sha += 1
    except ValueError:
        return
    
def multiple_choice_question_sha(question, option_0, option_1, option_2, correct_answer):
    readout(question)
    readout(f"Option 0: {option_0}")
    readout(f"Option 1: {option_1}")
    readout(f"Option 2: {option_2}")

    integer_check_sha(input("Choose your Answer, type 0 or 1 or 2: "), correct_answer)
    return

def octopus_planet():
    print(u"\u001b[34m\nMMMMMMMMMMMMWNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNKxc'.xMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMWWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdc;..  cXMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWWNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kdollc;,..    ..'lKWMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMWWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNWOldOXWMMMMMMMMMWXK0OOO0NMMMMMW0l'.          ...',lONNNWWMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNK:. .;cloddolc:,..    .'kXd:::.            ...,d0WMMWWNWWWMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWXx;.....              .oc ';.         ....;o0NMMMMMMMWWWNWWMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNOdc,.....'..       cd..Ok.       .';lkXWMMMMMMMMMMMMWWWWWMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkxlccc;,...   .xo lXk.     .;d0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Odl;.. .xc.x0x,    :0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdlx:.kkd:   '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX: dxll..''xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc :d;c'.;'cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMWc ,d,.. ;,.kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMNc .d;   ;: :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMN: .o,   ;c..dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWK; 'o,   ;l,.,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWW0, ;o.   ;lcl'oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx..ll    ;olO:,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX: 'o;    :doKo.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd..lc  .. cdoNk.cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..lc.     codWK,,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNKKNWNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXk; .lc.     .lokMN:.kMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKX0OKXKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo:::;.  ,o;       .co0MWl.xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWNXNXXNMMMMMMMMWNXK0OO0OkOKNWKOOkkkkOO00KKXWMMMMMMMMMMMMMMMMMMMMMMMW0,      'lc.   ..   ':xWMWo.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMWNXXXXKK0OkxdollddloO00K0Oxdooddddxxxxdoooccok0XNNWWWNNNWMMMMMMMMMMMMMMMMMMMMMMNd.     ,ll'    ,;.   .c0MMMo.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nNNWMMMMWWWNK00000OO00KKOxxoloddddddxk0XNXK0OkxddodO0OO0KKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMXx,    .col'    'do.    .xWMMWl.xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nX0OO0KKXXKKNNX0OkkkkO0KXXKKKNNNWNNKOO0NWNXKK00KNWMMMMMMWWWWWMMMMMMWWWWMMMMMMMMMMMMWNOl'   'cooc.    ,x0o.     cNMMMNc.kMMWWNWMMMMMMMMMMMMMMMMMMMMMMMMM\nMWN0kdoxkdloxxxk0KKXXXNNWMWNXKKXKXXkkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNWMMMMMMMWX0dc'. ':oxdc'    .;xNK:      ,KMMMMK,,KMMMWNNWWMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMN0OOxkKWWWWWWMMMMMMMMMWNXWMNKKKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXK0Oxdoc;...,cdkkd:.     .cONWk'      'OWWMMMk.cWMMMMMWWWNWMMMMMMMMMMMMMMMMMMMMM\nMMMMMMWXKXWMMMWWNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Okxdoolllccc::;;,'.''''';coxOOkdc'.     .,dKWW0:.      .kXNMMMWl.xMMMMMMMMWWNWWWMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMWKko:,..         ..',;:cloxO0000Okdc,.       .,lONMWKl.   .   'k0XWMMM0,;XMMMMMMMMMMWWNNWWMMWNNWMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMMMMWKd;.      .';cloxOOOOOOOkxdolc;'....        .,oONMMW0l.     .  ,kO0WMMMWl.xMMMMMMMMMMMMMWNNWWWNK0XWNXNWMMMMM\nMMMMMMMMMMMMMMMMMMMMWWNNWWMMMMMMMMMMMMMXx:.    .;ldxxxxdoc:;,'...             ..   .:d0WMMMXx:.         :xk0XWMMMk.cNMMMMMMMMMMMMMMWWNXXKOKNXXXOXMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWWNNWWWMMMMMMWXkc.    ,lxkxl;'.                         .':dO0KNMMXkc.   ..  .. .oxxOKNMMMK;,KMMMMMMMNXK0OOkkkOkkOOxdkxxxk0KXNWW\nMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNKOdlc;.    .cdxl,.                         .,;cdO0OdccxOxc'      ..  ..;ddxO0XWMMX:'OMMMMMMMWNNNNNNK0kdoccccdOKNWWXKKXNW\nMMMMMMMMMMMMMMMMMMMMMMMMMNOdc,.      .'cooc'                        .,cokOOOko:'. .;;.             'oddxkOKXWWXc'xWMMMMMMMMMMMMMMMWNNNXOOOXNXOdlloxkKN\nMMMMMMMMMMMMMMMMMMMMMWKxc'. .';:coooooo:.                      ':cloddoc;'.                 ...  'lddoxxk0KXWXc'xWMMMMMMMMMMMMMMMMWXK0kxxocllox0XWMMMM\nMMMMMMMMMMMMMMMMMMWXx:..;ldxxxxol:;'.  .,;:;,.                 ','..           ..     ..   .'..'lddoddxkO0KNK:'kWMMMMMMMMMMMMMMMMWXXKXKOOxd0NWMMMMMMMM\nMMMMMMMMMMMMMMMMNkc',ldxxl:'.        .cc:lodoodl.                             ...    ...    .;lddloodkkkOKXk,,OWMMMMMMMMMMMMMMMMMWNXXWWNXXNWMMMMMMMMMM\nMMMMMMMMMMMMMWKd;;lddc,.    ....''''.:l;:x0Oxl;lx;                               .  ...   ':oxololoxxxkO00d,cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW\nMMMMMMMMMMMW0l;cddc...,:ldkkkxxdddddodkoldOKWNc.ol                  .,'.       .''. ...,;cxocllldxddxkkOOc;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW\nMMMMMMMMMW0c,cxo;;cdO0Okoccccccccc:;,,'',:ldo:'lx'                .... .',.    .. .',;ldl:locoxdoddxkkOo;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMXo,lKNkloddl:ccldk0K0Odl:,,;,..:c,.,ccoxo:;.              ''..  ... ..,,,;ldo::ooclxxdoooddxOx:c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMM0, .::;,,,,cdOXWWKko;...,'.'oOxoloooolodoox0Oo'              .';clc::cldoc;:loccoxdoolooooxkxllONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMM0dlllodxO0XXKkdc,. .;;.'oOkocclxOkdodddxxxkO0K0d;.       .    .......';colcclddoolloooooxOxod0WWNNWMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMXxlc:;;,'..   ,:'.:xOxlccokOkolooxkkkkkOO000KNW0d,    .,.            ;lddlllooooooldkOxdkXMMMWWNNWWMMMMWNNXNMWNXKXMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMWk,.        ;c;;oxxl;;lk0OdloooxkxxddxxxkxkO0KXNNWNx'  .,,....         .cllllolllok00OOKWMMMWNXK000XNWMWXNW00XOxoodkOXMMMMMMMMMMMMMMMMMMMMMMMM\nWMMMMMMMMMN0kc. .;l:;cddocloxkdlllox0OkdddxxxkxddxkO0KKKXNWW0,  ....'.           ;ollld0XXKKXWMMMMMMWWXXK0OOkxxkxdoclodkOkxkodO0KXNWWMMMMMMMMMMMMMMMMM\nWMMMMMMMMMMMMWXx;..:lllcldxdooddxxddodddxkkkkkkkkO000KKKKXXNWKo;.    ...          .oXWWNNWWMMMMMMMMMMMMMMMMMNKOxxdxk0NMMWNKX0KNNNNWMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWKd:',cooooddxdddxxxxxxoodxxkkOOOOOOOOOOO00KXNNNXOc.  ',.   ...    .ckXWMMMMMMMMMMMMMMMMMWMMMMMMMMWNXKKKKXNWWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMWXOo:;:coodxxkkkxdddxkkOOOOOkkkxxxxkkOO0KKXNWWWWd.  .  .;,,;'.     .;cokKWMMMMMMMMWNX0OO0KKK0kxxddodkOKNWWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMWN0xlclllooodxOO00KK00OkkkkkkkkOO00KXXNNNWWMWx'    .....'.          .,o0WMMMMMMWXOxddxxxxxOOKNXOk0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxooodddddddddddddddddxxxxkO00KXNNWMMMXd:..      .             .l0WMMMMMMWNNMMMMNXK00KKkONMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0OOOkkkkkkkkOO00KKXNWWMMMMWWMMMWX0xol'    ..... ...     .ckNMMMMMMMMMMMMWNWNXKXWMMWWMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMWWNWWMMMWWMMMWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWMMMMMMMNO:.        ...       'cx0NMMMMWMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMWNNWWWMWWNXXKKKNMMMMMMMWWMMMMMMMMMMMMMWNXXNWMMWXKKNMMMMWWNWWWMMMMMMMW0o:;;;;,'.            .':lxOKWMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMWWWNWWMMNX0OOO0KXXXXKKXKO0KXK0KXX0xocc::cldxkOOkONNXKXWWWNNWWMMMMMMMMMWWMMWNKko:,...          .'c0MMMMMMMMMMMMMMWWNWWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMWWNNWWWMMWKOddolodlcooccodlclllcldkkkOkodocllccldk0NWMMWWNWWWWWMMMMMMMMMMMMMMMWNK0OkxxdddxxkOO0NMMMMMMMMMMMMMMMWWWWWWWMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMWWNNWWMWXXKXN0Oxxk0KXNWWNXKXKKKKKKKNXkKNKOkk0KNWMMMMMMMWWNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMWWNWWWWNNWMMWWWMMMMMMMMMMMWNXKXK0K0KWMMMMMMMMMMMMMMMMMMWWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNWWMMMMMMMMMMMMMM\nkkkkkkkkkkkkkkkkkkkkkxxxxxkkkkkkkkkkkkkkkkkkkkkkxdodkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxkkkkkkkkkkkkk\u001b[0m")
    message = "\nWelcome to Oceania, a world covered in water and ruled by the Whale Queen.\n\n\nUpon landing your craft on the water, you are greeted by a pod of dolphins.\nYou wear your diving helmet (which is equipped with a “universal language translator”), open the hatch and gently glide into the water. \n\nThe leader of the dolphins asks for the purpose of your visit to Oceania.\nYou explain the situation you and your crew are facing and ask if the dolphins would help you source the highly sought-after Ambergris.\nAmbergris is an essential component of the rocket-fuel which when added to the fuel provides enough thrust to the rockets to propel the craft through the wormhole.\nThe dolphin informs you that only the Whale Queen can give you Ambergris. Being highly sought after, special permission must be asked before anyone can have even a small piece of Ambergris.\nYou ask to see the Whale Queen, and the dolphin gestures you to follow it.\nAfter a short journey you arrive at a beautiful lagoon. This is where the Whale Queen holds court, and upon your arrival you are taken directly to meet her.\n\nYou respectfully address the Whale Queen and explain that you are there to source Ambergris for your rocket engines. The Whale Queen is sympathetic to your story, BUT….\n\nBefore anyone can possess the sacred Ambergris, one must prove to the residents of Oceania that they are worthy of owning Ambergris.\n\nYou may prove your worth by answering these three questions correctly:\n\n"
    for char in message:
        sys.stdout.write (char)
        sys.stdout.flush()
        time.sleep(0.005)
        if char != "\n":
            time.sleep(0.005)
        else:
            time.sleep(0.05)

    multiple_choice_question_sha("Your first question is:\nWhat is the largest mammal on your home planet Earth?", "Blue Whale", "Great White Shark", "Giant Squid",0)
    print ("\n")
    multiple_choice_question_sha("Your second question is:\nWhich of these sea creatures has the longest life-span?", "Loch Ness Monster", "Iceland Sharks", "Jellyfish",2)
    print ("\n")
    multiple_choice_question_sha("Your third question is:\nWhat is more?", "Number of stars in the Milky Way Galaxy", "Pieces of plastic in Earth's Oceans", "Hair on a human's head",1)
    print ("\n")
    global points_sha
    if points_sha >= 1:
        readout(f"Congratulations!\nYou have proven that you are worthy of owning Ambergris.\n\nThe Whale Queen presents you with a large piece of Ambergris and instructs the dolphins to escort you back to your spaceship.\n\nNow you can continue your journey to the other planets.")
        items_list.append("Ambergris")
        space_area()
    return

############################################################################################################################################
planet_functions = {0: human_planet, 1 : cat_planet, 2 : toad_planet, 3 : vulcan_planet, 5 : viper_planet , 4 : octopus_planet}
############################################################################################################################################

if __name__ == '__main__':
    character_setup()