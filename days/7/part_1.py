from parse import parse_data

hands = parse_data(example=0)

chars = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def check_type(hand):
    for char in chars:
        if hand == char * 5:
            return 7
        if hand.count(char) == 4:
            return 6
        if hand.count(char) == 3:
            for schar in chars:
                if hand.count(schar) == 2 and char != schar:
                    return 5
            return 4
        if hand.count(char) == 2:
            for schar in chars:
                if hand.count(schar) == 2 and char != schar:
                    return 3
                if hand.count(schar) == 3 and char != schar:
                    return 5
            return 2
    return 1

#Convert hand into an integer that can be sorted
#example: 2 04 02 04 13 10 for 424KT
#Type, value of 1st,2,3,4,5 card in order. 
for i in range(0, len(hands)):
    card_value = check_type(hands[i][0])* 10** 10
    for c in range(0, 5):
        mult = 10 ** (8 - c * 2)
        card_value += chars[hands[i][0][c]] * mult
    hands[i][0] = card_value
    hands[i][1] = int(hands[i][1])

sorted_hands = sorted(hands, key=lambda x: x[0])
total_winnings = 0
for i in range(0, len(sorted_hands)):
    total_winnings += (i+1) * sorted_hands[i][1]
print(f"Total winnings: {total_winnings}")