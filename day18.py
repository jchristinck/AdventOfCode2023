import sys


def floodfill(l):
    if l not in cubes:
        cubes.append(l)
        floodfill((l[0] + 1, l[1]))
        floodfill((l[0] - 1, l[1]))
        floodfill((l[0], l[1] + 1))
        floodfill((l[0], l[1] - 1))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    text = [x for x in open("input/day18.txt", "r").read().splitlines()]
    dirs, dists, colors = [x.split()[0] for x in text], [int(x.split()[1]) for x in text], [x.split()[2] for x in text]
    cubes = [(0, 0)]
    for di, dist, color in zip(dirs, dists, colors):
        pred = cubes[-1]
        for d in range(1, dist + 1):
            if di == 'R':
                cubes.append((pred[0], pred[1] + d))
            if di == 'D':
                cubes.append((pred[0] + d, pred[1]))
            if di == 'L':
                cubes.append((pred[0], pred[1] - d))
            if di == 'U':
                cubes.append((pred[0] - d, pred[1]))
    del cubes[-1]
    ff = (1, 1)
    while ff in cubes:
        ff += (1, 1)
    floodfill(ff)
    print(len(cubes))  # 28911

