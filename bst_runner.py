from pathlib import Path
from app import BST, Result, ResultCollection
from multiprocessing import Pool
from pprint import pprint
from logger import logger
import random


class BSTCollection:
    PYTHON = BST("Python 3.11.0", Path("BST/python3/run.sh"))
    RUST = BST("Rust 1.67", Path("BST/rust/run.sh"))
    C = BST("C c99", Path("BST/c/run.sh"))
    CPP = BST("C++ gcc12", Path("BST/c++/run.sh"))
    LUA = BST("Lua 5.4.3", Path("BST/lua/run.sh"))





    @classmethod
    def get_all(cls):
        return [cls.PYTHON, cls.RUST, cls.C, cls.CPP, cls.LUA]


def run(bst: BST, amount:int) -> Result:
    logger.info(f"Running {bst.name} for {amount} elements")
    res = bst.run(amount)
    logger.info(f"Finish {bst.name} for {amount} elements")
    return res



def main():
    arg_coll = []
    for bst in BSTCollection.get_all():
        for amount in [100,1_000,10_000, 100_000, 1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000,6_000_000,7_000_000,8_000_000,9_000_000,10_000_000]:
            for _ in range(3):
                arg_coll.append((bst, amount))
    random.shuffle(arg_coll)
    with Pool(processes=5) as pool:
        results = pool.starmap(run, arg_coll)
    results = ResultCollection(results)
    results.plot_all()
    results.to_json()
    pass

if __name__ == "__main__":
    main()