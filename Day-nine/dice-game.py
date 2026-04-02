import random

def dice_game():
    score = 0

    print("🎲 Dice Game Started!")

    while True:
        choice = input("\nRoll dice? (y/n): ").lower()

        if choice != "y":
            break

        dice = random.randint(1, 6)
        print(f"🎲 You rolled: {dice}")

        if dice == 1:
            print("💀 You rolled 1! Game over.")
            score = 0
            break
        else:
            score += dice
            print(f"✅ Score: {score}")

    print(f"\n🏁 Final Score: {score}")

dice_game()