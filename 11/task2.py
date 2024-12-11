import fileinput
from collections import Counter


def main():
    stones = [
        int(stone) for line in fileinput.input() for stone in line.strip().split()
    ]
    stones = Counter(stones)

    # 75 blinks
    for _ in range(75):
        new_stones = Counter()

        for stone, count in stones.items():
            # rule 1: if the stone is engraved with the number 0,
            #         it is replaced by a stone engraved with the number 1.
            if stone == 0:
                new_stones[1] += count
            # rule 2: if the stone is engraved with a number that has
            #         an even number of digits, it is replaced by two stones.
            #         The left half of the digits are engraved on the new
            #         left stone, and the right half of the digits are
            #         engraved on the new right stone. (The new numbers don't
            #         keep extra leading zeroes: 1000 would become stones
            #         10 and 0.)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                new_stones[int(stone[: len(stone) // 2])] += count
                new_stones[int(stone[len(stone) // 2 :])] += count
            # rule 3: if none of the other rules apply, the stone is replaced
            #         by a new stone; the old stone's number multiplied by 2024
            #         is engraved on the new stone.
            else:
                new_stones[stone * 2024] += count

        stones = new_stones

    answer = sum(stones.values())
    print(answer)


if __name__ == "__main__":
    main()
