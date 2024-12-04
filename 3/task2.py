import re
import sys


def main():
    program = sys.stdin.read()

    answer = 0
    enabled = True
    for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", program):
        if m.group() == "do()":
            enabled = True
        elif m.group() == "don't()":
            enabled = False
        elif enabled:
            answer += int(m.group(1)) * int(m.group(2))
    print(answer)


if __name__ == "__main__":
    main()
