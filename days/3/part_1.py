import re
from parse import parse_data

data = parse_data()

def get_full_number(list, index):
    full_number = ""
    for i in range(index, len(list)):
        if(list[i].isalnum()):
            full_number += list[i]
        else:
            return full_number
    return full_number

def get_surroundings(number, y, x):
    # print(f"Got {number} at row {y} position {x}")
    # print(f"Bounding-box should be from {y-1},{x-1} to {y+2},{x+len(number)+1}")
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


def check_for_special(box):
    # print(f"Box : {box}")
    for y in range(box[0], box[2]):
        for x in range(box[1],box[3]):
            if(not data[y][x].isalnum() and data[y][x] != "."):
                return True
    return False


sum = 0
y = 0
while y < len(data):
    x = 0
    while x < len(data[y]):
        if(data[y][x].isalnum()):
            number = get_full_number(data[y], x)
            box = get_surroundings(number,y,x)
            valid = check_for_special(box)
            if(valid):
                sum += int(number)
            x += len(number)-1
        x += 1
    y += 1

print(f"Sum of parts: {sum}")