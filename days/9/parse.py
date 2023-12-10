def parse_data(example=False):
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    data = []
    with open(f"days/9/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            seq = [int(x) for x in line.split(" ")]
            data.append(seq)
    return data