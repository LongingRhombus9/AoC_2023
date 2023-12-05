def main():
    card_no = 0
    hand_instance = {}
    hand_match = {}

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            card_no += 1
            current_hand = []
            winning_hand = []
            wins = []

            seg = line.rstrip().split(": ")
            cards = seg[1].split(" | ")
            for hand in cards[0].strip().split(" "):
                if hand != "":
                    current_hand.append(hand)
            
            for win in cards[1].strip().split(" "):
                if win != "":
                    winning_hand.append(win)

            for cur_card in current_hand:
                for win_card in winning_hand:
                    if win_card == cur_card:
                        wins.append(win_card)
            hand_match[card_no] = len(wins)            

        for hand in hand_match:
            hand_instance[hand] = 1

        for hand,match_no in hand_match.items():
            next_hand = hand + 1
            next = []
            for _ in range(match_no):
                next.append(next_hand)
                next_hand += 1
            for instance in next:
                hand_instance[instance] += hand_instance[hand]
        print(sum(hand_instance.values()))
            
main()