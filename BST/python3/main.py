import datetime
from typing import List
from tree import Tree


def get_add_numbers() -> List[int]:
    with open("/datasets/add.txt", "r") as file:
        content = file.read()
        numbers = list(map(int, content.split()))
    return numbers


def get_check_numbers() -> List[int]:
    with open("/datasets/check.txt", "r") as file:
        content = file.read()
        numbers = list(map(int, content.split()))
    return numbers


def main() -> None:
    add_results = []
    check_results = []
    len_results = []
    height_results = []

    add_numbers = get_add_numbers()
    check_numbers = get_check_numbers()


    for _ in range(3):
        bst = Tree()
        # Add elements
        start_time = datetime.datetime.now()
        for i in add_numbers:
            bst.add(i)
        end_time = datetime.datetime.now()
        add_results.append((end_time - start_time).total_seconds())

        # Len elements
        start_time = datetime.datetime.now()
        length = bst.length()
        end_time = datetime.datetime.now()
        len_results.append((end_time - start_time).total_seconds())
        print(f"{length=}")

        # height elements
        start_time = datetime.datetime.now()
        height = bst.height()
        end_time = datetime.datetime.now()
        height_results.append((end_time - start_time).total_seconds())
        print(f"{height=}")

        # Check elements
        start_time = datetime.datetime.now()
        for i in check_numbers:
            bst.contain(i)
        end_time = datetime.datetime.now()
        check_results.append((end_time - start_time).total_seconds())

    average_add = sum(add_results) / len(add_results)
    average_check = sum(check_results) / len(check_results)
    average_len = sum(len_results) / len(len_results)
    average_height = sum(height_results) / len(height_results)

    print(f"Average add: {average_add:.2f}")
    print(f"Average check: {average_check:.2f}")
    print(f"Average len: {average_len:.2f}")
    print(f"Average height: {average_height:.2f}")


if __name__ == "__main__":
    main()
