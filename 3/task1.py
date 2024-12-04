import re
import sys


def main():
    program = sys.stdin.read()

    answer = 0
    for m in re.finditer(r"mul\((\d+),(\d+)\)", program):
        answer += int(m.group(1)) * int(m.group(2))
    print(answer)


if __name__ == "__main__":
    main()
