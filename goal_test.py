from graph import Node


# the Goal_Test function should be defined statically and be different for each problem
# and receive different data and return the desired data.
def goal_test(currentNode: Node, goalNode: Node = None):
    goal_node = goalNode
    if currentNode == goal_node:
        return True
    return False
