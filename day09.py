if __name__ == "__main__":
    text = [list(map(int, row.split())) for row in open("input/day09.txt", "r").read().splitlines()]
    sum_beginning, sum_end = 0, 0
    for row in text:
        hierarchy = [row]
        while [el for el in hierarchy[-1] if el != 0]:
            hierarchy.append([hierarchy[-1][idx + 1] - hierarchy[-1][idx] for idx in range(len(hierarchy[-1]) - 1)])
        for idx in range(len(hierarchy) - 2, -1, -1):
            hierarchy[idx].insert(0, hierarchy[idx][0] - hierarchy[idx + 1][0])
            hierarchy[idx].append(hierarchy[idx][-1] + hierarchy[idx + 1][-1])
        sum_beginning += hierarchy[0][0]
        sum_end += hierarchy[0][-1]
    print(sum_beginning)  # 957
    print(sum_end)  # 1953784198
