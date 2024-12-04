import sys


def main():
    # There are two columns of numbers, which have the same length,
    # so reading them.
    left_list, right_list = [], []
    for line in sys.stdin:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # The answer to the task is a sum of differences between numbers
    # that have the same positions in the sorted lists.
    left_list.sort()
    right_list.sort()
    answer = sum(abs(left - right) for left, right in zip(left_list, right_list))
    print(answer)


if __name__ == "__main__":
    main()
