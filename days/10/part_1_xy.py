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
    'F': [False, True, True, False],
    '.': [False, False, False, False],
    'S': [True,True,True,True]
}
d = directions #for easier access

def find_start(data):
    for y in range(0,len(data)):
        if data[y].find("S") != -1:
            x = data[y].find("S")
            return [x,y]
    return [None, None]

def find_first_step(start_position):
    # #up
    sp = start_position
    if(sp[1] > 0):
        tile_up = data[sp[1]-1][sp[0]]
        print(tile_up)
        if (d[tile_up][down]):
            print("found start")
            return [sp[0],sp[1]], [sp[0],sp[1]-1]
    #down
    if(sp[1] < len(data)):
        tile_down = data[sp[1]+1][sp[0]]
        print(tile_down)
        if (d[tile_down][up]):
            print("found start")
            return [sp[0],sp[1]], [sp[0],sp[1]+1]
    #left
    if(sp[0] > 0):
        tile_left = data[sp[1]][sp[0]-1]
        print(tile_left)
        if (d[tile_left][right]):
            print("found start")
            return [sp[0],sp[1]], [sp[0]-1,sp[1]]
    #right
    if(sp[0] < len(data[0])):
        tile_right = data[sp[1]][sp[0]+1]
        print(tile_right)
        if (d[tile_right][left]):
            print("found start")
            return [sp[0],sp[1]],[sp[0]+1,sp[1]]
    
    return [sp[0],sp[1]], [0,0]
    pass

def find_next(current, next):
    print("==================================")
    print("New find_next")
    n = next
    if(data[n[1]][n[0]] == "S"):
        return False, False
    
    # print(f"[n[0]+1,n[1]]: {[n[0]+1,n[1]]}")
    print(f"current {current}")
    print(f"next {next}")
    # print(f"[n[0],n[1]-1] {[n[0],n[1]-1]}")
    #up
    if(n[1] > 0 and [n[0],n[1]-1] != current):
        tile_up = data[n[1]-1][n[0]]
        print(tile_up)
        if (d[tile_up][down]):
            print(f"found next up: {tile_up}")
            return [n[0],n[1]], [n[0],n[1]-1]
    #down
    if(n[1] < len(data)-1 and [n[0],n[1]+1] != current):
        tile_down = data[n[1]+1][n[0]]
        print(tile_down)
        if (d[tile_down][up]):
            print(f"found next tile_down: {tile_down}")
            return [n[0],n[1]], [n[0],n[1]+1]
    #left
    if(n[0] > 0 and [n[0]-1,n[1]] != current):
        tile_left = data[n[1]][n[0]-1]
        print(tile_left)
        if (d[tile_left][right]):
            print(f"found next tile_left: {tile_left}")
            return [n[0],n[1]], [n[0]-1,n[1]]
    #right
    if(n[0] < len(data[0])-1 and [n[0]+1,n[1]] != current):
        tile_right = data[n[1]][n[0]+1]
        print(tile_right)
        if (d[tile_right][left]):
            print(f"found next tile_right: {tile_right}")
            return [n[0],n[1]],[n[0]+1,n[1]]
    
    # return [sp[0],sp[1]], [0,0]
    # return [0,0], [0,0]

def print_map(data):
    for row in data:
        print(row.replace("-","═").
                replace("|", "║").
                replace("F", "╔").
                replace("7", "╗").
                replace("J", "╝").
                replace("L", "╚"))
        
def main(data):
    start_position = find_start(data)
    print(f"Start is at {start_position}")
    print_map(data)
    current, next = find_first_step(start_position)
    print(f"Starting at {current}, going to {next}")
    steps = 0
    while next:
        current, next = find_next(current, next)
        steps += 1
        print(f"{steps} steps taken")
    print(f"Total steps: {steps}")
    print(f"Furthest should be {steps/2}")

if __name__ == "__main__":
    main(data)