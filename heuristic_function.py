from graph import Node
from numpy import sqrt


def heuristic(node1: Node, node2: Node):
    return sqrt(((node1.position[0]-node2.position[0])**2)+((node1.position[1]-node2.position[1])**2))
