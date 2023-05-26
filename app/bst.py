import subprocess
from dataclasses import dataclass
from pathlib import Path

from logger import logger

from .result import Result
from .runner import Runner


@dataclass()
class BST:
    name: str
    runner: Runner

    def run(self, amount=10_000_000) -> Result:
        output = self.runner.run(10)

        return Result.FROM_RESULT(self.name, amount, output)
