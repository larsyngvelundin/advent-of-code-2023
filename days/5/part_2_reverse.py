from parse import parse_data
from time import time

drs = 0
srs = 1
rl = 2

data = parse_data(example=0)
for i in range(0, len(data['seeds'])):
  data['seeds'][i] = int(data['seeds'][i])

valid_seed_ranges = []
for i in range(0, len(data['seeds']), +2):
    valid_seed_ranges.append(range(data['seeds'][i],data['seeds'][i] + data['seeds'][i+1]))

def get_middle(low,high):
    r = high - low
    m = int(r / 2)
    return low + m

def get_lowest_seed(seeds):
    min = seeds[0]
    for i in range(2, len(seeds), +2):
        if seeds[i] < min:
            min = seeds[i]
    return min

lowest_possible_seed = get_lowest_seed(data['seeds'])

def check_if_valid_seed(seed):
    if(seed < lowest_possible_seed):
        return False
    for seed_range in valid_seed_ranges:
        if seed in seed_range:
            return True
    return False

def get_seed_from_location(loc):
    seed = loc
    for i in range(len(data['order']) - 1, -1,-1):
        maps = data[data['order'][i]]
        for map in maps:
            if (seed in range(map[drs],map[drs]+map[rl])):
                next_seed = seed - (map[drs] - map[srs])
                seed = next_seed
                break
        pass
    return seed

def get_first_low():
    current_loc = 1
    first_low_found = False
    while current_loc < (10 ** 20) and first_low_found == False:
        seed = get_seed_from_location(current_loc)
        if seed and check_if_valid_seed(seed):
            first_low_found = True
            return current_loc
        else:
            pass
        current_loc *= 10
    return False

first_low = get_first_low()

def check_one(loc):
    seed = get_seed_from_location(loc)
    if seed and check_if_valid_seed(seed):
        return True
    return False

def main():
    new_to_check = get_middle(int(first_low/10), first_low)
    chigh = first_low
    clow = int(first_low/10)
    last_valid = first_low
    errors_in_a_row = 0
    while True:
        was_valid = check_one(new_to_check)
        if was_valid:
            chigh = new_to_check
            last_valid = new_to_check
        else:
            clow = new_to_check
            errors_in_a_row += 1
        if(errors_in_a_row > 25):
            return f"{last_valid} is probably the lowest"
        new_to_check = get_middle(clow,chigh)

if __name__ == "__main__":
    start_time_total = time()
    print(main())
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"Found solution in: {elapsed_time:.5f} seconds")