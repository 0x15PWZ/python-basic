secret = 5
guess = 0

while guess != secret:
    guess = int(input("Guess number (1-10): "))
    if guess == secret:
        print("Correct!")
    else:
        print("Try again.")
