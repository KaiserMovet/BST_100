from typing import Any

from node import Node


class Tree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def add(self, value) -> bool:
        if self.root is None:
            self.root = Node(value)
            return True
        return self.root.add(value)

    def contain(self, value) -> bool:
        if self.root is None:
            return False
        return self.root.contain(value)

    def length(self) -> int:
        if self.root is None:
            return 0
        return self.root.length()

    def height(self) -> int:
        if self.root is None:
            return 0
        return self.root.height()
