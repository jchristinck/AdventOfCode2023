import numpy as np
import copy


def rocks_fall(patt, dir):
    match dir:
        case 1:
            patt = np.transpose(patt)
        case 2:
            patt = np.flipud(patt)
        case 3:
            patt = np.transpose(np.fliplr(patt))
    for idy, row in enumerate(patt):
        for idx, el in enumerate(row):
            match el:
                case '.':
                    for idc in range(idy + 1, len(patt)):
                        match patt[idc][idx]:
                            case '#':
                                break
                            case 'O':
                                patt[idy][idx] = 'O'
                                patt[idc][idx] = '.'
                                break
    match dir:
        case 1:
            patt = np.transpose(patt)
        case 2:
            patt = np.flipud(patt)
        case 3:
            patt = np.transpose(np.fliplr(patt))
    return patt


if __name__ == "__main__":
    pattern = np.array([list(x) for x in open("input/day14.txt", "r").read().splitlines()])
    history = []
    rep_found = False
    cycle = 0
    while not rep_found:
        for idp in range(len(history)):
            if np.array_equal(history[idp], pattern):
                rep_found = (cycle, idp)
        history.append(copy.deepcopy(pattern))
        for rotation in range(4):
            rocks_fall(pattern, rotation)
            if not (cycle or rotation):
                print(sum([sum([len(pattern) - y for e in r if e == 'O']) for y, r in enumerate(pattern)]))  # 109345
        cycle += 1
    total_cycles = (1000000000 - rep_found[1]) % (rep_found[0] - rep_found[1]) + rep_found[1]
    print(sum([sum([len(pattern) - y for e in r if e == 'O']) for y, r in enumerate(history[total_cycles])]))  # 112452
