from parse import parse_data

def main():
    data = parse_data("data.txt")
    powers_sum = 0
    for game in data:
        max = {'red':0,'green':0,'blue':0}
        for set in data[game]:
            for color in set:
                if(set[color] > max[color]):
                    max[color] = set[color]
        power = max['red'] * max['blue'] * max['green']
        powers_sum += power
    print(f"Sum of powers: {powers_sum}")

if(__name__ == "__main__"):
    main()