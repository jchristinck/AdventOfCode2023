import math
if __name__ == "__main__":
    text = open("input/day06.txt", "r").read().splitlines()
    ts, ds = [list(map(int, text[idx].split(": ")[1].split())) for idx in range(2)]
    print(math.prod([t - (math.floor((t - math.sqrt((t ** 2) - (4 * d))) / 2) * 2) - 1 for t, d in zip(ts, ds)]))  # 219849
    t, d = [int(text[idx].split(": ")[1].replace(" ", "")) for idx in range(2)]
    print(t - (math.floor((t - math.sqrt((t ** 2) - (4 * d))) / 2) * 2) - 1)  # 29432455
