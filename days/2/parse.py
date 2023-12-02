

def parse_data(file_name): #messy, but works hehe
    data = {}
    with open(f"days/2/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            game_number = line[line.find("Game")+5:line.find(":")]
            data[game_number] = []
            line_sets = line[line.find(":")+2:]
            set_strings = line_sets.split("; ")
            list_of_sets = []
            for game_set in set_strings:
                colors = game_set.split(", ")
                color_set = {}
                for color in colors:
                    color_pair = color.split(" ")
                    color_set[color_pair[1]] = int(color_pair[0])
                list_of_sets.append(color_set)
            data[game_number] = list_of_sets

    return data