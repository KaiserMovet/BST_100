from pathlib import Path
from app import BST, Result, ResultCollection
from multiprocessing import Pool
from logger import logger
import random
import sys
from typing import List


class BSTCollection:
    PYTHON = BST("Python 3.11.0", Path("BST/python3/run.sh"))
    RUST = BST("Rust 1.67", Path("BST/rust/run.sh"))
    C = BST("C c99", Path("BST/c/run.sh"))
    CPP = BST("C++ gcc12", Path("BST/c++/run.sh"))
    LUA = BST("Lua 5.4.3", Path("BST/lua/run.sh"))
    CS = BST("CSharp 5.0", Path("BST/c#/run.sh"))

    
    @classmethod
    def get_by_name(cls, name: str):
        for bst in cls.get_all():
            if bst.name.split()[0].lower() == name.lower():
                return bst
        logger.warning(F"Cannot find bst with '{name}' name")
        return None

    @classmethod
    def get_all(cls) -> List[BST]:
        return [cls.PYTHON, cls.RUST, cls.C, cls.CPP, cls.LUA, cls.CS]


def run(bst: BST, amount:int) -> Result:
    logger.info(f"Running {bst.name} for {amount} elements")
    res = bst.run(amount)
    logger.info(f"Finish {bst.name} for {amount} elements")
    return res



def main():

    bst_to_calculate = []
    if len(sys.argv) <= 1:
        bst_to_calculate = BSTCollection.get_all()
    else:
        bst_to_calculate = [BSTCollection.get_by_name(sys.argv[1])]

    arg_coll = []
    for bst in bst_to_calculate:
        for amount in [100,1_000,10_000, 100_000, 1_000_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000,6_000_000,7_000_000,8_000_000,9_000_000,10_000_000]:
            for _ in range(3):
                arg_coll.append((bst, amount))
    random.shuffle(arg_coll)
    with Pool(processes=1) as pool:
        results = pool.starmap(run, arg_coll)
    results = ResultCollection(results)
    results.plot_all()
    results.to_json(merge_with_existing=True)
    pass

if __name__ == "__main__":
    main()