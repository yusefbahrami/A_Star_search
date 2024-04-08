from graph import Node


# the Goal_Test function should be defined statically and be different for each problem
# and receive different data and return the desired data.

goal_node = None


def goal_test(currentNode: Node, goalNode: Node = None):
    if goal_node == None:
        goal_node = goalNode

    if currentNode == goal_node:
        return [goal_node, True]
    return [goal_node, False]
