import random

def spin_roulette():
    """имитирует вращение рулетки и выбирает случайный номер(0-36)."""
    return random.randint(0, 36)

def get_player_bet(current_balance):
    """спрашивает у пользователя сумму ставки и число на которое ставит"""
    while True:
        try:
            print(f"\nВаш текущий баланс: {current_balance}$")
            bet_amount_str = input("Введите сумму ставки: $")
            bet_amount = int(bet_amount_str)

            if bet_amount <= 0:
                print("Сумма ставки должна быть положительной.")
            elif bet_amount > current_balance:
                print("Недостаточно средств на балансе.")
            else:
                break # сумма ставки корректна

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число для суммы ставки.")

    while True:
        try:
            bet_number_str = input("Введите номер, на который ставите (от 0 до 36): ")
            bet_number = int(bet_number_str)

            if 0 <= bet_number <= 36:
                break # номер ставки корректен
            else:
                print("Неверный номер. Пожалуйста, введите число от 0 до 36.")

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число для номера ставки.")

    return bet_amount, bet_number

def calculate_result(bet_amount, bet_number, winning_number):
    """Определяет результат раунда и возвращает изменение баланса."""
    print(f"\nРулетка крутится... Выпал номер: {winning_number}")

    if bet_number == winning_number:
        # выигрыш при ставке на номер: 35 к 1
        winnings = bet_amount * 35
        print(f"Поздравляем! Вы выиграли {winnings}$.")
        return winnings
    else:
        loss = -bet_amount
        print(f"К сожалению, вы проиграли {bet_amount}$.")
        return loss

def main():
    """Основная функция игры."""
    balance = 12000 # стартовый балик

    print("Добро пожаловать в простую рулетку!")
    print("Ставка на один номер платит 35 к 1.")

    while balance > 0:
        bet_amount, bet_number = get_player_bet(balance)

        # уменьшаем баланс на сумму ставки сразу
        balance -= bet_amount
        print(f"Ваша ставка {bet_amount}$ на номер {bet_number} принята.")
        print(f"Оставшийся баланс до результата: {balance}$")


        winning_number = spin_roulette()
        change_in_balance = calculate_result(bet_amount, bet_number, winning_number)

        # прибавляем выигрыш (если пользователь угадал)
        balance += change_in_balance # change_in_balance уже содержит -bet_amount + winnings или просто -bet_amount

        print(f"Ваш новый баланс: {balance}$")

        if balance <= 0:
            print("\nУ вас закончились деньги. Игра окончена.")
            break

        play_again = input("Хотите сыграть еще? (да/нет): ").lower()
        if play_again != 'да':
            print("\nСпасибо за игру!")
            break

    print("\nДо свидания!")

# заапускаем игру
if __name__ == "__main__":
    main()
