import itertools
import sys

MAS = "MAS"


def get_x(puzzle, center):
    return (
        "".join(
            [
                puzzle[center[0] - 1][center[1] - 1],
                puzzle[center[0]][center[1]],
                puzzle[center[0] + 1][center[1] + 1],
            ]
        ),
        "".join(
            [
                puzzle[center[0] + 1][center[1] - 1],
                puzzle[center[0]][center[1]],
                puzzle[center[0] - 1][center[1] + 1],
            ]
        ),
    )


def main():
    puzzle = list(sys.stdin)

    answer = 0
    for center in itertools.product(
        range(1, len(puzzle) - 1), range(1, len(puzzle[0]) - 1)
    ):
        try:
            w1, w2 = get_x(puzzle, center)
        except IndexError:
            continue

        if (w1 == MAS or w1[::-1] == MAS) and (w2 == MAS or w2[::-1] == MAS):
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
