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
    print("What is always in front of you but can't be seen?")
    riddle_time_answer = str(input("Please enter your answer:").lower())
    if riddle_time_answer.lower().find(answer) > -1:
        print("Yey!")
        viper_reward()
        return
    elif riddle_time_answer.lower().find(answer) == -1:
        print("Try 1 more time.")
        #need countdown for limited times
        viper_riddle()
        return
    else:
        print("You are nearly there")
        viper_riddle()
        return
        
    return


def player_yes_no():
        
        player_yes_no_string = str(input("Please enter yes or no:"))
        if player_yes_no_string.lower()[0] == "y":
            print("Yes")
            #linked this function to the other
            viper_riddle()
        elif player_yes_no_string.lower()[0] == "n":
            print("No")
            print("You return to your spacecraft.")
            animal_galaxy.space_area()
        else:
            player_yes_no()
        return

def viper_reward():
    print("Here is your reward. This Infinity Banana will last you all the way back to your home planet.")
    animal_galaxy.items_list.append("Infinity Banana")
    animal_galaxy.space_area()
    
    message=("         @@@@(@(@@                                                 *****   ,***\n  **   **,@@@@((///&@                                              *** *** .****\n  ,*****,     %@@%**,*@                                             *****    ***\n                  @@,..%(,*%@@@@@@@,          . .                               \n                   ,@@/.............@@@&                                        \n                   @@//*../.......//...*@@                                      \n                  @@/./@..................@@                                    \n                  @@/..@%...................@@                                  \n                  @@/...&,...................@@@                                \n                  @@/.....@.....*@@@@&.*@@@@@..@@                @@@@@          \n                  ,@&/.... ...&@.............@..@@               @@   .@        \n                   @%/.,......@..@,   @.@  @.....@@               &&..@@@@@@@@@@\n                    ((/.........@     /.&   @.....@@             @     ,/      .\n                     @@/.......&*(@,  @.&//*/......@@          @.@        .@@@% \n                     .@@/.......@@@@ /%.@@@*@.......@@         @@  @@,        *@\n                      ,@(/.......@@@@..........@.....@*     @@%../@@@@@         \n                       *@//....@@............@.......@@@@@&...*/@@              \n        @@  @           (@(,.....*@/...(@@   @........@@...*/@@,                \n       @    @            &@/.....,@@ .@@@@@@..........@@/@@@                    \n       *@     @@        . @@/......@@@@@@@@@..........(@                        \n     @@  @      @ @@  .@@..@@*.......@*******@.........@*                       \n  @@ @.   @    ,@ @*.....,/&@(..........**.............@@                       \n @@    /.     @,&@@@@@@@@@  @@/........................@@                       \n @   @    *@%               .@/.......................%@*                       \n  @@  ,,                     @&, .....................@@                        \n                             @@.......................@@                        \n                             @@.../..................@@                         \n                            @@(...@...........,,,...@@%                         \n                            @@/../@................,@@                          \n                            @@,..//.............../@@                           \n                           @@/../@...............&@/                            \n                          @@%,./&../............@@                              \n                         /@@/.//@............./@@                               \n                         @@/,//@.........././@@                                 \n                        @@////@...........*/@/                                  \n.                       @@/*/@.*/......./(@/                        . .         \n                        @@//&...../..,/@@                                       \n                         @@/.....,//@@                                          \n                         @%&//(@@@/                             ")
    for x in message:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)


def viper_planet():
    viper_introduction()
    player_yes_no()
    return

#viper_planet()
      
