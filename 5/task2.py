import sys
from collections import defaultdict
from functools import cmp_to_key


def is_update_valid(update, page_requires):
    unprocessed_pages = set(update)
    for page in update:
        unprocessed_pages.remove(page)

        # A set of required pages should be a subset of processed pages
        if page_requires[page] & unprocessed_pages:
            print(f"Invalid: {update}")
            return False

    print(f"Valid: {update}")
    return True


def get_middle_page(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


def fix_update(update, page_requires):
    def compare(item1, item2):
        # returns -1 if item1 should be before item2
        # returns 1 if item1 should be after item2
        # returns 0 in other cases

        if item2 in page_requires[item1]:
            assert item1 not in page_requires[item2]
            return 1
        if item1 in page_requires[item2]:
            assert item2 not in page_requires[item1]
            return -1
        return 0

    return sorted(update, key=cmp_to_key(compare))


def main():
    # Read section 1 of an input file (page ordering rules)
    page_requires = defaultdict(set)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            # The end of section 1
            break

        page_before, page_after = map(int, line.split("|"))
        page_requires[page_after].add(page_before)

    # Read section 2 of the input file (updates)
    updates = []
    for line in sys.stdin:
        line = line.strip()
        updates.append([int(page) for page in line.split(",")])

    answer = sum(
        get_middle_page(fix_update(update, page_requires))
        for update in updates
        if not is_update_valid(update, page_requires)
    )
    print(answer)


if __name__ == "__main__":
    main()
