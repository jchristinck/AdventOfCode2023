def determine_type():
    hand_set = set(hand)
    match len(hand_set):
        case 1:
            return 1  # five of a kind
        case 2:
            for char in hand:
                if hand.count(char) == 4:
                    return 2  # four of a kind
                elif hand.count(char) == 2:
                    return 3  # full house
        case 3:
            for char in hand:
                if hand.count(char) == 3:
                    return 4  # three of a kind
                elif hand.count(char) == 2:
                    return 5  # two pairs
        case 4:
            return 6  # pair
        case 5:
            return 7  # high card


def determine_order():
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands_comp = []
    for idx in indices:
        h = list(hands[idx])
        for idy, char in enumerate(h):
            h[idy] = char.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        hands_comp.append([list(map(int, h)), idx])
    hands_comp = sorted(hands_comp, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
    return [x[1] for x in hands_comp]


if __name__ == "__main__":
    text = open("input/day07.txt", "r").read().splitlines()
    hands, bids = [x.split()[0] for x in text], list(map(int, [x.split()[1] for x in text]))
    types, ranks = [], [0 for _ in range(len(text))]
    for hand in hands:
        types.append(determine_type())
    current_rank = 1
    for type in range(7, 0, -1):
        indices = [idx for idx, element in enumerate(types) if type == element]
        indices = determine_order()
        for idx in indices:
            ranks[idx] = current_rank
            current_rank += 1
    print(sum([a * b for a, b in zip(ranks, bids)]))  # 249726565
