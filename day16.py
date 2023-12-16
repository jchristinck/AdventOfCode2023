import numpy as np


def calc_tiles(beams):
    visited = [[[0 for _ in range(4)] for _ in range(len(pattern[0]))] for _ in range(len(pattern))]
    while len(beams):
        beam = beams.pop()
        if beam[2] == 0 and beam[0]:
            sign = pattern[beam[0] - 1, beam[1]]
            new_loc = [beam[0] - 1, beam[1]]
        elif beam[2] == 1 and beam[1] < len(pattern[0]) - 1:
            sign = pattern[beam[0], beam[1] + 1]
            new_loc = [beam[0], beam[1] + 1]
        elif beam[2] == 2 and beam[0] < len(pattern) - 1:
            sign = pattern[beam[0] + 1, beam[1]]
            new_loc = [beam[0] + 1, beam[1]]
        elif beam[2] == 3 and beam[1]:
            sign = pattern[beam[0], beam[1] - 1]
            new_loc = [beam[0], beam[1] - 1]
        else:
            continue
        sign_idx = '/\\-|.'.index(sign)
        for new_dir in conv[sign_idx][beam[2]]:
            if not visited[new_loc[0]][new_loc[1]][new_dir]:
                beams.add((new_loc[0], new_loc[1], new_dir))
                visited[new_loc[0]][new_loc[1]][new_dir] = 1
    return sum([sum([any(y) for y in x]) for x in visited])


if __name__ == "__main__":
    pattern = np.array([list(x) for x in open("input/day16.txt", "r").read().splitlines()])
    conv = [[[1], [0], [3], [2]],  # /
            [[3], [2], [1], [0]],  # \
            [[1, 3], [1], [1, 3], [3]],  # -
            [[0], [0, 2], [2], [0, 2]],  # |
            [[0], [1], [2], [3]]]  # .
    beams_array = {(0, -1, 1)}
    print(calc_tiles(beams_array))  # 6605
    beams_array = []
    for y in range(len(pattern)):
        beams_array.append({(y, -1, 1)})
        beams_array.append({(y, len(pattern), 3)})
    for x in range(len(pattern[0])):
        beams_array.append({(-1, x, 2)})
        beams_array.append({(len(pattern[0]), x, 0)})
    print(max([calc_tiles(beam_start) for beam_start in beams_array]))  # 6766

