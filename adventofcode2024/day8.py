import itertools as it


def read_input():
    with open("day8.txt") as f:
        return [c for c in f.read().splitlines()]


def get_map(symbol, antenna_map):
    return [
        (x, y)
        for x in range(len(antenna_map))
        for y in range(len(antenna_map[0]))
        if antenna_map[x][y] == symbol
    ]


def get_single_antinodes(symbol_map):
    # because of the way we read the data, we know that x1 <= x2
    for (x1, y1), (x2, y2) in it.combinations(symbol_map, 2):
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        if y1 > y2:
            yield (x1 - x_diff, y1 + y_diff)
            yield (x2 + x_diff, y2 - y_diff)
        else:
            yield (x1 - x_diff, y1 - y_diff)
            yield (x2 + x_diff, y2 + y_diff)


def get_all_antinodes(symbol_map, antenna_map):
    # again, because of the way we read the data, we know that x1 <= x2
    for (x1, y1), (x2, y2) in it.combinations(symbol_map, 2):
        # the antenna nodes themselves will always be included
        yield (x1, y1)
        yield (x2, y2)

        x_min = x1
        x_max = x2
        x_diff = abs(x1 - x2)

        y_min = min(y1, y2)
        y_max = max(y1, y2)
        y_diff = abs(y1 - y2)

        if y1 > y2:
            x = x_min - x_diff
            y = y_max + y_diff
            while 0 <= x < len(antenna_map) and 0 <= y < len(antenna_map[0]):
                yield (x, y)
                x -= x_diff
                y += y_diff
            x = x_max + x_diff
            y = y_min - y_diff
            while 0 <= x < len(antenna_map) and 0 <= y < len(antenna_map[0]):
                yield (x, y)
                x += x_diff
                y -= y_diff
        else:
            x = x_min - x_diff
            y = y_min - y_diff
            while 0 <= x < len(antenna_map) and 0 <= y < len(antenna_map[0]):
                yield (x, y)
                x -= x_diff
                y -= y_diff
            x = x_max + x_diff
            y = y_max + y_diff
            while 0 <= x < len(antenna_map) and 0 <= y < len(antenna_map[0]):
                yield (x, y)
                x += x_diff
                y += y_diff


def get_possible_antinodes(symbol_map, antenna_map, multi):
    if multi:
        yield from get_all_antinodes(symbol_map, antenna_map)
    else:
        for x, y in get_single_antinodes(symbol_map):
            if 0 <= x < len(antenna_map) and 0 <= y < len(antenna_map[0]):
                yield (x, y)


def calculate(multi=False):
    seen_antinodes = set()
    antenna_map = read_input()
    distinct_symbols = set(c for line in antenna_map for c in line if c != ".")
    symbol_maps = {symbol: get_map(symbol, antenna_map) for symbol in distinct_symbols}
    for symbol_map in symbol_maps.values():
        for antinode in get_possible_antinodes(symbol_map, antenna_map, multi):
            seen_antinodes.add(antinode)
    print(len(seen_antinodes))


def part1():
    calculate()


def part2():
    calculate(multi=True)


if __name__ == "__main__":
    part1()
    part2()
