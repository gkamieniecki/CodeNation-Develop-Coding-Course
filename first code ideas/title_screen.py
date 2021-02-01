from art import logo_art


def start():
    
    # print(title_art)
    print(logo_art)
    print("Welcome to Batman: Stuck in the Riddle!\n")

    start_game = input('Type "s" to start the game or "q" to quit the game: ').lower()

    if start_game == "s":
        room1()
    elif start_game == "q":
        print("Goodbye")
    else:
        print("Try again.")
        start()

start()