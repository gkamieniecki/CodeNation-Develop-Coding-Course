#################################
### Activities and Challenges ###
#################################

# Activity 1
# Displays 4 films stored in an array
# Use a for loop to show each film in the array
# Create a function called film_check() that checks if the 3rd film in the array is Ghostbusters.
# If it is, it should return "yey it's ghostbusters". If it isn't, it should return "booo, we want ghostbusters"
 

def activity1():

    film_list = ["batman", "superman", "spider-man", "iron-man"]

    for film in film_list:
        print(film)

    def film_check():
        if film_list[2] == "Ghostbusters":
            print("yey it's ghostbusters")
        else:
            print("booo, we want ghostbusters") 


# Activity 2

# Create a variable count, and a while loop to display count from 0 to 9,
# stop the while loop when the count reaches 10.

def activity2():
    count = 0

    while count < 10:
        for n in range(0, 11):
            count = n
            print(count)


# Activity 3
# 
# Create a variable, generate a random number between 1 and 30 six times, 
# each random number generated, check if this number is divisible by 7 or not.


def activity3():
    import random
    
    def check(number):
        if number % 7 == 0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} isn't divisible by 7")

    for n in range(6):
        n = random.randint(1, 30)
        check(n)
    

# Activity 4

# Create a program that check all numbers between 1 and 20, 
# whether it is a prime number or not.


        


# Challenge 1

# Head or tails game
# must be inside a function and must use random library

def challenge1():
    
    import random

    def start_game():
        heads_tails = ["Heads", "Tails"]
        ask_user = input("Heads or Tails?: ").title()
        result = random.choice(heads_tails)

        if ask_user == result:
            print(f"{result}! You win.")
        else:
            print(f"{result}! You lose.")
        
        try_again = input('Do you want to play again? Type "yes" or "no": ').lower()

        if try_again == "yes":
            start_game()
        else:
            print("Goodbye.")


# Challenge 2

# Create a variable called grade. Create a mark scheme for a school based on marks out of 100.
# If my grade is below 25 I get an F
# Between 25 and 44 - E
# Between 45 and 49 - D
# Between 50 and 59 - C
# Between 60 and 79 - B
# 80 or over - A

def challenge2():
    
    def mark_scheme(score):
        if score < 25:
            print(f"Your grade: F")
        elif score >= 25 and score < 44:
            print(f"Your grade: E")
        elif score >= 45 and score < 49:
            print(f"Your grade: D")
        elif score >= 50 and score < 59:
            print(f"Your grade: C")
        elif score >= 60 and score < 79:
            print(f"Your grade: B")
        else:
            print(f"Your grade: A")

    user_score = int(input("What's your score? "))

    mark_scheme(user_score)


# Challenge 3

# Make a variable called tile, give that a letter. 
# Create a program that explains how many points your letter is worth in a game of Scrabble.

# 0 Points - Blank tile.
# 1 Point - A, E, I, L, N, O, R, S, T and U.
# 2 Points - D and G.
# 3 Points - B, C, M and P.
# 4 Points - F, H, V, W and Y.
# 5 Points - K.
# 8 Points - J and X.
# 10 Points - Q and Z.


def challenge3():
    user_letter = input("What's your letter?: ").upper()
    user_points = 0

    pts0 = [" "]
    pts1 = ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"]
    pts2 = ["D", "G"]
    pts3 = ["B", "C", "M", "P"]
    pts4 = ["F", "H", "V", "W", "Y"]
    pts5 = ["K"]
    pts8 = ["J", "X"]
    pts10 = ["Q", "Z"]

    if user_letter in pts0:
        user_points += 0
    elif user_letter in pts1:
        user_points += 1
    elif user_letter in pts2:
        user_points += 2
    elif user_letter in pts3:
        user_points += 3
    elif user_letter in pts4:
        user_points += 4
    elif user_letter in pts5:
        user_points += 5
    elif user_letter in pts8:
        user_points += 8
    elif user_letter in pts10:
        user_points += 10

    print(f"Your letter is worth {user_points} points.")



# Challenge 4

# Create a loop that asks a user to input a number, 
# then displays the times table/multiplication table for that number (up to 12) e.g. if i input 1, I should see:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# 1 x 11 = 11
# 1 x 12 = 12
# it should start again and ask the user for a new number every time it finishes.

def table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
        
quit = False
while not quit:        
    user_number = input('Enter a number or type "q" to quit: ')
    if user_number == "q":
        quit = True
        print("Goodbye")
    else:
        user_number = int(user_number)
        table(user_number)

         


