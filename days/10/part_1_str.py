from parse import parse_data

data = parse_data(example=1)

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

def check_if_matching_v(first,second):
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

# for char1 in all_chars:
#     for char2 in all_chars:
#         print(f"{char1}{char2} = {check_if_matching_v(char1,char2)}")

for y in range(0, len(data)):
    data_test = list(data[y])
    x = 0
    while x < len(data_test)-1:
    # for x in range(0,len(data_test)-1):
        res = check_if_matching_v(data_test[x],data_test[x+1])
        print(res)
        if (not res[0]):
            if (res[1]):
                data_test[x + res[1] - 1] = "X"
                print(f"before{x}")
                x -= 2
                print(f"after{x}")
        x += 1
    data[y] = "".join(data_test)

for row in data:
    print(row)
    # if data[]