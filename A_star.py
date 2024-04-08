from heapq import heappop, heappush
from graph import Node


class AStar:
    def __init__(self, start_state: Node, goal_state: Node, heuristic: callable) -> None:
        self.start_state: Node = start_state
        self.goal_state: Node = goal_state
        self.explored = set()
        self.heap: list[Node] = [start_state]
        self.heuristic: callable = heuristic

    def run(self):
        while self.heap:
            current: Node = heappop(self.heap)
            self.explored.add(current)

            if current == self.goal_state:
                break

            for edge in current.branches:
                child: Node = edge.target
                temp_g = current.g + edge.weight
                temp_f = temp_g + self.heuristic(current, self.goal_state)

                if child in self.explored and temp_f >= child.f:
                    continue

                if child not in self.heap or temp_f < child.f:
                    child.parent = current
                    child.g = temp_g
                    child.f = temp_f

                    if child in self.heap:
                        self.heap.remove(child)

                    heappush(self.heap, child)

    def show_solution(self):
        solution: list[Node] = []
        node: Node = self.goal_state
        while node:
            solution.append(node)
            node = node.parent
        print(solution[::-1])
