import itertools
import sys
from contextlib import suppress

import more_itertools


def rotate(original):
    return list(zip(*original))[::-1]


def puzzle_rotations(puzzle):
    for _ in range(4):
        yield puzzle
        puzzle = rotate(puzzle)


XMAS = "XMAS"


def main():
    puzzle = list(sys.stdin)

    answer = 0
    for rotation in puzzle_rotations(puzzle):
        # firstly count normal XMAS entries
        for line in rotation:
            for word in more_itertools.windowed(line, len(XMAS)):
                word = "".join(word)
                if word == XMAS:
                    answer += 1

        # and then diagonal
        for i, j in itertools.product(range(len(rotation)), range(len(rotation[0]))):
            with suppress(IndexError):
                word = ""
                for k in range(len(XMAS)):
                    word += rotation[i + k][j + k]
                if word == XMAS:
                    answer += 1
    print(answer)


if __name__ == "__main__":
    main()
