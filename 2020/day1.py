
from math import prod


def read_data():
    with open('data.txt') as f:
        return f.read().splitlines()


def find_pair(numbers: list, total: int) -> list:

    numbers = list(map(int, numbers))

    for number in numbers:
        remainder = total - number
        if remainder in numbers:
            return [number, remainder]

    return None


def find_triplets(numbers: list, total: int) -> list:

    numbers = list(map(int, numbers))

    while len(numbers) != 0:
        number = numbers.pop()
        remainder = total - number
        last_two = find_pair(numbers, remainder)
        if last_two:
            last_two.append(number)
            return last_two

    return None


def find_answer(pair: list) -> int:

    if not pair:
        return 0

    return prod(pair)


if __name__ == "__main__":

    data = read_data()

    print(find_answer(find_triplets(data, 2020)))
