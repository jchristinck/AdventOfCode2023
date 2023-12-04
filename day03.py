import copy


def checkNeighbours(text, idy, idx):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dy, dx in directions:
        ny, nx = idy + dy, idx + dx
        if 0 <= ny < len(text) and 0 <= nx < len(text[ny]) and not text[ny][nx] == '.' and not text[ny][nx].isnumeric():
            return True

    return False


if __name__ == "__main__":
    text = [list(line) for line in open("input/day03.txt", "r").read().splitlines()]
    textCopy = copy.deepcopy(text)
    total_sum = 0
    for idy, row in enumerate(text):
        for idx, element in enumerate(row):
            number = ""
            symbolFound = False
            while element.isnumeric() & textCopy[idy][idx].isnumeric():
                number += element
                if not symbolFound:
                    symbolFound = checkNeighbours(text, idy, idx)
                textCopy[idy][idx] = "x"
                idx = idx + 1
                if idx >= len(row):
                    break
                element = row[idx]
            if number and symbolFound:
                total_sum += int(number)
    print(total_sum)
