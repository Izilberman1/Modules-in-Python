from random import randint

# Generate a number from 1 to 10.
answer = randint(1, 10)

# Get input from user.


# Check that input is a number between 1 and 10.
while True:
    try:
        guess = int(input("Guess a number between 1 and 10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a GENIUS!")
                break
            print("All good")
            break
        else:
            print("Hey, bozo I said between 1 and 10")
    except ValueError:
            print("Please enter a number")
            continue
# Check if the number is the correct guess, otherwise ask again.

