import random

ROWS = 3
COLUMNS = 3
MAX_LINES = 3

symbol_count = {
    "*" : 3,
    "+" : 3,
    "/" : 3,
    "-" : 3,
    "%" : 3,
    "^" : 3
}
symbol_values = {
    "*" : 2,
    "+" : 3,
    "/" : 4,
    "-" : 5,
    "%" : 6,
    "^" : 10,
}

def get_spin( rows, cols, symbols ) :
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
    

def print_get_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1 :
                print(column[row], end=" | ")
            else :
                print(column[row],end="")
        
        print()

def deposit():
    while True :
        Amount = input("Enter the amount you would like to deposit : ")
        if Amount.isdigit():
            Amount=int(Amount)
            if Amount > 0 :
                break
            else:
                print("Amount must be greater than 0 !!")
        else :
            print("Please enter a number.")

    return Amount


def get_number_of_lines():
    while True :
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else :
                print("Please enter  valid number of lines.")
        else :
            print("Please enter a number.")
    return lines


def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            symbol_check = column[line]
            if symbol != symbol_check :
                break
        else :
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def bet_user():
    while True :
        amount = input("Enter the amount you would like to bet : ")
        if amount.isdigit() :
            amount = int(amount)
            if 1 <= amount :
                break
            else :
                print("The amount must be in more than $1")
        else :
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True :
        bet = bet_user()
        total_bet = bet*lines

        if total_bet > balance :
            print(f"You do not have enough money to bet on.\nYour current balance is : ${balance}")
        else :
            break

    print(f"You are betting {bet} on {lines} line/lines.")
    print(f"Your total bettin amount is {total_bet}")

    slots = get_spin(ROWS, COLUMNS, symbol_count)
    print_get_spin(slots)

    winnings, winning_lines = check_win(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on ", *winning_lines)
    return winnings-total_bet

def main():
    balance = deposit()
    while True :
        print(f"Current balance is ${balance}")
        ans = input("Press enter to play or 'q' to quit.")
        if ans == "q" :
            break
        balance += spin(balance)
    print(f"you are left with ${balance}")

main()


    



