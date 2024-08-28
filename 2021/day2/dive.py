
def read_data():
    with open('data.txt') as f:
        return f.readlines()


def implement_instructions(contents: list, hp: int, dp: int):

    for instruction in contents:
        split = instruction.split()
        direction = split[0]
        amount = int(split[1])


def change_position(direction: str, amount: int, hp: int, dp: int) -> tuple:
    pass


if __name__ == "__main__":

    hp = 0
    dp = 0

    file_contents = read_data()

    implement_instructions(file_contents, hp, dp)
