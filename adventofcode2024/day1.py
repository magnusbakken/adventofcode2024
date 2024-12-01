def parse_input(f):
    return [list(map(int, line.strip().split("   "))) for line in f]


def get_lists():
    with open("day1.txt") as f:
        return parse_input(f)


def part1():
    lists = get_lists()
    left, right = [l[0] for l in lists], [l[1] for l in lists]
    left.sort()
    right.sort()
    print(sum(abs(l - r) for l, r in zip(left, right)))


def part2():
    lists = get_lists()
    left, right = [l[0] for l in lists], [l[1] for l in lists]
    grouped = {}
    for r in right:
        if r not in grouped:
            grouped[r] = 0
        grouped[r] += 1

    total = 0
    for l in left:
        total += grouped.get(l, 0) * l

    print(total)


if __name__ == "__main__":
    part1()
    part2()
