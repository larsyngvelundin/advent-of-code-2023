def parse_data(example=False): #messy, but works hehe
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    data = {}
    with open(f"days/4/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            card_number = line[line.find("Card")+5:line.find(":")]
            winning_numbers = line[line.find(":")+2:line.find("|")-1].strip().replace("  ", " ").split(" ")
            numbers = line[line.find("|")+2:].strip().replace("  ", " ").split(" ")
            data[card_number] = {'numbers': numbers, 'winning_numbers': winning_numbers}
    return data