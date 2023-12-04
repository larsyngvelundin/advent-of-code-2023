from parse import parse_data

data = parse_data()

def main():
    sum = 0 
    for card in data:
        multiplier = -1
        for win_number in data[card]['winning_numbers']:
            if win_number in data[card]['numbers']:
                multiplier += 1
        winnings = int(2**multiplier)
        sum += winnings
    print(f"Sum of winnings: {sum}")

if __name__ == "__main__":
    main()