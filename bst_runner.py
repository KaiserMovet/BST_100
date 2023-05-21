from pathlib import Path
from app import BST, Result, ResultCollection
from multiprocessing import Pool
from pprint import pprint
class BSTCollection:
    PYTHON = BST("Python 3.11.0", Path("BST/python3/run.sh"))

    @classmethod
    def get_all(cls):
        return [cls.PYTHON]


def run(bst: BST, amount:int) -> Result:
    return bst.run(amount)


def main():
    arg_coll = []
    for bst in BSTCollection.get_all():
        for amount in [20, 40]:
            for _ in range(3):
                arg_coll.append((bst, amount))

 
    with Pool() as pool:
        results = pool.starmap(run, arg_coll)
    results = ResultCollection(results)
    pprint(results)
    results.plot_all()
    pass

if __name__ == "__main__":
    main()