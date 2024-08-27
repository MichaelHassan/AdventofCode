

def read_data():
    with open('data.txt') as f:
        return f.readlines()


def count_increases_single(depths: list) -> int:
    count = 0
    temp = int(depths[0])

    for i in range(1, len(depths)):
        number = int(depths[i])
        if temp < number:
            count += 1

        temp = number

    return count


def count_increases_multiple(depths: list) -> int:
    count = 0
    temp = int(depths[0]) + int(depths[1]) + int(depths[2])

    for i in range(1, len(depths) - 2):
        number = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
        if temp < number:
            count += 1

        temp = number

    return count


if __name__ == "__main__":

    file_contents = read_data()

    print(count_increases_single(file_contents))

    print(count_increases_multiple(file_contents))
