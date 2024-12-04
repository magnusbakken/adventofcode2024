def read_file():
    with open("day4.txt", "r") as f:
        lines = f.read().splitlines()
        return [[c for c in line] for line in lines]


def find_sequences(x, y, data):
    if x < len(data) - 3:
        yield data[x][y] + data[x + 1][y] + data[x + 2][y] + data[x + 3][y]
    if x > 2:
        yield data[x][y] + data[x - 1][y] + data[x - 2][y] + data[x - 3][y]
    if y < len(data[0]) - 3:
        yield data[x][y] + data[x][y + 1] + data[x][y + 2] + data[x][y + 3]
    if y > 2:
        yield data[x][y] + data[x][y - 1] + data[x][y - 2] + data[x][y - 3]
    if x < len(data) - 3 and y < len(data[0]) - 3:
        yield data[x][y] + data[x + 1][y + 1] + data[x + 2][y + 2] + data[x + 3][y + 3]
    if x > 2 and y > 2:
        yield data[x][y] + data[x - 1][y - 1] + data[x - 2][y - 2] + data[x - 3][y - 3]
    if x < len(data) - 3 and y > 2:
        yield data[x][y] + data[x + 1][y - 1] + data[x + 2][y - 2] + data[x + 3][y - 3]
    if x > 2 and y < len(data[0]) - 3:
        yield data[x][y] + data[x - 1][y + 1] + data[x - 2][y + 2] + data[x - 3][y + 3]


def is_cross_center(x, y, data):
    if data[x][y] != "A":
        return False

    if (
        data[x - 1][y - 1] == "M"
        and data[x - 1][y + 1] == "M"
        and data[x + 1][y - 1] == "S"
        and data[x + 1][y + 1] == "S"
    ):
        return True
    elif (
        data[x - 1][y - 1] == "S"
        and data[x - 1][y + 1] == "S"
        and data[x + 1][y - 1] == "M"
        and data[x + 1][y + 1] == "M"
    ):
        return True
    elif (
        data[x - 1][y + 1] == "S"
        and data[x + 1][y + 1] == "S"
        and data[x - 1][y - 1] == "M"
        and data[x + 1][y - 1] == "M"
    ):
        return True
    elif (
        data[x - 1][y + 1] == "M"
        and data[x + 1][y + 1] == "M"
        and data[x - 1][y - 1] == "S"
        and data[x + 1][y - 1] == "S"
    ):
        return True
    return False


def part1():
    data = read_file()
    total = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            for coords in find_sequences(x, y, data):
                if "".join(coords) == "XMAS":
                    total += 1
    print(total)


def part2():
    data = read_file()
    total = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[0]) - 1):
            if is_cross_center(x, y, data):
                total += 1
    print(total)


if __name__ == "__main__":
    part1()
    part2()
