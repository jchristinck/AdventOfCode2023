if __name__ == "__main__":
    text = open("input/day04.txt", "r").read().splitlines()
    points, number_of_cards = 0, [1] * len(text)
    for idx, card in enumerate(text):
        (winning, owning) = card.split(" | ")
        winning = list(map(int, winning.split(": ")[1].split()))
        owning = list(map(int, owning.split()))
        card_score = sum(1 for number in owning if number in winning)
        if card_score:
            points += 2 ** (card_score - 1)
        for i in range(card_score):
            number_of_cards[idx + 1 + i] += number_of_cards[idx]
    print(points)
    print(sum(number_of_cards))
