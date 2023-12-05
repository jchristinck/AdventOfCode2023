if __name__ == "__main__":
    text = open("input/day05.txt", "r").read().splitlines()
    idx, seeds = 1, list(map(int, text[0].split(': ')[1].split()))
    while text[idx]:
        seeds.append(list(map(int, text[idx])))
        idx += 1
    idx += 2
    maps = [[] for _ in range(7)]
    for i in range(7):
        while idx < len(text) and text[idx]:
            maps[i].append(list(map(int, text[idx].split())))
            idx += 1
        idx += 2
    more_seeds = []
    for idx in range(0, len(seeds), 2):
        more_seeds.append(range(seeds[idx], seeds[idx] + seeds[idx + 1]))
    for idx in range(len(seeds)):
        for mapp in maps:
            for conversion in mapp:
                if seeds[idx] in range(conversion[1], conversion[1] + conversion[2]):
                    seeds[idx] = seeds[idx] - conversion[1] + conversion[0]
                    break
    converted_seeds = more_seeds
    for mapp in maps:
        more_seeds = converted_seeds
        converted_seeds = []
        for conversion in mapp:
            remaining_seeds = more_seeds
            more_seeds = []
            while remaining_seeds:
                seed_range = remaining_seeds.pop(0)
                if seed_range[0] >= conversion[1] and seed_range[-1] <= conversion[1] + conversion[2]:  # within
                    converted_seeds.append(range(seed_range[0] - conversion[1] + conversion[0],
                                                 seed_range[-1] - conversion[1] + conversion[0] + 1))
                elif seed_range[0] < conversion[1] < seed_range[-1] <= conversion[1] + conversion[2]:  # too far lower
                    converted_seeds.append(range(conversion[0], seed_range[-1] - conversion[1] + conversion[0] + 1))
                    remaining_seeds.append(range(seed_range[0], conversion[1]))
                elif conversion[1] <= seed_range[0] < conversion[1] + conversion[2] < seed_range[-1]:  # too far upper
                    converted_seeds.append(range(seed_range[0] - conversion[1] + conversion[0],
                                                 seed_range[0] - conversion[1] + conversion[0] + conversion[2]))
                    remaining_seeds.append(range(conversion[1] + conversion[2],
                                                 seed_range[-1] + 1))
                elif seed_range[0] < conversion[1] and seed_range[-1] > conversion[1] + conversion[2]:  # both out of r
                    converted_seeds.append(range(conversion[0], conversion[0] + conversion[2] + 1))
                    remaining_seeds.append(range(seed_range[0], conversion[1]))
                    remaining_seeds.append(range(conversion[2] + conversion[0] + 1,
                                                 seed_range[-1] - conversion[1] + conversion[0] + 1))
                else:
                    more_seeds.append(seed_range)
        for seed in more_seeds:
            if more_seeds not in converted_seeds:
                converted_seeds.append(seed)
    print(min(seeds))  # 51580674
    print(min([x[0] for x in converted_seeds]))  # 99751240
