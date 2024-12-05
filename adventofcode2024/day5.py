import itertools as it


def read_file():
    orderings = []
    productions = []
    with open("day5.txt", "r") as f:
        lines = f.read().splitlines()
        idx = 0
        for i in range(len(lines)):
            line = lines[i]
            if line == "":
                idx = i
                break
            x, y = line.split("|")
            orderings.append((int(x), int(y)))
        for line in lines[idx + 1 :]:
            productions.append(tuple(map(int, line.split(","))))
    return orderings, productions


def is_well_ordered(production, orderings):
    for a, b in it.combinations(production, 2):
        for x, y in orderings:
            if a == y and b == x:
                return False
    return True


def get_first_ordering_problem(production, orderings):
    for a, b in it.combinations(production, 2):
        for x, y in orderings:
            if a == y and b == x:
                return (a, b)
    return None


def swap(production, a, b):
    new_production = list(production)
    a_idx = new_production.index(a)
    b_idx = new_production.index(b)
    new_production[a_idx], new_production[b_idx] = (
        new_production[b_idx],
        new_production[a_idx],
    )
    return tuple(new_production)


def part1():
    total = 0
    orderings, productions = read_file()
    for production in productions:
        if is_well_ordered(production, orderings):
            middle_page = production[len(production) // 2]
            total += middle_page
    print(total)


def part2():
    total = 0
    orderings, productions = read_file()
    for production in productions:
        problem = get_first_ordering_problem(production, orderings)
        if problem is None:
            continue
        while problem is not None:
            production = swap(production, problem[0], problem[1])
            problem = get_first_ordering_problem(production, orderings)
        middle_page = production[len(production) // 2]
        total += middle_page

    print(total)


if __name__ == "__main__":
    part1()
    part2()
