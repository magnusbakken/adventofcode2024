import re

MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
MUL_RE2 = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")


def parse_input1(filename):
    with open(filename, "r") as f:
        return list(map(lambda x: (int(x[0]), int(x[1])), re.findall(MUL_RE, f.read())))


def parse_input2(filename):
    with open(filename, "r") as f:
        matches = re.findall(MUL_RE2, f.read())
        results = []
        for match in matches:
            if match[0] == "mul":
                results.append((int(match[1]), int(match[2])))
            elif match[3] == "do":
                results.append("do")
            elif match[4] == "don't":
                results.append("don't")
        return results


def part1():
    expressions = parse_input1("day3.txt")
    print(sum(x * y for x, y in expressions))


def part2():
    expressions = parse_input2("day3.txt")
    total = 0
    has_dont = False
    for expr in expressions:
        if expr == "do":
            has_dont = False
        elif expr == "don't":
            has_dont = True
        elif not has_dont:
            total += expr[0] * expr[1]
    print(total)


if __name__ == "__main__":
    part1()
    part2()
