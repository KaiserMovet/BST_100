from dataclasses import dataclass
from typing import Callable, List, Dict
from collections import defaultdict
import matplotlib.pyplot as plt


class ResultValidation(Exception):
    pass


@dataclass
class Result:
    name: str
    amount: int
    add: float
    check: float
    len: float
    height: float
    validation: tuple

    # def __post_init__(self) -> None:
    #     if self.validation != ("5000000", "57"):
    #         raise ResultValidation(F"Current validation is {self.validation}")

    @staticmethod
    def FROM_RESULT(name:str, amount:int, result: str) -> "Result":
        add = None
        check = None
        len = None
        height = None
        val = None
        for line in result.splitlines():
            if "ADD_TEST" in line:
                add = float(line.split(":")[1])
            if "CHECK_TEST" in line:
                check = float(line.split(":")[1])
            if "LEN_TEST" in line:
                len = float(line.split(":")[1])
            if "HEIGHT_TEST" in line:
                height = float(line.split(":")[1])
            if "VALIDATION" in line:
                val = (int(line.split(":")[1]), int(line.split(":")[2]))
        return Result(name=name,
                      amount=amount,
                      add=add, #type: ignore
                      check=check, #type: ignore
                      height=height, #type: ignore
                      len=len, #type: ignore
                      validation=val, #type: ignore
                    )
    @staticmethod
    def FROM_AVG(results: List["Result"]) -> "Result":
        res_len = len(results)
        add = 0.0
        check = 0.0
        leng = 0.0
        height = 0.0
        for result in results:
            add += result.add
            check += result.check
            leng += result.len
            height += result.height
        return Result(
            name = results[0].name,
            amount = results[0].amount,
            add=add/res_len,
            check=check/res_len,
            len=leng/res_len,
            height=height/res_len,
            validation=results[0].validation,
        )


class ResultCollection:
    def __init__(self, results: List[Result]) -> None:
        temp_data = defaultdict(lambda: defaultdict(list))
        for result in results:
            temp_data[result.name][result.amount].append(result)
        
        self.data = defaultdict(lambda: {})
        for name in temp_data.keys():
            for amount, results in temp_data[name].items():
                self.data[name][amount] = Result.FROM_AVG(results)

    def _plot(self, title: str, picture_name:str, result_func: Callable) -> None:
        for key, values in self.data.items():
            keys = list(values.keys())
            add_values = [result_func(result) for result in values.values()]

            plt.plot(keys, add_values, label=key)
            plt.scatter(keys, add_values)
            
        plt.xlabel('Amount of elements in BST')
        plt.ylabel('Time (s)')
        plt.title(title)
        plt.legend()
        plt.savefig(f'./results/{picture_name}.jpg')
        plt.clf()
        
    def plot_add(self) -> None:
        self._plot("Adding elements", "add", lambda x: x.add)

    def plot_check(self) -> None:
        self._plot("Checking elements", "check", lambda x: x.check)

    def plot_height(self) -> None:
        self._plot("Counting height of BST", "height", lambda x: x.height)

    def plot_len(self) -> None:
        self._plot("Counting elements", "len", lambda x: x.len)
    
    def plot_all(self) -> None:
        self.plot_add()
        self.plot_check()
        self.plot_height()
        self.plot_len()


    
    def __repr__(self):
        return repr(self.data)