def calc_hash(patt):
    val = 0
    for char in patt:
        val = (val + ord(char)) * 17 % 256
    return val


if __name__ == "__main__":
    text = open("input/day15.txt", "r").read().split(',')
    print(sum([calc_hash(step) for step in text]))  # 511416
    bxs = [[] for _ in range(256)]
    for step in text:
        idx_sign = max(step.find('='), step.find('-'))
        idx = calc_hash(step[:idx_sign])
        if step[idx_sign] == '=':
            for idy, lens in enumerate(bxs[idx]):
                if step[:idx_sign] == lens[0]:
                    bxs[idx][idy] = (step[:idx_sign], step[idx_sign + 1])
                    break
            else:
                bxs[idx].append((step[:idx_sign], step[idx_sign + 1]))
        else:
            for idy, lens in enumerate(bxs[idx]):
                if step[:idx_sign] == lens[0]:
                    del bxs[idx][idy]
    print(sum([sum([(j + 1) * (i + 1) * int(l[1]) for i, l in enumerate(bxs[j])]) for j in range(len(bxs))]))  # 290779
