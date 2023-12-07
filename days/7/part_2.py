from parse import parse_data

hands = parse_data(example=0)

chars = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':1,'Q':12,'K':13,'A':14}

def update_higest(i, highest):
    if highest < i:
        highest = i
    return highest

def check_type(hand):
    highest = 1
    for char in chars:
        jhand = hand.replace("J", char)
        if jhand == char * 5:
            highest = update_higest(7, highest)
        if jhand.count(char) == 4:
            highest = update_higest(6, highest)
        if jhand.count(char) == 3:
            for schar in chars:
                if jhand.count(schar) == 2 and char != schar:
                    highest = update_higest(5, highest)
            highest = update_higest(4, highest)
        if jhand.count(char) == 2:
            for schar in chars:
                if jhand.count(schar) == 2 and char != schar:
                    highest = update_higest(3, highest)
                if jhand.count(schar) == 3 and char != schar:
                    highest = update_higest(5, highest)
            highest = update_higest(2, highest)
    return highest

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