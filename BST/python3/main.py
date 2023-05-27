import sys
import time
from typing import List

from tree import Tree


def get_numbers(path) -> List[int]:
    with open(path, "r") as file:
        content = file.read()
        numbers = list(map(int, content.split()))
    return numbers


def main() -> None:
    amount = int(sys.argv[1])

    add_numbers = get_numbers("/datasets/add.txt")[:amount]
    check_numbers = get_numbers("/datasets/check.txt")[:amount]

    bst = Tree()

    # Add elements
    start_time = time.time()
    for i in add_numbers:
        bst.add(i)
    end_time = time.time()
    print(f"ADD_TEST:{end_time - start_time}")

    # Check elements
    start_time = time.time()
    for i in check_numbers:
        bst.contain(i)
    end_time = time.time()
    print(f"CHECK_TEST:{end_time - start_time}")

    # Len elements
    start_time = time.time()
    for _ in range(10):
        bst.length()
    end_time = time.time()
    print(f"LEN_TEST:{(end_time - start_time)/10}")

    # Height elements
    start_time = time.time()
    for _ in range(10):
        bst.height()
    end_time = time.time()
    print(f"HEIGHT_TEST:{(end_time - start_time)/10}")

    print(f"VALIDATION:{bst.length()}:{bst.height()}")


if __name__ == "__main__":
    main()
