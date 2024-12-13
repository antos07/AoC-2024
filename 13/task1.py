import fileinput
import math
import re
from dataclasses import dataclass

from more_itertools import batched


@dataclass
class Button:
    price: int
    dx: int
    dy: int


@dataclass
class Machine:
    button_a: Button
    button_b: Button
    prize_position: tuple[int, int]


def parse_button(line, price):
    m = re.match(r"Button [AB]: X\+(\d+), Y\+(\d+)", line)
    assert m is not None
    return Button(price, int(m.group(1)), int(m.group(2)))


def parse_prize_position(line):
    m = re.match(r"Prize: X=(\d+), Y=(\d+)", line)
    assert m is not None
    return int(m.group(1)), int(m.group(2))


def read_data():
    # Clearing the input from '\n'
    lines = (line.strip() for line in fileinput.input())
    # Removing empty lines
    lines = (line for line in lines if line)

    for line_button_a, line_button_b, line_prize_position in batched(
        lines, 3, strict=True
    ):
        button_a = parse_button(line_button_a, price=3)
        button_b = parse_button(line_button_b, price=1)
        yield Machine(button_a, button_b, parse_prize_position(line_prize_position))


def is_integer(n):
    return math.isclose(n, round(n))


def solve(machine):
    # PROBLEM
    #
    # a * x1 + b * x2 = X
    # a * y1 + b * y2 = Y
    # 3 * a + b -> min
    #
    # where (x1, y1), (y1, y2) - dx and dy of the buttons A and B respectively,
    # X and Y - the prize position,
    # a, b - how many times to push the respective button.
    #
    # ------------------------------------------------------------------------
    # SOLUTION
    #
    # b = (X - a * x1) / x2
    #
    # a * y1 + (X - a * x1) / x2 * y2 = Y
    # a * y1 + X / x2 * y2 - a * x1 / x2  * y2 = Y
    # a * (y1 - x1 / x2  * y2) = Y - X / x2 * y2
    # a = (Y - X / x2 * y2) / (y1 - x1 / x2 * y2)
    #
    # Here I assumed that there is no 0 values.

    x1 = machine.button_a.dx
    y1 = machine.button_a.dy
    x2 = machine.button_b.dx
    y2 = machine.button_b.dy
    X, Y = machine.prize_position

    a = (Y - X / x2 * y2) / (y1 - x1 / x2 * y2)
    if not is_integer(a):
        return 0
    a = round(a)

    b = (X - a * x1) / x2
    if not is_integer(b):
        return 0
    b = round(b)

    if a > 100 or b > 100:
        return 0

    return machine.button_a.price * a + machine.button_b.price * b


def main():
    machines = read_data()
    answer = sum(solve(machine) for machine in machines)
    print(answer)


if __name__ == "__main__":
    main()
