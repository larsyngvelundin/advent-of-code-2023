import re
from parse import parse_data

data = parse_data()
gears = {}

def get_full_number(list, index):
    full_number = ""
    for i in range(index, len(list)):
        if(list[i].isalnum()):
            full_number += list[i]
        else:
            return full_number
    return full_number

def get_surroundings(number, y, x):
    box = [y-1,x-1,y+2,x+len(number)+1] #ty,lx,by,rx
    if(box[0] < 0):
        box[0] = 0
    if(box[1] < 0):
        box[1] = 0
    if(box[2] > len(data)):
        box[2] = len(data)
    if(box[3] > len(data[x])):
        box[3] = len(data[x])
    return box

def calculate_gear_value(gear_id, number):
    value = 0
    if gear_id in gears.keys():
        value = gears[gear_id] * number
    else:
        gears[gear_id] = number
    return value

def check_for_gear(box, number):
    for y in range(box[0], box[2]):
        for x in range(box[1],box[3]):
            if(data[y][x] == "*"):
                gear_id = str(y) + "-"  + str(x)
                value = calculate_gear_value(gear_id, int(number))
                return value
    return False

def main():
    sum = 0
    y = 0
    while y < len(data):
        x = 0
        while x < len(data[y]):
            if(data[y][x].isalnum()):
                number = get_full_number(data[y], x)
                box = get_surroundings(number,y,x)
                gear_ratio = check_for_gear(box, number)
                sum += int(gear_ratio)
                x += len(number)-1
            x += 1
        y += 1

    print(f"Sum of gear ratios: {sum}")

if __name__ == "__main__":
    main()