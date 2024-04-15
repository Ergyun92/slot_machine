import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLUMNS = 3

symbols_counting = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            elif amount == 0:
                print("Amount has to be greater than 0.")
        else:
            print("Invalid entry. Please enter a valid sum")
    return amount


def pick_lines():
    while True:
        lines = input("On how many lines would you like to bet on(1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if lines not in range(1, MAX_LINES + 1):
                print("You have to pick between 1-3")
            else:
                break
        else:
            print("You have to enter a valid number")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line?: ")
        if bet.isdigit():
            bet = int(bet)
            if bet in range(MIN_BET, MAX_BET + 1):
                break
            elif bet < MIN_BET or bet > MAX_BET:
                print(f"You must bet between {MIN_BET} and {MAX_BET}")
        else:
            print("You have to enter a valid number")
    return bet


def spin_slot_machine(rows, columns, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    cols = []
    for _ in range(columns):
        col = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            col.append(value)
        cols.append(col)
    return cols


def show_slot_machine(cols):
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            if i != len(cols) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def check_winnings(cols, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = cols[0][line]
        for col in cols:
            winning_symbol = col[line]
            if symbol != winning_symbol:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spinning(balance):
    lines = pick_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount.(balance = ${balance}")
        else:
            break
    print(f"Your bet is ${bet} on {lines} lines. Total bet = ${total_bet}")
    slots = spin_slot_machine(ROWS, COLUMNS, symbols_counting)
    show_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}!")
    print(f"You have won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    amount = deposit()
    while True:
        print(f"Current balance is ${amount}")
        play_again = input("Press Enter to continue or q to quit")
        if play_again.lower() == 'q':
            break
        amount += spinning(amount)
    print(f"You ended up with ${amount}.")


main()
