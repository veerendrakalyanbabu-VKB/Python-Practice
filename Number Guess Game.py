import random

secret_number = random.randint(1, 10)

print("\n==============================")
print("      NUMBER GUESS GAME")
print("==============================")

print("Made by Veerendra 🚀")

attempts = 5

while attempts > 0:

    try:
        guess = int(input("\nGuess a number between 1 and 10: "))

        if guess == secret_number:
            print("\n🎉 Congratulations! Correct Guess!")
            break

        else:
            attempts -= 1

            if attempts > 0:
                print(f"\n❌ Wrong Guess. Attempts Left: {attempts}")

            else:
                print(f"\n💀 Game Over! Correct number was {secret_number}")

    except ValueError:
        print("\n❌ Please enter numbers only")