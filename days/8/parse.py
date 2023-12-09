def parse_data(example=False, part2=False):
    file_name = "data.txt"
    if example:
        if part2:
            file_name = "example_data2.txt"
        else:
            file_name = "example_data.txt"
    data = {}
    nodes = {}
    line_number = 0
    with open(f"days/8/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if (line_number == 0):
                data['directions'] = line.replace("L", "0").replace("R", "1")
                line_number += 1
            elif(line_number == 1):
                line_number += 1
                pass
            else:
                nodes[line[:3]] = line[7:-1].split(', ')
    data['nodes'] = nodes
    return data