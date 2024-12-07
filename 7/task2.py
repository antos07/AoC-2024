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
    # Here the 3rd type of equation is added: if the test_value
    # end with number[:-1] we can check concatenation
    for i, number in enumerate(reversed(numbers)):
        if test_value < 0:
            break
        if test_value % number == 0 and check_equation(
            test_value // number, numbers[: -(i + 1)]
        ):
            return True
        if (
            # this check is needed as we can't concatenate the number
            # with an empty string
            test_value != number
            and str(test_value).endswith(str(number))
            and check_equation(
                test_value=int(str(test_value).removesuffix(str(number))),
                numbers=numbers[: -(i + 1)],
            )
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
