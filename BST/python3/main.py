import time
from typing import List
from tree import Tree
import sys


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

    amount = int(sys.argv[1])

    add_numbers = get_add_numbers()[:amount]
    check_numbers = get_check_numbers()[:amount]


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
