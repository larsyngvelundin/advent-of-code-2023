def parse_data(example=False):
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    data = []
    with open(f"days/10/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            data.append(line)
    return data