import itertools
import sys


# From Task 1
def is_report_safe_without_modifications(report):
    if len(report) < 2:
        return True

    is_ascending = report[0] < report[1]
    for level1, level2 in itertools.pairwise(report):
        # A report is considered as safe when two conditions are satisfied:

        # 1. All levels are strictly ascending or descending
        if (level1 < level2) is not is_ascending:
            return False

        # 2. Any two adjacent levels differ by at least 1 and at most 3
        if not 1 <= abs(level1 - level2) <= 3:
            return False

    return True


def is_report_safe(report):
    # Knowing that there are only 5 levels in a report, it's OK to check
    # all possible reports with one level removed.
    for i in range(len(report)):
        # the level at position i will be removed from the report
        if is_report_safe_without_modifications(report[:i] + report[i + 1 :]):
            return True

    return False


def main():
    # Input
    reports = []
    for line in sys.stdin:
        reports.append([int(level) for level in line.split()])

    # Counting safe levels
    answer = sum(1 for report in reports if is_report_safe(report))
    print(answer)


if __name__ == "__main__":
    main()
