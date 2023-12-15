def calc_hash(patt):
    val = 0
    for char in patt:
        val = (val + ord(char)) * 17 % 256
    return val


if __name__ == "__main__":
    text = open("input/day15.txt", "r").read().split(',')
    print(sum([calc_hash(step) for step in text]))  # 511416

