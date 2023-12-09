from parse import parse_data

data = parse_data(example = 0)

still_looking = True
current_node = "AAA"
direction_index = 0
steps_taken = 0

while still_looking:
    if(direction_index >= len(data['directions'])):
        direction_index = 0
    current_node = data['nodes'][current_node][int(data['directions'][direction_index])]
    steps_taken += 1
    if(current_node == "ZZZ"):
        print(f"Reached 'ZZZ' in {steps_taken} steps")
        still_looking = False
    direction_index += 1