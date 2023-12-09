from parse import parse_data
import math

data = parse_data(example = 0, part2 = 1)

still_looking = True
current_nodes = []
direction_index = 0
steps_taken = 0

for node in data['nodes']:
    if(node[2] == "A"):
        current_nodes.append(node)

def find_loop(node):
    current_steps = 0
    current_node = node

    still_looking = True
    direction_index = 0
    steps_taken = 0
    steps_taken_total = 0

    while still_looking:
        if(direction_index >= len(data['directions'])):
            direction_index = 0
        current_node = data['nodes'][current_node][int(data['directions'][direction_index])]
        steps_taken += 1
        steps_taken_total += 1
        if(current_node[2] == "Z"):
            if steps_taken == current_steps:
                still_looking = False
            else:
                current_steps = steps_taken
                steps_taken = 0
        direction_index += 1
    return current_steps

loop_numbers = []
for node in current_nodes:
    loop_numbers.append(find_loop(node))

lcm = math.lcm(loop_numbers[0],loop_numbers[1])
for i in range(1,len(loop_numbers)-1):
    lcm = math.lcm(lcm,loop_numbers[i+1])
print(f"Reached --Z in {lcm} steps")