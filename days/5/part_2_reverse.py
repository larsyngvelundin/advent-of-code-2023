#Mostly luck that this gives the correct answer
#There are a lot of cases where this code would not give the correct answer
#If any of the lower seeds arent in the 1- 1*10**20 rangem they'll be missed by the initial checks
#Resulting in the code trying to find the lowest possible location in the wrong range.

from parse import parse_data
from time import time

drs, srs, rl = 0, 1, 2

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
    for seed_range in valid_seed_ranges:
        if seed in seed_range:
            return True
    return False

def get_first_low(): #going from 1, and up by the power of 10, find the first valid location
    current_loc = 1
    first_low_found = False
    while current_loc < (10 ** 20) and first_low_found == False:
        if get_seed_from_location(current_loc):
            first_low_found = True
            return current_loc,current_loc,current_loc
        current_loc *= 10
    return False,False,False

def main():
    chigh, last_valid, first_low = get_first_low()
    new_to_check = get_middle(int(first_low/10), first_low)
    clow = int(first_low/10)
    errors_in_a_row = 0
    while True:
        if get_seed_from_location(new_to_check):
            last_valid, chigh = new_to_check, new_to_check
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
    print(f"Found solution in: {elapsed_time:.5f} seconds ({elapsed_time})")