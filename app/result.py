import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from typing import Any, Callable, Dict, List

import matplotlib.pyplot as plt

from logger import logger


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

    def __post_init__(self) -> None:
        if int(self.validation[0]) != self.amount:
            raise ResultValidation(
                f"Current validation is {self.validation[0]} and it should be {self.amount}"
            )

    def asdict(self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def has_none(self):
        return any(
            [
                key is None
                for key in [
                    self.add,
                    self.check,
                    self.len,
                    self.height,
                    self.validation,
                ]
            ]
        )

    @staticmethod
    def FROM_RESULT(name: str, amount: int, result: str) -> "Result":
        add = None
        check = None
        leng = None
        height = None
        val = None
        for line in result.splitlines():
            if "ADD_TEST" in line:
                add = float(line.split(":")[1])
            if "CHECK_TEST" in line:
                check = float(line.split(":")[1])
            if "LEN_TEST" in line:
                leng = float(line.split(":")[1])
            if "HEIGHT_TEST" in line:
                height = float(line.split(":")[1])
            if "VALIDATION" in line:
                val = (int(line.split(":")[1]), int(line.split(":")[2]))
        if any([key is None for key in [add, check, leng, height, val]]):
            logger.error(
                f"Cannot find all keys in {name}:{amount}. Full output:\n{result}"
            )
        return Result(
            name=name,
            amount=amount,
            add=add,  # type: ignore
            check=check,  # type: ignore
            height=height,  # type: ignore
            len=leng,  # type: ignore
            validation=val,  # type: ignore
        )

    @staticmethod
    def FROM_AVG(results: List["Result"]) -> "Result":
        res_len = len(results)
        add = 0.0
        check = 0.0
        leng = 0.0
        height = 0.0
        for result in results:
            if result.has_none:
                res_len -= 1
                logger.warning(
                    f"Ommiting result in {results[0].name}:{results[0].amount}"
                )
                continue
            add += result.add
            check += result.check
            leng += result.len
            height += result.height
        if res_len == 1:
            logger.critical(
                f"Cannot get average result for {results[0].name}:{results[0].amount}"
            )
            raise ResultValidation(
                f"Cannot get average result for {results[0].name}:{results[0].amount}"
            )
        return Result(
            name=results[0].name,
            amount=results[0].amount,
            add=add / res_len,
            check=check / res_len,
            len=leng / res_len,
            height=height / res_len,
            validation=results[0].validation,
        )


class ResultCollection:
    def __init__(self, results: List[Result]) -> None:
        temp_data = defaultdict(lambda: defaultdict(list))
        for result in results:
            temp_data[result.name][result.amount].append(result)

        self.data = defaultdict(lambda: {})
        for name in sorted(temp_data.keys()):
            for amount in sorted(temp_data[name].keys()):
                self.data[name][amount] = Result.FROM_AVG(
                    temp_data[name][amount]
                )

    def _plot(
        self, title: str, picture_name: str, result_func: Callable
    ) -> None:
        for key, values in self.data.items():
            keys = list(values.keys())
            add_values = [result_func(result) for result in values.values()]

            plt.plot(keys, add_values, label=key)
            plt.scatter(keys, add_values)

        plt.xlabel("Amount of elements in BST")
        plt.ylabel("Time (s)")
        plt.title(title)
        plt.legend()
        plt.savefig(f"./results/{picture_name}.jpg")
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

    def to_json(self, merge_with_existing: bool = False) -> None:
        temp_data = {}
        for name in self.data.keys():
            temp_data[name] = {}
            for amount in self.data[name].keys():
                temp_data[name][amount] = self.data[name][amount].asdict()

        if merge_with_existing:
            with open("results.json", "r") as fp:
                actual_data = json.load(fp)
                actual_data.update(temp_data)
                temp_data = actual_data

        with open("results.json", "w") as fp:
            json.dump(temp_data, fp)

    def __repr__(self):
        return repr(self.data)
