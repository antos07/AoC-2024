import fileinput


def main():
    stones = [
        int(stone) for line in fileinput.input() for stone in line.strip().split()
    ]

    # 25 blinks
    for _ in range(25):
        new_stones = []
        for stone in stones:
            # rule 1: if the stone is engraved with the number 0,
            #         it is replaced by a stone engraved with the number 1.
            if stone == 0:
                new_stones.append(1)
            # rule 2: if the stone is engraved with a number that has
            #         an even number of digits, it is replaced by two stones.
            #         The left half of the digits are engraved on the new
            #         left stone, and the right half of the digits are
            #         engraved on the new right stone. (The new numbers don't
            #         keep extra leading zeroes: 1000 would become stones
            #         10 and 0.)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                new_stones += [
                    int(stone[: len(stone) // 2]),
                    int(stone[len(stone) // 2 :]),
                ]
            # rule 3: if none of the other rules apply, the stone is replaced
            #         by a new stone; the old stone's number multiplied by 2024
            #         is engraved on the new stone.
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    print(len(stones))


if __name__ == "__main__":
    main()
