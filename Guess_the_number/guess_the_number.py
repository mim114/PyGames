import random

lowDigit     = 10    # lower limit of random digit
highDigit    = 50    # upper limit of random digit
digit        = 0     # hidden number
countInput   = 0     # count of user's attempts
win          = False # flag to check if the user wins
playGame     = True  # flag to continue playing the game
playerNumber = 0     # user's guess
startScore   = 100   # initial score
score        = 0     # current score
maxScore     = 0     # maximum score

while playGame:
    countInput = 0
    score      = startScore
    digit      = random.randint(lowDigit, highDigit)

    #print(digit) # hint
    print("-" * 50)
    print("The computer has guessed a number, try to guess it.")

    while not win and score > 0:
        print("-" * 50)
        print(f"Current score: {score}")
        print(f"Record score:  {maxScore}")
        playerNumber = ""

        while not playerNumber.isdigit():
            playerNumber = input(f"Enter your guess (between {lowDigit} and {highDigit}): ")

            if not playerNumber.isdigit():
                print("." * 27 + "Invalid input. Please enter a number.")
            
        playerNumber = int(playerNumber)

        if playerNumber == digit:
            win = True
        else:
            length = abs(playerNumber - digit)
            if length < 3:
                print(" " * 50, "Very hote!")
            elif length < 5:
                print(" " * 50, "Hot!")
            elif length < 10:
                print(" " * 50, "Warm!")
            elif length < 15:
                print(" " * 50, "Chilly!")
            elif length < 20:
                print(" " * 50, "Cold!")
            else:
                print(" " * 50, "Very cold!")

            if countInput == 7:
                score -= 10

                if digit % 2 == 0:
                    print(" " * 50, "Even number!")
                else:
                    print(" " * 50, "Odd number!")
            elif countInput == 6:
                score -= 8
                if digit % 3 == 0:
                    print(" " * 50 , "Divisible by 3!")
                else:
                    print(" " * 50, "Not divisible by 3!")
            elif countInput == 5:
                score -= 4
                if digit % 4 == 0:
                    print(" " * 50, "Divisible by 4!")
                else:
                    print(" " * 50, "Not divisible by 4!")
            elif countInput > 2 and countInput < 5:
                score -= 2
                if playerNumber > digit:
                    print(" " * 50, "The hidden number is LESS than your guess.")
                else:
                    print(" " * 50, "The hidden number is GREATER than your guess.")
            score -= 5
        countInput += 1
    print("*" * 40)    

    if playerNumber == digit:
        print(f"Congratulations! You guessed the hidden number {digit} correctly.")
        print(f"Your final score: {score}")
    else:
        print(f"Sorry, but you couldn't guess the hidden number {digit}.")
        print(f"Your final score: {score}")

    if input("Enter - to play again, 0 - exit: ") == "0":
        playGame = False
    else:
        win = False

    if score > maxScore:
        maxScore = score


print("*" * 40)
print("Game over.")
