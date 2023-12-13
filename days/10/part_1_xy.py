from parse import parse_data

data = parse_data(example=0)

up, right, down, left = 0, 1, 2, 3
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
    #up
    sp = start_position
    if(sp[1] > 0):
        tile_up = data[sp[1]-1][sp[0]]
        if (d[tile_up][down]):
            return [sp[0],sp[1]], [sp[0],sp[1]-1]
    #down
    if(sp[1] < len(data)):
        tile_down = data[sp[1]+1][sp[0]]
        if (d[tile_down][up]):
            return [sp[0],sp[1]], [sp[0],sp[1]+1]
    #left
    if(sp[0] > 0):
        tile_left = data[sp[1]][sp[0]-1]
        if (d[tile_left][right]):
            return [sp[0],sp[1]], [sp[0]-1,sp[1]]
    #right
    if(sp[0] < len(data[0])):
        tile_right = data[sp[1]][sp[0]+1]
        if (d[tile_right][left]):
            return [sp[0],sp[1]],[sp[0]+1,sp[1]]
    
    return [sp[0],sp[1]], [0,0]

def find_next(current, next):
    n = next
    if(data[n[1]][n[0]] == "S"):
        return False, False
    ct = data[next[1]][next[0]]
    #up
    if(n[1] > 0 and [n[0],n[1]-1] != current):
        tile_up = data[n[1]-1][n[0]]
        if (d[tile_up][down] and d[ct][up]):
            return [n[0],n[1]], [n[0],n[1]-1]
    #down
    if(n[1] < len(data)-1 and [n[0],n[1]+1] != current):
        tile_down = data[n[1]+1][n[0]]
        if (d[tile_down][up] and d[ct][down]):
            return [n[0],n[1]], [n[0],n[1]+1]
    #left
    if(n[0] > 0 and [n[0]-1,n[1]] != current):
        tile_left = data[n[1]][n[0]-1]
        if (d[tile_left][right] and d[ct][left]):
            return [n[0],n[1]], [n[0]-1,n[1]]
    #right
    if(n[0] < len(data[0])-1 and [n[0]+1,n[1]] != current):
        tile_right = data[n[1]][n[0]+1]
        if (d[tile_right][left] and d[ct][right]):
            return [n[0],n[1]],[n[0]+1,n[1]]


def print_map(data):
    for row in data:
        print(row.replace("-","═").
                replace("|", "║").
                replace("F", "╔").
                replace("7", "╗").
                replace("J", "╝").
                replace("L", "╚"))


def main():
    start_position = find_start(data)
    current, next = find_first_step(start_position)
    steps = 0
    while next:
        current, next = find_next(current, next)
        steps += 1
    print(f"Total steps: {steps}")
    print(f"Furthest should be {steps/2}")

if __name__ == "__main__":
    main()