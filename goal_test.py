from graph import Node


# the Goal_Test function should be defined statically and be different for each problem
# and receive different data and return the desired data.


class GoalTest:
    def __init__(self, goalNode: Node) -> None:
        self.goalNode: Node = goalNode

    def goal_test(self, currentNode: Node):

        if currentNode == self.goalNode:
            return [self.goalNode, True]
        return [self.goalNode, False]
