from pathlib import Path
from app import BST, Result, ResultCollection
from multiprocessing import Pool
from pprint import pprint
from logger import logger

class BSTCollection:
    PYTHON = BST("Python 3.11.0", Path("BST/python3/run.sh"))
    RUST = BST("Rust 1.67", Path("BST/rust/run.sh"))
    C = BST("C c99", Path("BST/c/run.sh"))
    CPP = BST("C++ gcc 12", Path("BST/c++/run.sh"))




    @classmethod
    def get_all(cls):
        return [cls.PYTHON, cls.RUST, cls.C, cls.CPP]


def run(bst: BST, amount:int) -> Result:
    logger.info(f"Running {bst.name} for {amount} elements")
    res = bst.run(amount)
    logger.info(f"Finish {bst.name} for {amount} elements")
    return res



def main():
    arg_coll = []
    for bst in BSTCollection.get_all():
        for amount in [20, 40, 500]:
            for _ in range(1):
                arg_coll.append((bst, amount))

    with Pool() as pool:
        results = pool.starmap(run, arg_coll)
    results = ResultCollection(results)
    results.plot_all()
    pass

if __name__ == "__main__":
    main()