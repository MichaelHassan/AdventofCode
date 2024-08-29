def read_data():
    with open('data.txt') as f:
        return f.readlines()


def calc_surface_area(l: int, w: int, h: int) -> int:
    return 2*l*w + 2*w*h + 2*h*l


def get_smallest_side(constraints: list) -> int:

    constraints = sorted(constraints)

    return constraints[0] * constraints[1]


if __name__ == "__main__":

    file_contents = read_data()

    total = 0

    for line in file_contents:
        values = line.split("x")
        for i in range(0, len(values)):
            values[i] = int(values[i])

        total += calc_surface_area(values[0], values[1], values[2])
        total += get_smallest_side(values)

    print(total)
