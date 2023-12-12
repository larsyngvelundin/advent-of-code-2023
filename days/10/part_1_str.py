from parse import parse_data
from time import sleep
data = parse_data(example=0)

all_chars = "|-LJ7F"


up, right, down, left = 0, 1, 2, 3
print(up, right, down, left)
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

# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ

#['X', 'X', '7', 'J', 'J']
#X
#X
#7
#J
#J
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
    print(f"Returning {still_clearing}")
    return still_clearing

# for row in data:
#     print(row)

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
    print(f"Returning {still_clearing}")
    return still_clearing





def main():
    still_clearing = True
    while still_clearing:
        t_h = clear_h(data, still_clearing)
        t_v = clear_v(data, still_clearing)
        still_clearing = t_h + t_v
        # sleep(1)


if __name__ == "__main__":
    main()



for row in data:
    print(row.replace("-","═").
          replace("|", "║").
          replace("F", "╔").
          replace("7", "╗").
          replace("J", "╝").
          replace("L", "╚"))
    # if data[]
#try to count all non-periods?
dot_count = 0
for row in data:
    dot_count += row.count(".")
print(f"Found {dot_count} dots")
square_count = len(data) * len(data[0])
print(f"There is a total of {square_count} squares")
print(f"That minus the dots is {square_count - dot_count}")
print(f"So that means the answer is {(square_count - dot_count)/2}")