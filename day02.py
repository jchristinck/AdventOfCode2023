if __name__ == "__main__":
    text = open("input/day02.txt", "r").read().splitlines()
    ids = []
    minCubes = 0
    for row in text:
        row = row.split(":")
        ids.append(int(row[0].split(" ")[-1]))
        minNumOfBalls = [0, 0, 0]  # red, green, blue
        picks = row[1].split(";")
        for pick in picks:
            sorts = pick[1:].split(", ")
            for sort in sorts:
                (amount, color) = sort.split(" ")
                match color:
                    case "red":
                        minNumOfBalls[0] = max(minNumOfBalls[0], int(amount))
                        if int(amount) > 12:
                            ids[-1] = 0
                    case "green":
                        minNumOfBalls[1] = max(minNumOfBalls[1], int(amount))
                        if int(amount) > 13:
                            ids[-1] = 0
                    case "blue":
                        minNumOfBalls[2] = max(minNumOfBalls[2], int(amount))
                        if int(amount) > 14:
                            ids[-1] = 0
        minCubes += minNumOfBalls[0] * minNumOfBalls[1] * minNumOfBalls[2]
    print(sum(ids))
    print(minCubes)
