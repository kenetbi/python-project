import random, time

def truth_questions():
    truths = ["What is the most embarrassing thing you've done this week?",
    "Have you ever lied about your age to get into something?",
    "What is your biggest fear?",
    "What is a secret you've never told anyone here?"]
    selected = random.choice(truths)
    print("")
    print(selected)
    time.sleep(1)
    input("\nPress enter once the player have answered...") 

def dare_command():
    dares = ["Do 10 push-ups right now.",
    "Sing the chorus of your favorite song out loud.",
    "Show the last text message you sent to someone.",
    "Speak in an accent for the next two rounds."]
    selected = random.choice(dares)
    print("")
    print(selected)
    time.sleep(1)
    input("\nPress enter once the player already did it...")

players = ["Kenneth","Kristian","Karl","Karen","Kaide"]
is_playing = True

while is_playing:
    print("\nSpinning the bottle...")
    time.sleep(2)
    player_turn = random.choice(players)

    player_chosen = True
    while player_chosen:
        print(f"\nIt is {player_turn}'s turn!")
        selection = input("Choose 'truth' or 'dare': ").lower().strip()

        if selection == "truth":
            truth_questions()
            player_chosen = False
        elif selection == "dare":
            dare_command()
            player_chosen = False
        else:
            print("Invalid input!")