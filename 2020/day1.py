

def read_data():
    with open('data.txt') as f:
        return f.read().splitlines()


def find_pair(numbers: list, total: int) -> list:

    numbers = list(map(int, numbers))

    for number in numbers:
        remainder = total - number
        if remainder in numbers:
            return [number, remainder]

    return []


def find_answer(pair: list) -> int:

    if not pair:
        return 0

    if len(pair) > 2:
        raise ValueError("NOT A PAIR")

    return pair[0]*pair[1]


if __name__ == "__main__":

    data = read_data()

    print(find_answer(find_pair(data, 2020)))
