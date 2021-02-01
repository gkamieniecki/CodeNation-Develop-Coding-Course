##############
### Room 5 ###
##############


def correct_answer():
    print("Correct answer. The part of the access code is revealed on the laptop's screen.")
    room5()

def choices5():
    print('1 Server rack\n2 USB stick\n3 Cup\n4 Bomb\n5 Keys')
    
def go_back():
    room1()

def room5():
    print("Batman finds the riddle.\n")
    print("There is a bomb on top of the first server rack. Around the rack there is also a usb stick, a cup, keys and a pen. When the explosion comes which item is destroyed first? Use the laptop on the desk to type your answer.\n")

    choices5()
    choice = input(">> ").lower()

    if choice == "1":
        print("Wrong answer.")
    elif choice == "2":
        print("Wrong answer.")
    elif choice == "3":
        print("Wrong answer.")
    elif choice == "4":
        print("Correct answer")
    elif choice == "5":
        print("Wrong answer.")
    else:
        print("Not a valid option")
        room5()
    
print("Batman enters the server room.\n")

room5()

