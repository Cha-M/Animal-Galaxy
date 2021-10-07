import random, sys, time, os

points_sha = 0

def integer_check_sha(user_input, correct_answer):
    try:
        player_answer = int(user_input)
        if player_answer == correct_answer:
            print(f"Well Done")
            global points_sha
            points_sha += 1
        #    print(f"You have {points_sha} points.")
            return

        elif player_answer < 0 or player_answer > 2:
            integer_check_sha("Enter the number correctly. Please: ", correct_answer)
        else:
            print(f"Wrong answer.")
        #    global wrong_answers_sha
        #    wrong_answers_sha += 1
    except ValueError:
        return
    
def multiple_choice_question_sha(question, option_0, option_1, option_2, correct_answer):
    print(question)
    print(f"Option 0: {option_0}")
    print(f"Option 1: {option_1}")
    print(f"Option 2: {option_2}")

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
        print(f"Congratulations!\nYou have proven that you are worthy of owning Ambergris.\n\nThe Whale Queen presents you with a large piece of Ambergris and instructs the dolphins to escort you back to your spaceship.\n\nNow you can continue your journey to the other planets.")
        animal_galaxy.items_list.append("Ambergris")
        animal_galaxy.space_area()
    return
