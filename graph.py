class Node:
    def __init__(self, name: str, position: tuple, parent=None) -> None:
        self.name: str = name
        self.position: tuple = position
        self.parent: Node = parent
        self.branches: list[Edge] = []
        self.g: int | float = 0
        self.h: int | float = 0
        self.f: int | float = 0

    def add_branch(self, edge):
        self.branches.append(edge)

    def __lt__(self, othe_node):
        return self.f < othe_node.f

    def __repr__(self) -> str:
        return self.name


class Edge:
    def __init__(self, target: Node, weight: int | float) -> None:
        self.target: Node = target
        self.weight: int | float = weight
