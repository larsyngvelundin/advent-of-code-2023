from parse import parse_data_list as parse_data

data = parse_data(example=0)

def main():
    sum = 0 
    amount = [1] * len(data)
    for i in range(0,len(data)):
        winning_numbers = 0
        for win_number in data[i]['winning_numbers']:
            if win_number in data[i]['numbers']:
                winning_numbers += 1
        for j in range(i+1,i+1+winning_numbers):
            amount[j] += amount[i]
        sum += amount[i]
    print(f"Sum of winnings: {sum}")

if __name__ == "__main__":
    main()