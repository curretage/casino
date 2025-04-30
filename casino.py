import random

def spin_roulette():
    """simulates a roulette spin and returns a random winning number (0-36)."""
    return random.randint(0, 36)

def get_player_bet(current_balance):
    """prompts the player for the bet amount and the number they are betting on."""
    while True:
        try:
            print(f"\nYour current balance: {current_balance}$")
            bet_amount_str = input("Enter your bet amount: $")
            bet_amount = int(bet_amount_str)

            if bet_amount <= 0:
                print("Bet amount must be positive.")
            elif bet_amount > current_balance:
                print("Insufficient funds.")
            else:
                break # bet amount is valid

        except ValueError:
            print("Invalid input. Please enter an integer for the bet amount.")

    while True:
        try:
            bet_number_str = input("Enter the number you want to bet on (0 to 36): ")
            bet_number = int(bet_number_str)

            if 0 <= bet_number <= 36:
                break # bet number is valid
            else:
                print("Invalid number. Please enter a number between 0 and 36.")

        except ValueError:
            print("Invalid input. Please enter an integer for the bet number.")

    return bet_amount, bet_number

def calculate_result(bet_amount, bet_number, winning_number):
    """Determines the round result and returns the change in balance."""
    print(f"\nRoulette spinning... The winning number is: {winning_number}")

    if bet_number == winning_number:
        # payout for betting on a single number: 35 to 1
        winnings = bet_amount * 35
        print(f"Congratulations! You won {winnings}$.")
        return winnings
    else:
        loss = -bet_amount
        print(f"Sorry, you lost {bet_amount}$.")
        return loss

def main():
    """Main game function."""
    balance = 1000 # starting balance

    print("Welcome to Simple Roulette!")
    print("Betting on a single number pays 35 to 1.")

    while balance > 0:
        bet_amount, bet_number = get_player_bet(balance)

        # deduct the bet amount immediately from the balance
        balance -= bet_amount
        print(f"Your bet of {bet_amount}$ on number {bet_number} is placed.")
        print(f"Remaining balance before result: {balance}$")


        winning_number = spin_roulette()
        change_in_balance = calculate_result(bet_amount, bet_number, winning_number)

        # add winnings (if user won)
        # change_in_balance already contains -bet_amount + winnings or just -bet_amount
        balance += change_in_balance

        print(f"Your new balance: {balance}$")

        if balance <= 0:
            print("\nYou ran out of money. Game over.")
            break

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

    print("\nGoodbye!")

# run
if __name__ == "__main__":
    main()
