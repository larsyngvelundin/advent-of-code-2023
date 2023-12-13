from parse import parse_data

data = parse_data(example=1)
print(data)

up, right, down, left = 0, 1, 2, 3
print(up, right, down, left)
directions = {
    '-': [False, True, False, True],
    '|': [True, False, True, False],
    'L': [True, True, False, False],
    'J': [True, False, False, True],
    '7': [False, False, True, True],
    'F': [False, True, True, False]
}
d = directions #for easier access

def find_start(data):
    for y in range(0,len(data)):
        if data[y].find("S") != -1:
            x = data[y].find("S")
            return [x,y]
    return [None, None]

def find_first_step():
    

def find_next(last, current, next):
    if(last == None):
        #assume start
        find_first_step()
        return "bep"
    

def main(data):
    start_positions = find_start(data)
    print(f"Start is at {start_positions}")

if __name__ == "__main__":
    main(data)