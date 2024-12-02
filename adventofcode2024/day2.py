def parse_input(filename):
    with open(filename, "r") as f:
        return [list(map(int, line.strip().split(" "))) for line in f.readlines()]


def is_safe(series):
    current = None
    ascending = None
    for c in series:
        if current is not None:
            if ascending is None:
                ascending = c > current
            if c == current:
                return False
            elif abs(c - current) > 3:
                return False
            elif ascending and c < current or (not ascending and c > current):
                return False
        current = c
    return True


def part1():
    reports = parse_input("day2.txt")
    print(len([report for report in reports if is_safe(report)]))


def part2():
    reports = parse_input("day2.txt")
    total = 0
    for report in reports:
        if is_safe(report):
            total += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    total += 1
                    break
    print(total)


if __name__ == "__main__":
    part1()
    part2()
