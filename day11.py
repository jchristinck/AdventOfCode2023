if __name__ == "__main__":
    t = [list(map(int, x.replace('.', '0').replace('#', '1'))) for x in
         open("input/day11.txt", "r").read().splitlines()]
    empty_rows = [sum(t[idy]) for idy in range(len(t))]
    empty_cols = [sum(t[idy][idx] for idy in range(len(t))) for idx in range(len(t[0]))]
    galaxies = [(idy + sum([1 for idz, el in enumerate(empty_rows) if (idz < idy and not el)]),
                 idx + sum([1 for idz, el in enumerate(empty_cols) if (idz < idx and not el)]))
                for idx in range(len(t[0])) for idy in range(len(t)) if t[idy][idx]]
    galaxies_f = [(idy + sum([10 ** 6 - 1 for idz, el in enumerate(empty_rows) if (idz < idy and not el)]),
                   idx + sum([10 ** 6 - 1 for idz, el in enumerate(empty_cols) if (idz < idx and not el)]))
                  for idx in range(len(t[0])) for idy in range(len(t)) if t[idy][idx]]
    print(sum([abs(yi - yj) + abs(xi - xj) for cg, (yi, xi) in enumerate(galaxies) for (yj, xj) in galaxies[:cg]]))
    print(sum([abs(yi - yj) + abs(xi - xj) for cg, (yi, xi) in enumerate(galaxies_f) for (yj, xj) in galaxies_f[:cg]]))
    # 9563821 and 827009909817
