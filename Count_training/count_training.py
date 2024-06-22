import random

lowDiapazon  = 10
highDiapazon = 100
sign         = 0
playGame     = True
count        = 0
right        = 0
score        = 0

print("""The computer compiles an example. Enter your answer.
To exit, enter STOP""")
print("*" * 40)

while playGame:
    print(f"Current score: {score}")
    print(f"Tasks processed: {count}")
    print(f"Right answers: {right}")
    print("-" * 40)

    sign = random.randint(0, 3)

    if sign == 0:
        z = random.randint(lowDiapazon, highDiapazon)
        x = random.randint(lowDiapazon, highDiapazon)
        y = z - x

        if random.randint(0, 1) == 0:
            print(f"{x} + {y} = ?")
        else:
            print(f"{y} + {x} = ?")
    elif sign == 1:
        x = random.randint(lowDiapazon, highDiapazon)
        y = random.randint(0, x - lowDiapazon)
        z = x - y
        print(f"{x} - {y} = ?")
    elif sign == 2:
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        z = x * y
        print(f"{x} * {y} = ?")
    elif sign == 3:
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10))
        y = random.randint(lowDiapazon, highDiapazon) // x

        if y == 0:
            y = 1
        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")

    user = ""

    while (not user.isdigit() and user.upper() != "STOP"): 
        user = input("Enter your answer: ")

        if (user.upper() == "HELP"):
            if z > 9:
                print(f"Last digit of the answer: {z % 10}") 
            else:
                print("The answer consists of one number. Hint not possible.")
            score -= 10
        elif (user.upper() == "STOP"):
            playGame = False 
        else:
            if user.isdigit():
                count += 1
                if int(user) == z:
                    print("\nRight!\n")
                    right += 1
                    score += 10
                else:
                    print(f"\nThe answe wrong... Right answer: {z}\n")
                    print(f"\nYou can enter the command HELP to see the last digit of the answer (score - 10).\n")
                    score -= 20
            else:
                print("Invalid input. Please enter a number.")

print("*" * 45)
print("GAME STATISTICS:")
print(f"    Tasks processed: {count}")
print(f"    Right answers: {right}")
print(f"    Your final score: {score}")

if count > 0:
    print(f"    Percentage of correct answers: {int(right / count * 100)}%")
else:
    print("No tasks processed.")
