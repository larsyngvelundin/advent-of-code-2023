def parse_data(example=False):
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    hands = []
    with open(f"days/7/{file_name}", 'r') as file:
        first_line = True
        for line in file:
            line = line.rstrip('\n')
            hands.append(line.split(" "))
    return hands