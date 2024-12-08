import itertools as it
import operator


def concatNums(a, b):
    return int(str(a) + str(b))


class Line:
    def __init__(self, s, concatenation=False):
        answer, numbers = s.split(": ")
        self.answer = int(answer)
        self.numbers = list(map(int, numbers.split(" ")))
        self.concatenation = concatenation

    def __repr__(self):
        return f"Line({self.answer}: {' '.join(str(n) for n in self.numbers)})"

    def __str__(self):
        return f"{self.answer}: {' '.join(str(n) for n in self.numbers)}"

    def evaluate(self, operators):
        total = self.numbers[0]
        for idx, op in enumerate(operators):
            total = op(total, self.numbers[idx + 1])
        return total

    def is_solvable(self):
        op_count = len(self.numbers) - 1
        ops = self.get_operators()
        operator_lists = it.product(ops, repeat=op_count)
        for operators in operator_lists:
            if self.evaluate(operators) == self.answer:
                return True
        return False

    def get_operators(self):
        operators = [operator.add, operator.mul]
        if self.concatenation:
            operators.append(concatNums)
        return operators


def parse_file(concatenation=False):
    with open("day7.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        return [Line(line, concatenation) for line in lines]


def part1():
    total = 0
    lines = parse_file()
    for line in lines:
        if line.is_solvable():
            total += line.answer
    print(total)


def part2():
    total = 0
    lines = parse_file(concatenation=True)
    for line in lines:
        if line.is_solvable():
            total += line.answer
    print(total)


if __name__ == "__main__":
    part1()
    part2()
