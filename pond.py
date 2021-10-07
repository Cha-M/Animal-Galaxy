import random, sys, time, os

ttt_board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Define the print_ttt_board function
def print_ttt_board():
    global ttt_board
    print(f"   ╻   ╻   \n {ttt_board[1]} ┃ {ttt_board[2]} ┃ {ttt_board[3]} \n   ┃   ┃   \n╺━━╋━━━╋━━╸\n   ┃   ┃   \n {ttt_board[4]} ┃ {ttt_board[5]} ┃ {ttt_board[6]} \n   ┃   ┃   \n╺━━╋━━━╋━━╸\n   ┃   ┃   \n {ttt_board[7]} ┃ {ttt_board[8]} ┃ {ttt_board[9]} \n   ╹   ╹    ")
    
def player_turn():
    global ttt_board
    choice = input("Please choose a corresponding number 1-9 to place your X. ")
    choice = int(choice)
    if ttt_board[choice] in "123456789":
        ttt_board[choice] = "X"
    else:
            print("Sorry, that space is not empty!")
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
            print("The Glorious Toad Nation is victorious!! No exotic drive cooling fluid for you sorry, old chum.")
            animal_galaxy.space_area()
        elif winner("X"):
            print("Congratulations! You have emerged victorious against our greatest champion, you have secured the precious exotic drive cooling fluid.\nGood luck on your journey and go with the blessing of the great Toad Nation.")
            animal_galaxy.items_list.append("Exotic Drive Cooling Fluid")
            animal_galaxy.space_area()
    return            

def toad_planet():
    print ("Descending through the atmosphere, the finer details of a vast and wonderful world are slowly revealed to you.\nWhat at first appeared to be continent sized landmasses are, in fact, unbelievably huge lily pads.\nThese continent sized water lilies are all connected by a series of smaller (yet still gigantic) lilies, presumably for travel and transportation. \n Upon the largest of these enormous lilies lies a sprawling metropolis and as you get even closer to the surface, you can truly appreciate the scale of the place.\nThe castle at the heart of the metropolis is hundreds of kilometres wide and as you descend past its highest tower you check your altitude meter which says you're still 2000m from sea level!\nApproaching the surface you can finally start to make out the inhabitants of this strange new world.\nThey are Gigantic Toads and they are happily hopping about their daily business\n200m from the surface, one of them jumps straight up and passes by your ship window, smiling and waving his suitably giant top hat at you.\nWell they seem friendly at least, you think before landing at the gates of the impressive castle.\nUpon exiting your craft you are greeted by an opulently dressed Giant Toad..\n'Greetings brave space hopper, what brings you to the fair world of Pond and to the gates of the great castle Jumpalot, The beating heart of the Glorious Toad Nation?'\nYou explain that in order to get back home you need to obtain 3 litres of exotic drive cooling fluid, and you'd detected some on this planet\n'Of course we would be more than hoppy to help but as is our way, you must first defeat our champion at our national pastime, TicTacToad, before you can claim your prize!'\n")
    print ("How to play!- Players take turns marking the spaces in the 3×3 grid. \nThe grid is numbered 1-9 reading from the top left to bottom right respectively.\nThe player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.")
    toad_game()
    return

#toad_planet()

