import sys
from collections import Counter


def main():
    # There are two columns of numbers, which have the same length,
    # so reading them.
    left_list, right_list = [], []
    for line in sys.stdin:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # To find the answer:
    # 1. Count all numbers in the right list
    # 2. Sum the products of numbers from the left list and the number of times
    #    they occur in the right list
    right_counted = Counter(right_list)
    answer = sum(left * right_counted[left] for left in left_list)
    print(answer)


if __name__ == "__main__":
    main()
