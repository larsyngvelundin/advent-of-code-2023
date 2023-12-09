def parse_data(example=False):
    file_name = "data.txt"
    if example:
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