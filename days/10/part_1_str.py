from parse import parse_data
data = parse_data(example=0)

all_chars = "|-LJ7F"

up, right, down, left = 0, 1, 2, 3
directions = {
    '-': [False, True, False, True],
    '|': [True, False, True, False],
    'L': [True, True, False, False],
    'J': [True, False, False, True],
    '7': [False, False, True, True],
    'F': [False, True, True, False],
    '.': [False, False, False, False],
    'X': [False, False, False, False],
    'S': [True,True,True,True]
}
d = directions #for easier access

def check_if_matching_h(first,second):
    f, s = first, second
    if(d[f][right] and d[s][left]):
        return [True]
    if(d[f][right] and not d[s][left]):
        return [False, 1]
    if(not d[f][right] and d[s][left]):
        return [False, 2]
    if(not d[f][right] and not d[s][left]):
        return [False, None]
    return("something went wrong :(")

def check_if_matching_v(first,second):
    f, s = first, second
    if(d[f][down] and d[s][up]):
        return [True]
    if(d[f][down] and not d[s][up]):
        return [False, 1]
    if(not d[f][down] and d[s][up]):
        return [False, 2]
    if(not d[f][down] and not d[s][up]):
        return [False, None]
    return("something went wrong :(")

def clear_h(data, still_clearing):
    still_clearing = False
    for y in range(0, len(data)):
        data_test = list(data[y])
        x = 0
        while x < len(data_test)-1:
            res = check_if_matching_h(data_test[x],data_test[x+1])
            if (not res[0]):
                if (res[1] and data_test[x + res[1] - 1] != "S"):
                    data_test[x + res[1] - 1] = "."
                    still_clearing = True
                    x -= 2
            x += 1
        data[y] = "".join(data_test)
    return still_clearing

def clear_v(data, still_clearing):
    still_clearing = False
    for x in range(0, len(data[0])):
        data_test = ""
        for y in range(0, len(data)):
            data_test += data[y][x]
        data_test = list(data_test)
        y = 0
        while y < len(data_test)-1:
            res = check_if_matching_v(data_test[y],data_test[y+1])
            if (not res[0]):
                if (res[1] and data_test[y + res[1] - 1] != "S"):
                    data_test[y + res[1] - 1] = "."
                    still_clearing = True
                    y -= 2
            y += 1
        y = 0
        while y < len(data_test):
            temp_list = list(data[y])
            temp_list[x] = data_test[y]
            temp_list = "".join(temp_list)
            data[y] = temp_list
            y += 1
    return still_clearing


def clear_edges(data):
    #up
    up_row = list(data[0])
    for i in range(0,len(up_row)):
        if(d[up_row[i]][up]):
            up_row[i] = "."
    up_row = "".join(up_row)
    data[0] = up_row
    #down
    down_row = list(data[len(data)-1])
    for i in range(0,len(down_row)):
        if(d[down_row[i]][down]):
            down_row[i] = "."
    down_row = "".join(down_row)
    data[len(data)-1] = down_row
    left_row = ""
    right_row = ""
    #left and right
    for y in range(0, len(data)):
        left_row += data[y][0]
        right_row += data[y][-1]
    left_row = list(left_row)
    right_row = list(right_row)
    for i in range(0,len(left_row)):
        if(d[left_row[i]][left]):
            left_row[i] = "."
        if(d[right_row[i]][right]):
            right_row[i] = "."
        
    for y in range(0, len(data)):
        temp_list = list(data[y])
        temp_list[0] = left_row[y]
        temp_list[-1] = right_row[y]
        temp_list = "".join(temp_list)
        data[y] = temp_list
    pass

def clear_lone_loops(data):
    for y in range(0, len(data)-1):
        for x in range(0, len(data[y])-1):
            if data[y][x:x+2] == "F7":
                if data[y+1][x:x+2] == "LJ":
                    temp_list = list(data[y])
                    temp_list[x] = "."
                    temp_list = "".join(temp_list)
                    data[y] = temp_list


def print_map(data):
    for row in data:
        print(row.replace("-","═").
                replace("|", "║").
                replace("F", "╔").
                replace("7", "╗").
                replace("J", "╝").
                replace("L", "╚"))

def main():
    clear_edges(data)
    clear_lone_loops(data)
    still_clearing = True
    while still_clearing:
        t_h = clear_h(data, still_clearing)
        t_v = clear_v(data, still_clearing)
        still_clearing = t_h + t_v
        
    print_map(data)
    dot_count = 0
    for row in data:
        dot_count += row.count(".")
    print(f"Found {dot_count} dots")
    square_count = len(data) * len(data[0])
    print(f"There is a total of {square_count} squares")
    print(f"That minus the dots is {square_count - dot_count}")
    print(f"So that means the answer is {(square_count - dot_count)/2}")


if __name__ == "__main__":
    main()