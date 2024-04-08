from A_star import AStar
from graph import Edge, Node
from heuristic_function import heuristic
from goal_test import GoalTest


if __name__ == '__main__':
    n1 = Node("A", (0, 0))
    n2 = Node("B", (10, 20))
    n3 = Node("C", (20, 40))
    n4 = Node("D", (30, 10))
    n5 = Node("E", (40, 30))
    n6 = Node("F", (50, 10))
    n7 = Node("G", (50, 40))

    n1.add_branch(Edge(n2, 10))
    n1.add_branch(Edge(n4, 50))

    n2.add_branch(Edge(n3, 10))
    n2.add_branch(Edge(n4, 20))

    n3.add_branch(Edge(n5, 10))
    n3.add_branch(Edge(n7, 30))

    n4.add_branch(Edge(n6, 80))

    n5.add_branch(Edge(n6, 50))
    n5.add_branch(Edge(n7, 10))

    n7.add_branch(Edge(n6, 10))

    goalTestObject = GoalTest(n6)

    algorithm = AStar(n1, goalTestObject.goal_test, heuristic)
    algorithm.run()
    algorithm.show_solution()
