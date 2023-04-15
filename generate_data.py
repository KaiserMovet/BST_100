import random


def save_numbers(filename, amount):
    num_list = list(range(1, amount + 1))
    random.shuffle(num_list)
    rand_nums = num_list[:amount]
    with open(filename, "w") as file:
        for num in rand_nums:
            file.write(str(num) + "\n")


def main():
    save_numbers("datatests/add.txt", 10_000_000)
    save_numbers("datatests/check.txt", 20_000_000)


if __name__ == "__main__":
    main()
