def parse_position():
    with open("day6.txt", "r") as f:
        lines = f.read().splitlines()
        return [[c for c in line] for line in lines]


def find_starting_position(data):
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == "^":
                return x, y
    raise Exception("No starting position found.")


def is_in_bounds(x, y, data):
    return 0 <= x < len(data) and 0 <= y < len(data[0])


def get_next_position(x, y, direction):
    if direction == "up":
        return x - 1, y
    elif direction == "down":
        return x + 1, y
    elif direction == "left":
        return x, y - 1
    elif direction == "right":
        return x, y + 1
    else:
        raise Exception("Invalid direction.")


def get_next_direction(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"
    else:
        raise Exception("Invalid direction.")


def has_loop(position):
    seen_states = set()
    x, y = find_starting_position(position)
    direction = "up"
    while is_in_bounds(x, y, position):
        if (x, y, direction) in seen_states:
            return True
        seen_states.add((x, y, direction))
        next_x, next_y = get_next_position(x, y, direction)
        if not is_in_bounds(next_x, next_y, position):
            return False
        elif position[next_x][next_y] == "#":
            direction = get_next_direction(direction)
        else:
            x, y = next_x, next_y


def part1():
    visited = set()
    position = parse_position()
    x, y = find_starting_position(position)
    direction = "up"
    while is_in_bounds(x, y, position):
        visited.add((x, y))
        next_x, next_y = get_next_position(x, y, direction)
        if not is_in_bounds(next_x, next_y, position):
            break
        elif position[next_x][next_y] == "#":
            direction = get_next_direction(direction)
        else:
            x, y = next_x, next_y
    print(len(visited))


def part2():
    loops = 0
    position = parse_position()
    for x in range(len(position)):
        for y in range(len(position[0])):
            if position[x][y] == ".":
                position[x][y] = "#"
                if has_loop(position):
                    loops += 1
                position[x][y] = "."
    print(loops)


if __name__ == "__main__":
    part1()
    part2()
