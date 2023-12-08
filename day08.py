import math

if __name__ == "__main__":
    text = open("input/day08.txt", "r").read().splitlines()
    instr = []
    nodes = {}
    instr_ended = False
    for row in text:
        if not row:
            instr_ended = True
            continue
        if instr_ended:
            nodes[row[0:3]] = [row[7:10], row[12:15]]
        else:
            instr.extend(list(map(int, list(row.replace("L", "0").replace("R", "1")))))

    current = 'AAA'  # part 1
    steps = 0
    while not current == 'ZZZ':
        current = nodes[current][instr[steps % len(instr)]]
        steps += 1
    print(steps)  # 20569

    current = []  # part 2
    for key in nodes:
        if key[-1] == 'A':
            current.append(key)
    steps = [0 for _ in range(len(current))]
    for idx, key in enumerate(current):
        while not current[idx][-1] == 'Z':
            current[idx] = nodes[current[idx]][instr[steps[idx] % len(instr)]]
            steps[idx] += 1
    print(math.lcm(*steps))  # 21366921060721
