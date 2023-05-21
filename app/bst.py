from dataclasses import dataclass
from pathlib import Path
from .result import Result
import subprocess
from logger import logger


@dataclass()
class BST:
    name: str
    path: Path

    def run(self, amount=10_000_000) -> Result:
        output = subprocess.run([self.path, str(amount)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = output.stdout
        return Result.FROM_RESULT(self.name, amount, result)
