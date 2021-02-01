##############
### Room 4 ###
##############


def treadmill():
    print('Batman examines the treadmill, the screen is now showing "??? press play to start the game ???')
    # Batman presses "play". During the video call Riddler gives Batman another riddle and tells him that if he select the correct answer, Riddler will give a hint where to find a piece of the passord
    # Scenario 1 - wrong answer - people in a place in Gotham die (could be a public event) /// game over
    # Scenario 2 - correct answer - here's my hint Batman: TIME is running up! - batman goes back to choices
    user_choice = input(">> ").lower()
    if user_choice == "a":
        print("People die. Game Over")
    elif user_choice == "b":
        print("People die. Game Over")
    else:
        print("Correct. Yout TIME is running up")
        room4()

def phone():
    print("Batman answers the phone, speaks with Riddler and finds out that Riddler’s left the building and he’s got the software - GAME OVER")

def clock():
    print("Batman’s analyses the hands of the clock in detail and spots an engraved “?” symbol on one of them. On the backside of the hand with Riddler’s symbol, Batman finds a part of the access code to Room 6.")
    room1()

def choices():
    print("Batman tries to find a clue, looks around and sees:\n ")
    print('A. A treadmill with "?" symbol on the screen\nB. A ringing phone on the desk.\nC. A vintage clock above the desk.')
    
def go_back():
    room1()

def room4():
    stay_leave = input('Type "i" to investigate the room or "q" to go back:\n>> ').lower()
    if stay_leave == "i":
        print("Batman sees a riddle painted on the wall.\n")
        print("I run a dozen times faster than him,\nHe runs all day, twice around the gym.\nWho are we?\n")

        choices()
        choice = input(">> ").lower()

        if choice == "a":
            treadmill()
        elif choice == "b":
            phone()
        else:
            clock()
    else:
        go_back()


print("Batman enters the company’s gym.\n")

room4()

