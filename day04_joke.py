text = open("input/day04.txt", "r").read().splitlines()
points, num_cards = 0, [1] * len(text)
for idx, cd in enumerate(text):
    win, own = list(map(int, cd.split(" | ")[0].split(": ")[1].split())), list(map(int, cd.split(" | ")[1].split()))
    card_score = sum(1 for number in own if number in win)
    points += 2 ** (card_score - 1) if card_score else 0
    num_cards[idx + 1:idx + 1 + card_score] = [x + num_cards[idx] for x in num_cards[idx + 1:idx + 1 + card_score]]
print(points, sum(num_cards))  # 28750, 10212704
