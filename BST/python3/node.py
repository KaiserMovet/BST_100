class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: "Node" | None = None
        self.right: "Node" | None = None

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def add(self, value) -> bool:
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                return True
            return self.left.add(value)

        if value > self.value:
            if self.right is None:
                self.right = Node(value)
                return True
            return self.right.add(value)

        return False

    def contain(self, value) -> bool:
        if value < self.value:
            if self.left is None:
                return False
            return self.left.contain(value)

        if value > self.value:
            if self.right is None:
                return False
            return self.right.contain(value)

        return True

    def length(self) -> int:
        a = 0 if self.left is None else self.left.length()
        b = 0 if self.right is None else self.right.length()
        return a + b + 1

    def height(self) -> int:
        return max(
            self.left.height() + 1 if self.left is not None else 1,
            self.right.height() + 1 if self.right is not None else 1,
        )
