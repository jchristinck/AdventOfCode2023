def calc_sym_index(p, d):
    for i in range(len(p)):
        if sum([len([e1 for e1, e2 in zip(p[i - j], p[i + 1 + j]) if e1 != e2]) for j in
                range(min(i, len(p) - i - 2) + 1)]) == d and i < len(p) - 1:
            return i + 1
    return 0


if __name__ == "__main__":
    ps = [[list(y) for y in x.splitlines()] for x in open("input/day13.txt", "r").read().split("\n\n")]
    print(sum([calc_sym_index([list(i) for i in zip(*pt)], 0) + 100 * calc_sym_index(pt, 0) for pt in ps]))  # 37025
    print(sum([calc_sym_index([list(i) for i in zip(*pt)], 1) + 100 * calc_sym_index(pt, 1) for pt in ps]))  # 32854

