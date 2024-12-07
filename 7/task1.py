import sys


def read_equations():
    equations = []
    for line in sys.stdin:
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = [int(number) for number in numbers.strip().split()]
        equations.append((test_value, numbers))
    return equations


def check_equation(test_value, numbers):
    # The idea is to solve this task recursively. The equation
    # {test_number}: {numbers}
    # will only be valid, if valid is either the equation
    # {test_number - numbers[-1]}: {numbers[:-1]}
    # or assuming that test_number % numbers[-1] == 0
    # the equation {test_number // numbers[-1]}: {numbers[:-1]}
    #
    # There is no reason to subtract every number recursively - that
    # can be easily be done in a simple loop. But branches, where we
    # perform the division, will indeed be recursive.
    for i, number in enumerate(reversed(numbers)):
        if test_value < 0:
            break
        if test_value % number == 0 and check_equation(
            test_value // number, numbers[: -(i + 1)]
        ):
            return True
        test_value -= number

    return test_value == 0


def main():
    equations = read_equations()

    answer = sum(
        test_value
        for test_value, numbers in equations
        if check_equation(test_value, numbers)
    )
    print(answer)


if __name__ == "__main__":
    main()
