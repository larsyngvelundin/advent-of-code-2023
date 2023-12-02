from parse import parse_data

class BreakLoops(Exception): pass

def main():
    max = {'red':12,'green':13,'blue':14}
    data = parse_data("data.txt")
    valid_games_sum = 0
    for game in data:
        try:
            for set in data[game]:
                for color in set:
                    if(set[color] > max[color]):
                        raise BreakLoops
                    
            valid_games_sum += int(game)
        except BreakLoops:
            pass
    print(f"Sum of possible games: {valid_games_sum}")



if(__name__ == "__main__"):
    main()