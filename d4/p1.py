def main():
    all_points = []

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            # Enter game
            current_hand = []
            winning_hand = []
            wins = []
            points = 0

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

            if len(wins) != 0:
                points = 1
                for point in wins[1:]:
                    print(point)
                    points *= 2
            all_points.append(points)

        print(">>>", sum(all_points))

main()