import random, sys, time, os

def slow_text (string):
    
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)
    return

def yes_or_no(question):
    answer = input(question + " (Enter 'yes' to continue or 'no' to chicken out): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + " (Enter 'yes' to continue or 'no' to chicken out):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

def vulcan_planet():

    slow_text (f"Greetings {player_name}.\n\
You have traversed the vast void of deep space and have entered the unforgiving atmosphere of \n\
the planet Vulcan.\n\
You are met with howling supersonic winds and treacherous mountains that could overshadow Everest.\n\
This land is rampant with superfast flying beasts that could shred you up should they be alerted to your presence\n\
You have embarked on a daring mission to find the elusive temple of the rubalised crystal.\n\
The high winds and low visibility make it almost impossible for you to navigate the terrain.\n\
Many have tried and met their demise... this is your only shot to aquire the fabled crystal in order\n\
to recreate a wormhole in the fabric of space-time so you can get back home.")
    if yes_or_no(" Now would be a good time to turn back \n\
or are you willing to risk it?"):
        print("So... you have chosen death! let's continue")
    else:
        print("Did you really think you could leave now?! let's continue")

    slow_text ("After treading the desolate landscape for what seems to be an eternity\n\
your space rover's navigation instrument starts to chime indicating you have arrived at the temple of the guardian.\n\
this is where the rubalised crystal is being protected! You exit your rover and with the help of your\n\
anchor boots claw your way to a green shadowy hue.\n\
Oh great... this appears to be a keypad next to the stone entrance.\n\
you will have to answer the riddle below correctly, in order to disarm the forcefield so you can enter the temple.\n\
Do hurry... we don't have much time, this planet's core is very unstable and could collapse in on itself.")
#could make a game_over for planet exploding after attempts

    attempt=0

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
            print ("I can be a source of relaxation")

        elif ans == 'another clue':
            print("I'm pretty bright and waxy")

        elif ans == "I'm too dumb":
            print ('Ha Ha... I knew you didnt have it in you')
            print("You return to your spacecraft.")
            animal_galaxy.space_area()
            break

        else: 
            print ("Don't you want the crystal? Give it another go!")

    slow_text ("As you enter the great temple you begin to marvel at the grandeur.\n\
The atmosphere inside is eerie and silent,\n\
a stark contrast to the world outside.\n\
you see a huge shadow pass over you at blinding speed leaving you disorientated by the plumes of volcanic dust \n\
now surrounding you. you hear a thunderous voice echo through the temple - \n\
""I am Speedtail, guardian of the rubalised crystal!"" Once the dust settles you see a magnificent golden eagle perched upon a throne \n\
with a mesmerising gem clutched in its razor sharp claws.\n\
""Sooo… you think you have what it takes to be the rightful master of the crystal?\n\
I, the mighty guardian of the rubalised crystal challenge you\n\
to the ultimate game of ""Hangruby"". Ahh... it's like hangman you say but guess the word wrong and i shall shatter this crystal\n\
in my grip, in turn washing away your hopes of ever fixing your jump-drive and returning to your planet!""")

    ###Until hangman finished -Sha
    print("However, he drops it on the ground and you take it.")
    animal_galaxy.items_list.append("Rubalised Crystal")
    animal_galaxy.space_area()

    return

#vulcan_planet()



#still working on adding the hangman game in , i will integrate it this evening in my own time
# as im working on it still - but if player is successful
# this will be displayed - If hangman is completed successfully -
#  “you have earned the estemed rank - “master of the Rubalised crystal”.
#  The guardian eagle is impressed. He will now beam you back to your spaceship in a blink of an eye”.
